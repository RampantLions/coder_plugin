#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import annotations
from loguru import logger

class BasePlugin:
    """A basic plugin unit."""

    # Static metadata per plugin
    name: str = None               # Unique plugin name
    parent_group: str = None        # Entry point group under which this plugin registers itself
    plugin_group: str = None        # Group this plugin will own for its children (optional)

    def __init__(self):
        self.logger = logger
        # "coder_plugin"
        self.parent = None  # If this plugin is also a child of another
        self.children = []  # If this plugin is a manager of children
        self.logger.debug(f"Initializing the {self.__class__.__name__} resource")
        pass

    def setup(self):
        """Perform setup tasks for this plugin."""
        pass

    def run(self):
        """Run the plugin's main logic."""
        raise NotImplementedError

    # Context Manager Support Enter
    def __enter__(self):
        self.logger.debug(f"Setting up the {self.__class__.__name__} resource")
        return self

    # Context Manager Support Exit
    def __exit__(self, exc_type, exc_value, traceback):
        self.logger.debug(f"Cleaning up the {self.__class__.__name__} resource")
