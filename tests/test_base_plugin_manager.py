import importlib.metadata
from types import TracebackType
from typing import Optional, Type

import pytest

from coder_plugin.base_plugin_manager import BasePluginManager
from coder_plugin.base_plugin_unit import BasePluginUnit


# Dummy classes
class DummyException(Exception):
    pass


class DummyLogger:
    def __init__(self, logs):
        self.logs = logs

    def debug(self, message: str):
        self.logs.append(message)


class DummyChildPlugin(BasePluginUnit):  # type: ignore
    def run(self, *args, **kwargs):  # type: ignore
        return "child_run"

    def set_up(self, *args, **kwargs):  # type: ignore
        return self


class DummyEntryPoint:
    def __init__(self, name):  # type: ignore
        self.name = name

    def load(self):  # type: ignore
        return DummyChildPlugin


class DummyEntryPointsFound:
    def select(self, group=None):  # type: ignore
        return [DummyEntryPoint("test_plugin")]  # type: ignore


class DummyEntryPointsEmpty:
    def select(self, group=None):
        return []


class ManagerWithNoPluginGroup(BasePluginManager):  # type: ignore
    plugin_group = None


# --- Core Tests ---


def test_initialization_without_auto_load():
    manager = BasePluginManager(auto_load_children=False)
    assert isinstance(manager, BasePluginManager)
    assert manager.parent is None
    assert isinstance(manager.children, list)
    assert manager.children == []


def test_initialization_with_auto_load(monkeypatch):
    called = {}

    def dummy_load_children(self):
        called["load_children"] = True

    monkeypatch.setattr(BasePluginManager, "load_children", dummy_load_children)
    BasePluginManager(auto_load_children=True)
    assert called.get("load_children") is True


def test_context_manager_entry_exit_normal():
    logs = []
    manager = BasePluginManager()
    manager.logger = DummyLogger(logs)

    with manager as entered:
        assert entered is manager

    result = manager.__exit__(None, None, None)
    assert result is None

    assert any("Prepare the BasePluginManager plugin manager for context-managed execution." in m for m in logs)
    assert any("Cleaning up the BasePluginManager plugin manager after context-managed execution." in m for m in logs)


def test_context_manager_exit_with_exception():
    logs = []
    manager = BasePluginManager()
    manager.logger = DummyLogger(logs)

    exc_type: Type[BaseException] = DummyException
    exc_value = DummyException("test")
    tb: Optional[TracebackType] = None

    result = manager.__exit__(exc_type, exc_value, tb)
    assert result is None

    assert any("Cleaning up the BasePluginManager plugin manager after context-managed execution." in m for m in logs)


# --- load_children() Branches ---


def test_load_children_plugin_group_none(monkeypatch):
    # manager = BasePluginManager()
    # monkeypatch.setattr(BasePluginManager, "plugin_group", None)
    #
    # manager.load_children()
    # assert manager.children == []

    # Patch class plugin_group BEFORE manager instance creation
    monkeypatch.setattr(BasePluginManager, "plugin_group", None)
    logs = []
    # manager = BasePluginManager()
    manager = ManagerWithNoPluginGroup()
    manager.logger = DummyLogger(logs)  # type: ignore
    manager.load_children()
    assert manager.children == []

    # We expect NO loading message because it returned early
    assert not any("Loading" in m for m in logs)


def test_load_children_with_plugins(monkeypatch):  # type: ignore
    logs = []
    manager = BasePluginManager()
    manager.logger = DummyLogger(logs)

    monkeypatch.setattr(BasePluginManager, "plugin_group", "dummy.group")
    monkeypatch.setattr(importlib.metadata, "entry_points", lambda: DummyEntryPointsFound())

    manager.load_children()

    assert len(manager.children) == 1
    assert isinstance(manager.children[0], DummyChildPlugin)
    assert manager.children[0].parent is manager
    assert any("Loading BasePluginManager children plugins" in m for m in logs)


# --- load_from_parent_group() Branches ---


def test_load_from_parent_group_success(monkeypatch):  # type: ignore
    monkeypatch.setattr(importlib.metadata, "entry_points", lambda: DummyEntryPointsFound())

    plugin = BasePluginManager.load_from_parent_group("dummy.group", "test_plugin")
    assert isinstance(plugin, DummyChildPlugin)


def test_load_from_parent_group_lookup_error(monkeypatch):  # type: ignore
    monkeypatch.setattr(importlib.metadata, "entry_points", lambda: DummyEntryPointsEmpty())

    with pytest.raises(LookupError) as exc_info:
        BasePluginManager.load_from_parent_group("dummy.group", "missing_plugin")

    assert "Plugin missing_plugin not found in group dummy.group" in str(exc_info.value)


# --- run() and set_up() fan-out ---


def test_run_forwards_to_children():  # type: ignore
    logs = []  # type: ignore
    manager = BasePluginManager()
    manager.logger = DummyLogger(logs)  # type: ignore

    dummy_child = DummyChildPlugin()
    dummy_child.logger = DummyLogger(logs)  # type: ignore

    manager.children.append(dummy_child)

    result = manager.run()

    assert result is None
    assert any("Running managed task(s) for BasePluginManager plugins" in m for m in logs)
    assert any("Running the DummyChildPlugin plugin" in m for m in logs)


def test_set_up_forwards_to_children():  # type: ignore
    logs = []  # type: ignore
    manager = BasePluginManager()
    manager.logger = DummyLogger(logs)  # type: ignore

    dummy_child = DummyChildPlugin()

    dummy_child.logger = DummyLogger(logs)  # type: ignore
    manager.children.append(dummy_child)

    result = manager.set_up()

    assert result is manager
    assert any("Performing managed setup task(s) for BasePluginManager plugins" in m for m in logs)
    assert any("Setting up DummyChildPlugin plugin" in m for m in logs)


def test_load_from_parent_group_candidate_found_but_no_match(monkeypatch):  # type: ignore
    class DummyEntryPointNoMatch:
        def __init__(self):  # type: ignore
            self.name = "wrong_plugin"

        def load(self):  # type: ignore
            return DummyChildPlugin

    class DummySelectableWithWrongPlugin:
        def select(self, group=None):  # type: ignore
            return [DummyEntryPointNoMatch()]  # type: ignore # Candidate exists, but wrong name

    monkeypatch.setattr(importlib.metadata, "entry_points", lambda: DummySelectableWithWrongPlugin())

    with pytest.raises(LookupError) as exc_info:
        BasePluginManager.load_from_parent_group("dummy.group", "expected_plugin")

    assert "Plugin expected_plugin not found in group dummy.group" in str(exc_info.value)
