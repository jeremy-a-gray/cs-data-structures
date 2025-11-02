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

"""Doubly-Linked Lists."""

from .node import DoublyLinkedNode  # noqa:  F401


class DoublyLinkedList:
    """Represent a doubly-linked list."""

    def __init__(self, *args):
        """Initialize the ``DoublyLinkedList``.

        Initialize the ``DoublyLinkedList``.  Append any items in
        ``args`` to the list in order.

        Parameters
        ----------
        args : list
            Items to append to the list.

        """
        self.head = None
        self.tail = None

        for item in args:
            self.append(item)

    def __repr__(self):
        """Reproduce the ``DoublyLinkedList``."""
        return "DoublyLinkedList(" + ", ".join([f"'{item!s}'" for item in self]) + ")"

    def __str__(self):
        """Stringify the ``DoublyLinkedList``."""
        return "[" + ", ".join([f"'{item!s}'" for item in self]) + "]"

    def __len__(self):
        """Find the length of the list.

        Returns
        -------
        int
            The length of the list.

        """
        pass

    def __iter__(self):
        """Iterate over the list."""
        pass

    def isEmpty(self):
        """Determine if the list is empty.

        Returns
        -------
        bool
            ``True`` if the list is empty, ``False`` otherwise.

        """
        pass

    def reverse(self):
        """Reverse the list."""
        pass

    def index(self, record):
        """Find the index of the matching ``record`` in the list.

        Returns
        -------
        int
            The zero-based index of the node matching ``record`` in
            the list.  Returns -1 if ``record`` is not found.

        """
        pass

    def find_head(self):
        """Find the head the list.

        Returns
        -------
        DoublyLinkedNode
            The head of the list.

        """
        pass

    def find_tail(self):
        """Find the tail the list.

        Returns
        -------
        DoublyLinkedNode
            The tail of the list.

        """
        pass

    def insert_before(self, new, record=None):
        """Insert a node into the list.

        Insert a new node with record ``new`` into the list before the
        node with record ``record``.  If no record is given, then
        prepend the new node onto the list.  If no record is found,
        then append the new node onto the list.

        """
        pass

    def insert_after(self, new, record=None):
        """Insert a node in the list.

        Insert a new node with record ``new`` into the list after the
        node with record ``record``.  If no record is given, then
        append the new node onto the list.  If no record is found,
        then append the new node onto the list.

        """
        pass

    def append(self, record):
        """Append ``record`` onto the end of the list.

        Parameters
        ----------
        record
            The value to be appended to the list.

        """
        pass

    def delete(self, record):
        """Remove the node matching ``record`` from the list.

        Returns
        -------
        record
            The ``record`` from the removed node or ``None`` if no
            node was removed.  Removes the first node matching
            ``record``.

        """
        pass

    def pop(self):
        """Remove the tail node from the list.

        Returns
        -------
        record
            The record of the removed node or ``None`` if empty.

        """
        pass
