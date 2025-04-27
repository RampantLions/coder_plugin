#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import annotations
from .base_plugin import BasePlugin
import importlib.metadata

class PluginManager(BasePlugin):
    """Manages discovery and loading of sub-plugins for a specific plugin group."""

    def __init__(self, auto_load_children: bool = False):
        """
        Initializes the PluginManager.

        :param auto_load_children: If True, automatically load children upon initialization.
        """
        super().__init__()
        # "coder_plugin.plugin_manager:PluginManager"
        self.sub_plugins = []

        if auto_load_children:
            self.load_children()

    def load_children(self):
        """Discover and load child plugins dynamically via this plugin's plugin_group."""
        if not self.plugin_group:
            return

        entry_points = importlib.metadata.entry_points()
        children_eps = entry_points.select(group=self.plugin_group)

        for ep in children_eps:
            plugin_cls = ep.load()
            plugin_instance = plugin_cls()
            plugin_instance.parent = self
            self.children.append(plugin_instance)

    def setup(self):
        for plugin in self.children:
            plugin.setup()

    def run(self):
        for plugin in self.children:
            plugin.run()

    # Context Manager Support Enter
    def __enter__(self):
        self.logger.debug(f"Setting up the {self.__class__.__name__} resource")
        return self

    # Context Manager Support Exit
    def __exit__(self, exc_type, exc_value, traceback):
        self.logger.debug(f"Cleaning up the {self.__class__.__name__} resource")

    @classmethod
    def load_from_parent_group(cls, parent_group: str, parent_name: str):
        """
        Discover and load a plugin from a parent group by its registered name.
        Useful for cases where the app needs to bootstrap starting from the top.
        """
        entry_points = importlib.metadata.entry_points()
        candidates = entry_points.select(group=parent_group)

        for ep in candidates:
            if ep.name == parent_name:
                plugin_cls = ep.load()
                return plugin_cls()

        raise LookupError(f"Plugin {parent_name} not found in group {parent_group}")
