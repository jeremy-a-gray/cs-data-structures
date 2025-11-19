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

from .node import Node


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
        cur = self.head
        count = 0

        while cur is not None:
            count += 1
            cur = cur.next

        return count

    def __iter__(self):
        """Iterate over the ``Stack``.

        Iterate over the stack from head to tail to enable iterator
        protocol.

        """
        cur = self.head

        while cur is not None:
            yield cur
            cur = cur.next

        return

    def isEmpty(self):
        """Determine if the ``Stack`` is empty.

        Returns
        -------
        bool
            ``True`` if the ``Stack`` is empty, ``False`` otherwise.

        """
        return True if len(self) == 0 else False

    def push(self, record):
        """Push a ``record`` onto a ``Stack``.

        Parameters
        ----------
        record
            The record to be pushed onto the tail of stack.

        """
        # Build the node.
        node = Node(record)

        # Push onto the tail.

        # Empty list.
        if self.isEmpty():
            self.head = node
            self.tail = node
            return

        # Non-empty list; append the node and fix the tail.
        self.tail.next = node
        self.tail = node

        return

    def pop(self):
        """Pop the tail from the ``Stack``.

        Returns
        -------
        record
            The record from the tail from the stack.

        """
        # Empty stack.
        if self.tail is None:
            return None

        record = self.tail.record

        if self.head == self.tail:
            # Length one stack.
            self.head = None
            self.tail = None
        else:
            # Length many stack.

            # Traverse the list.
            cur = self.head
            last = None
            before = None

            while cur is not None:
                before = last
                last = cur
                cur = cur.next

            self.tail = before
            self.tail.next = None

        return record
