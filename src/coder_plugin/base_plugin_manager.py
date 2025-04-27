#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Base plugin manager for the coder_plugin system.

Provides plugin discovery, dynamic loading, and context management
for organized hierarchical plugin systems.

"""

# coder_plugin/base_plugin_manager.py

from __future__ import annotations

import importlib.metadata

from typing import Any, Optional, Self, Type

from .base_plugin_unit import BasePluginUnit


class BasePluginManager(BasePluginUnit):
    """
    Manages discovery and loading of sub-plugins for a specific plugin group.

    This base class provides dynamic plugin discovery using Python entry points,
    hierarchical plugin management, and context management support.
    """

    def __enter__(self) -> Self:
        """
        Context manager entry.

        Prepares the plugin manager for context-managed execution.

        Returns:
            Self: Enables context management with 'with' blocks.
        """

        self.logger.debug(f"Prepare the {self.__class__.__name__} plugin manager for context-managed execution.")
        return self # pylint: disable=useless-return

    # pylint: disable=useless-return
    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[Any],
    ) -> Optional[bool]:
        """
        Context manager exit.

        Cleans up resources when exiting the plugin manager context-managed execution.

        Args:
            exc_type (Optional[Type[BaseException]]): Exception type, if any.
            exc_value (Optional[BaseException]): Exception instance, if any.
            traceback (Optional[Any]): Traceback object, if any.

        Returns:
            Optional[bool]:
                - True to suppress the exception.
                - False or None to propagate the exception.
        """
        self.logger.debug(f"Cleaning up the {self.__class__.__name__} plugin manager after context-managed execution.")

        # Example logic: suppress all exceptions
        # return True

        # Example logic: suppress only specific exception types
        # if exc_type and issubclass(exc_type, SomeExpectedException):
        #     self.logger.warning(f"Suppressed {exc_type.__name__}: {exc_value}")
        #     return True

        # Default: do not suppress
        return None

    def __init__(self, *args: Any, auto_load_children: bool = False, **kwargs: Any) -> None:
        """
        Initialize the PluginManager.

        Args:
            auto_load_children (bool):
                If True, automatically load children upon initialization.
        """
        super().__init__(*args, **kwargs)

        if auto_load_children:
            self.load_children()

    def load_children(self) -> None:
        """
        Discover and load child plugins dynamically via this plugin's plugin_group.

        Defensive coding:
            - If no plugin group is defined, loading is skipped.
            - In the future, consider raising an exception if no plugin_group is set.
        """
        plugin_group = type(self).plugin_group
        if plugin_group is None:
            self.logger.debug(f"{self.__class__.__name__}: Plugin group was None; skipping load.")
            return

        self.logger.debug(f"Loading {self.__class__.__name__} children plugins")
        entry_points = importlib.metadata.entry_points()
        children_eps = entry_points.select(group=plugin_group)

        for ep in children_eps:
            plugin_cls = ep.load()
            plugin_instance = plugin_cls()
            if plugin_instance != self:
                self.logger.debug(
                    f" ╰─▶  Loading {ep.__class__.__name__} entry_point with {plugin_instance.__class__.__name__}."
                )
                plugin_instance.parent = self
                self.children.append(plugin_instance)

    # pylint: disable=useless-return
    def run(self, *args: Any, **kwargs: Any) -> Any:
        """
        Run the plugin manager's main logic.

        Args:
            *args (Any): Positional arguments forwarded to each child plugin.
            **kwargs (Any): Keyword arguments forwarded to each child plugin.

        Returns:
            Any: The result of the plugin manager's execution, as defined by the subclass.
        """

        self.logger.debug(f"Running managed task(s) for {self.__class__.__name__} plugins")
        for plugin in self.children:
            self.logger.debug(f" ╰─▶  Running the {plugin.__class__.__name__} plugin")
            plugin.run(*args, **kwargs)
        return None

    def set_up(self, *args: Any, **kwargs: Any) -> Self:
        """
        Perform setup task(s) for all loaded child plugins.

        Returns:
            Self: Enables fluent chaining after set up.
        """
        self.logger.debug(f"Performing managed setup task(s) for {self.__class__.__name__} plugins")
        for plugin in self.children:
            self.logger.debug(f" ╰─▶  Setting up {plugin.__class__.__name__} plugin")
            plugin.set_up(*args, **kwargs)
        return self

    @classmethod
    def load_from_parent_group(cls: Type[Self], parent_group: str, parent_name: str, *args: Any, **kwargs: Any) -> Self:
        """
        Discover and load a plugin from a parent group by its registered name.

        Args:
            parent_group (str): The entry point group where the parent plugin is registered.
            parent_name (str): The registered name of the plugin to load.
            *args (Any): Positional arguments to pass to the plugin constructor.
            **kwargs (Any): Keyword arguments to pass to the plugin constructor.

        Returns:
            Self: An instantiated plugin object.

        Raises:
            LookupError: If no plugin with the specified name is found.

        Notes:
            → If no additional arguments are needed, the plugin class will be instantiated with no arguments.
            → If arguments are needed, they will be passed through *args and **kwargs.

        """
        entry_points = importlib.metadata.entry_points()
        candidates = entry_points.select(group=parent_group)

        for ep in candidates:
            if ep.name == parent_name:
                plugin_cls = ep.load()
                return plugin_cls(*args, **kwargs)

        raise LookupError(f"Plugin {parent_name} not found in group {parent_group}")
