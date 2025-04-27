#!/usr/bin/env python
# -*- coding: utf-8 -*-

# coder_plugin/base_plugin_handler.py

from __future__ import annotations
from coder_plugin.base_plugin_unit import BasePluginUnit
from typing import Any, Optional, Self, Type

class BasePluginHandler(BasePluginUnit):
    """
    A basic plugin unit.

    Provides a foundation for plugins that can be dynamically discovered and loaded
    via Python entry points. Supports runtime set up, execution, and context management.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the plugin handler."""
        super().__init__()
        self.logger.debug(f"Initializing the {self.__class__.__name__}")

    def __enter__(self) -> Self:
        """
        Context manager entry.

        Prepares the plugin for context-managed operations.

        Returns:
            Self: The plugin instance itself.
        """

        self.logger.debug(f"Prepare the {self.__class__.__name__} plugin handler for context-managed execution.")
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[object]
    ) -> Optional[bool]:
        """
        Context manager exit.

        Cleans up resources when exiting the plugin handler context-managed execution.

        Args:
            exc_type (Optional[Type[BaseException]]): Exception type, if any.
            exc_value (Optional[BaseException]): Exception instance, if any.
            traceback (Optional[object]): Traceback object, if any.

        Returns:
            Optional[bool]:
                - True to suppress the exception.
                - False or None to propagate the exception.
        """
        self.logger.debug(f"Cleaning up the {self.__class__.__name__} plugin handler after context-managed execution.")

        # Example logic: suppress all exceptions
        # return True

        # Example logic: suppress only specific exception types
        # if exc_type and issubclass(exc_type, SomeExpectedException):
        #     self.logger.warning(f"Suppressed {exc_type.__name__}: {exc_value}")
        #     return True

        # Default: do not suppress
        return None

    def run(self, *args: Any, **kwargs: Any) -> Any:
        """
        Run the plugin handler's main logic.

        This method must be implemented by subclasses.

        Args:
            *args (Any): Positional arguments for plugin's run logic.
            **kwargs (Any): Keyword arguments for plugin's run logic.

        Returns:
            Any: The result of the plugin handler's execution, as defined by the subclass.

        Raises:
            NotImplementedError: If not overridden by a subclass.
        """
        self.logger.debug(f"Running handler {self.__class__.__name__}")
        raise NotImplementedError

    def set_up(self, *args: Any, **kwargs: Any) -> Self:
        """
        Perform setup task(s) for this plugin.

        This method should be overridden by subclasses to implement any required
        initialization logic before running the plugin.

        Returns:
            Self: Enables fluent chaining after set up.
        """

        self.logger.debug(f"Performing handler setup task(s) for {self.__class__.__name__}")
        return self
