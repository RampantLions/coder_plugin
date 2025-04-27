#!/usr/bin/env python
# -*- coding: utf-8 -*-

# coder_plugin/base_plugin_unit.py

from __future__ import annotations
from typing import Any, List, Optional, Self, Type
from loguru import logger  # type: ignore

class BasePluginUnit:
    """
    Common base class for plugin units.

    Provides shared infrastructure fields including logging, parent linkage,
    and child management for hierarchical plugin systems.

    Class Attributes:
    name (Optional[str]):
        Purpose:
            The unique identifier for this plugin class when registered with Python’s entry point system.
        Usage:
            →  Used by systems like importlib.metadata.entry_points() to match and discover a plugin implementation.
            →  Acts as the lookup key when loading specific plugins dynamically.

    parent_group (Optional[str]):
        Purpose:
            The entry point group under which this plugin registers itself.
        Usage:
            →  When this plugin is loaded via entry_points(), it is found inside the group specified by parent_group.
            →  This organizes plugins of the same type into namespaces.

    plugin_group (Optional[str]):
        Purpose:
            The entry point group that this plugin will own for discovering its children (if it acts as a plugin manager).
        Usage:
            →  If this plugin loads other plugins dynamically, it looks under plugin_group for child plugins to attach.
            →  Enables hierarchical plugin trees where a plugin manages subordinate plugins.
    """

    name: Optional[str] = None
    parent_group: Optional[str] = None
    plugin_group: Optional[str] = None

    def __enter__(self) -> Self:
        """
        Context manager entry.

        Prepares the plugin unit for context-managed execution.

        Returns:
            Self: Enables context management with 'with' blocks.
        """

        self.logger.debug(f"Prepare the {self.__class__.__name__} plugin unit for context-managed execution.")
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[Any],
    ) -> Optional[bool]:
        """
        Context manager exit.

        Cleans up resources when exiting the plugin unit context-managed execution.

        Args:
            exc_type (Optional[Type[BaseException]]): Exception type, if any.
            exc_value (Optional[BaseException]): Exception instance, if any.
            traceback (Optional[Any]): Traceback object, if any.

        Returns:
            Optional[bool]:
                - True to suppress the exception.
                - False or None to propagate the exception.
        """
        self.logger.debug(f"Cleaning up the {self.__class__.__name__} plugin unit after context-managed execution.")

        # Example logic: suppress all exceptions
        # return True

        # Example logic: suppress only specific exception types
        # if exc_type and issubclass(exc_type, SomeExpectedException):
        #     self.logger.warning(f"Suppressed {exc_type.__name__}: {exc_value}")
        #     return True

        # Default: do not suppress
        return None

    def __init__(self, *args: Any, **kwargs: Any):
        """
        Initialize the plugin unit.

        Instance Attributes:
            logger (loguru.Logger): Logger instance attached to this plugin.
            parent (Optional[BasePluginUnit]):
                → The runtime parent of this plugin instance, if attached to a manager.
                → Enables back-reference to the plugin that created or is managing this plugin,
                  supporting hierarchical plugin trees.
            children (List[BasePluginUnit]):
                → List of runtime-loaded child plugin instances.
                → Enables recursive set up, execution, and teardown across plugin trees.
        """
        self.logger: logger.__class__ = logger  # type: ignore
        self.parent: Optional[BasePluginUnit] = None  # type: ignore
        self.children: List[BasePluginUnit] = []  # type: ignore

    def run(self, *args: Any, **kwargs: Any) -> Any:
        """
        Run the plugin unit's main logic.

        This method must be implemented by subclasses.

        Args:
            *args (Any): Positional arguments for plugin unit.
            **kwargs (Any): Keyword arguments for plugin unit.

        Returns:
            Any: The result of the plugin unit's execution, as defined by the subclass.

        Raises:
            NotImplementedError: If not overridden by a subclass.
        """

        self.logger.debug(f"Running unit task(s) for {self.__class__.__name__}")
        raise NotImplementedError

    def set_up(self, *args: Any, **kwargs: Any) -> Self:
        """
        Perform setup task(s) for this plugin unit.

        This method should be overridden by subclasses to implement any required
        initialization logic before running the plugin.

        Returns:
            Self: Enables fluent chaining after set up.
        """

        self.logger.debug(f"Performing unit setup task(s) for {self.__class__.__name__}")
        return self
