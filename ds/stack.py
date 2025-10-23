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

    def __init__(self, *args):
        """Initialize the ``Stack``.

        Initialize the ``Stack``.  Push any items in ``args`` to the
        stack in order.

        Parameters
        ----------
        args : list
            Items to append to the stack.

        """
        self.head = None
        self.tail = None

        for item in args:
            self.push(item)

    def __repr__(self):
        """Reproduce the ``Stack``."""
        return "Stack(" + ", ".join([f"'{item!s}'" for item in self]) + ")"

    def __str__(self):
        """Stringify the ``Stack``."""
        return "[" + ", ".join([f"'{item!s}'" for item in self]) + "]"

    def __len__(self):
        """Find the length of the ``Stack``.

        Returns
        -------
        int
            The length of the stack.

        """
        pass

    def __iter__(self):
        """Iterate over the ``Stack``.

        Iterate over the stack from head to tail to enable iterator
        protocol.

        """
        pass

    def isEmpty(self):
        """Determine if the ``Stack`` is empty.

        Returns
        -------
        bool
            ``True`` if the ``Stack`` is empty, ``False`` otherwise.

        """
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
        """Pop the tail from the ``Stack``.

        Returns
        -------
        record
            The record from the tail from the stack.

        """
        pass
