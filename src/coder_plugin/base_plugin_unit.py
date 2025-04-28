#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Base plugin unit for the coder_plugin system.

Defines shared fields and behaviors (logger, parent, children) for all plugins,
including context management, runtime setup, and execution contract enforcement.
"""

from __future__ import annotations

from typing import Any, List, Optional, Self, Type

from loguru import logger  # type: ignore


class BasePluginUnit:
    """
    Common base class for plugin units.

    Provides shared infrastructure fields including logging, parent linkage,
    and child management for hierarchical plugin systems.

    Attributes:
        name (Optional[str]): The unique identifier for this plugin class when registered
            with Python’s entry point system.
        parent_group (Optional[str]): The entry point group under which this plugin registers itself.
        plugin_group (Optional[str]): The entry point group that this plugin will own for discovering its children
            (if it acts as a plugin manager).
        logger (loguru.Logger): Logger instance attached to this plugin.
        parent (Optional[BasePluginUnit]): The runtime parent of this plugin instance.
        children (List[BasePluginUnit]): List of runtime-loaded child plugin instances.
    """

    name: Optional[str] = None
    parent_group: Optional[str] = None
    plugin_group: Optional[str] = None

    def __init__(self, *args: Any, **kwargs: Any):
        """
        Initialize a BasePluginUnit instance.

        Args:
            *args (Any): Positional arguments (currently unused).
            **kwargs (Any): Keyword arguments (currently unused).
        """

        self.logger: logger.__class__ = logger  # type: ignore
        self.parent: Optional[BasePluginUnit] = None  # type: ignore
        self.children: List[BasePluginUnit] = []  # type: ignore

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
            Optional[bool]: True to suppress the exception, False or None to propagate.
        """

        self.logger.debug(f"Cleaning up the {self.__class__.__name__} plugin unit after context-managed execution.")

        # Default: do not suppress
        return None

    def run(self, *args: Any, **kwargs: Any) -> Any:
        """
        Run the plugin unit's main logic.

        This method must be implemented by subclasses.

        Args:
            *args (Any): Positional arguments for the plugin unit's run logic.
            **kwargs (Any): Keyword arguments for the plugin unit's run logic.

        Returns:
            Any: The result of the plugin unit's execution.

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

        Args:
            *args (Any): Positional arguments for the plugin unit's set up logic.
            **kwargs (Any): Keyword arguments for the plugin unit's set up logic.

        Returns:
            Self: Enables fluent chaining after set up.
        """

        self.logger.debug(f"Performing unit setup task(s) for {self.__class__.__name__}")
        return self
