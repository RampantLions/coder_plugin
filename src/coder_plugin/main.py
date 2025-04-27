#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import annotations
from .root_plugin import RootPluginManager

def main():
    # Instantiate root manager
    root_manager = RootPluginManager()

    # Load first layer of plugins
    root_manager.load_children()

    # Recursively setup
    root_manager.setup()

    # Run everything
    root_manager.run()
