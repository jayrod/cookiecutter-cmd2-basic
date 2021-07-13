#!/usr/bin/env python
# coding=utf-8
"""
A simple application using cmd2 

"""

import argparse
import cmd2

class App(cmd2.Cmd):
    """A simple cmd2 application."""

    def __init__(self):
        super().__init__()

    def do_special(self, args:cmd2.Statement):
        """Performs special command"""
        self.poutput("A Command")
