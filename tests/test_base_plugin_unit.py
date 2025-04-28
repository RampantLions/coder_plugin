from types import TracebackType
from typing import Optional, Type

import pytest
from coder_plugin.base_plugin_unit import BasePluginUnit


class DummyException(Exception):
    """Custom exception for testing purposes."""


def test_initialization_fields():
    unit = BasePluginUnit()

    # Class attributes
    assert BasePluginUnit.name is None
    assert BasePluginUnit.parent_group is None
    assert BasePluginUnit.plugin_group is None

    # Instance attributes
    # assert hasattr(unit, "logger")
    # assert isinstance(unit.logger, type(BasePluginUnit.logger))
    assert unit.parent is None
    assert isinstance(unit.children, list)
    assert unit.children == []


def test_context_manager_entry_exit_normal():
    unit = BasePluginUnit()

    with unit as entered_unit:
        assert entered_unit is unit


def test_context_manager_exit_no_exception():
    unit = BasePluginUnit()

    result = unit.__exit__(None, None, None)
    assert result is None  # Should not suppress anything


def test_context_manager_exit_with_exception():
    unit = BasePluginUnit()

    exc_type: Type[BaseException] = DummyException
    exc_value = DummyException("Test exception")
    tb: Optional[TracebackType] = None

    result = unit.__exit__(exc_type, exc_value, tb)
    assert result is None  # Should still propagate


def test_run_raises_not_implemented():
    unit = BasePluginUnit()
    with pytest.raises(NotImplementedError):
        unit.run()


def test_set_up_returns_self():
    unit = BasePluginUnit()
    result = unit.set_up()
    assert result is unit


def test_logger_debug_calls(monkeypatch):
    """
    Monkeypatch the logger to verify debug messages are being issued.
    """
    logs = []

    class DummyLogger:
        def debug(self, message: str):
            logs.append(message)

    unit = BasePluginUnit()
    monkeypatch.setattr(unit, "logger", DummyLogger())

    with unit:
        pass

    unit.set_up()

    with pytest.raises(NotImplementedError):
        unit.run()

    # At least these log messages must have been captured
    assert any("Prepare the BasePluginUnit plugin unit for context-managed execution." in m for m in logs)
    assert any("Cleaning up the BasePluginUnit plugin unit after context-managed execution." in m for m in logs)
    assert any("Performing unit setup task(s) for BasePluginUnit" in m for m in logs)
    assert any("Running unit task(s) for BasePluginUnit" in m for m in logs)


def test_parent_and_children_structure():
    parent_unit = BasePluginUnit()
    child_unit = BasePluginUnit()

    child_unit.parent = parent_unit
    parent_unit.children.append(child_unit)

    assert child_unit.parent is parent_unit
    assert child_unit in parent_unit.children
