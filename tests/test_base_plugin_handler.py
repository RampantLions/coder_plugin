from types import TracebackType
from typing import Optional, Type

import pytest

from coder_plugin.base_plugin_unit import BasePluginUnit


class DummyException(Exception):
    """Custom exception for testing purposes."""


class DummyLogger:
    def __init__(self, logs):
        self.logs = logs

    def debug(self, message: str):
        self.logs.append(message)


def test_initialization_fields():
    unit = BasePluginUnit()

    # Class attributes
    assert BasePluginUnit.name is None
    assert BasePluginUnit.parent_group is None
    assert BasePluginUnit.plugin_group is None

    # Instance attributes
    assert hasattr(unit, "logger")
    assert unit.parent is None
    assert isinstance(unit.children, list)
    assert unit.children == []


def test_context_manager_entry_exit_normal():
    logs = []
    unit = BasePluginUnit()
    unit.logger = DummyLogger(logs)

    with unit as entered_unit:
        assert entered_unit is unit

    result = unit.__exit__(None, None, None)
    assert result is None

    assert any("Prepare the BasePluginUnit plugin unit for context-managed execution." in msg for msg in logs)
    assert any("Cleaning up the BasePluginUnit plugin unit after context-managed execution." in msg for msg in logs)


def test_context_manager_exit_with_exception():
    logs = []
    unit = BasePluginUnit()
    unit.logger = DummyLogger(logs)

    exc_type: Type[BaseException] = DummyException
    exc_value = DummyException("test exception")
    tb: Optional[TracebackType] = None

    result = unit.__exit__(exc_type, exc_value, tb)
    assert result is None
    assert any("Cleaning up the BasePluginUnit plugin unit after context-managed execution." in msg for msg in logs)


def test_run_raises_not_implemented():
    logs = []
    unit = BasePluginUnit()
    unit.logger = DummyLogger(logs)

    with pytest.raises(NotImplementedError):
        unit.run()

    assert any("Running unit task(s) for BasePluginUnit" in msg for msg in logs)


def test_set_up_returns_self():
    logs = []
    unit = BasePluginUnit()
    unit.logger = DummyLogger(logs)

    result = unit.set_up()
    assert result is unit
    assert any("Performing unit setup task(s) for BasePluginUnit" in msg for msg in logs)


def test_parent_and_children_structure():
    parent_unit = BasePluginUnit()
    child_unit = BasePluginUnit()

    child_unit.parent = parent_unit
    parent_unit.children.append(child_unit)

    assert child_unit.parent is parent_unit
    assert child_unit in parent_unit.children
