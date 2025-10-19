# ******************************************************************************
#
# cs-data-structures, computer science data structures
#
# Copyright 2025 Jeremy A Gray <grayj2@wcslive.com>.
#
# All rights reserved.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# ******************************************************************************

"""Stacks."""

from .node import DoublyLinkedNode  # noqa:  F401


class Stack:
    """Represent a stack."""

    def __init__(self):
        """Initialize a ``Stack``."""
        pass

    def __repr__(self):
        """Reproduce a ``Stack``."""
        pass

    def __str__(self):
        """Stringify a ``Stack``."""
        pass

    def push(self, record):
        """Push a ``record`` onto a ``Stack``.

        Parameters
        ----------
        record
            The record to be pushed onto the head of stack.

        """
        pass

    def pop(self):
        """Pop the head from a ``Stack``.

        Returns
        -------
        record
            The record from the head of the stack.

        """
        pass
