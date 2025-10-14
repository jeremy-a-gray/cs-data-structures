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

"""Singly-linked lists."""

from .node import Node  # noqa:  F401


class List:
    """Represent a list."""

    def __init__(self, *args):
        """Initialize the ``List``.

        Initialize the ``List``.  Append any items in ``args`` to the
        list in order.

        Parameters
        ----------
        args : list
            Items to append to the list.

        """
        self.head = None

        for item in args:
            self.append(item)

    def __repr__(self):
        """Reproduce the ``List``."""
        return "List(" + ", ".join([f"'{item!s}'" for item in self]) + ")"

    def __str__(self):
        """Stringify the ``List``."""
        return "[" + ", ".join([f"'{item!s}'" for item in self]) + "]"

    def __len__(self):
        """Find the length of the ``List``.

        Returns
        -------
        int
            The length of the list.

        """
        pass

    def __iter__(self):
        """Iterate over the list.

        Iterate over the list to enable iterator protocol.

        """
        pass

    def isEmpty(self):
        """Determine if the ``List`` is empty.

        Returns
        -------
        bool
            ``True`` if the ``List`` is empty, ``False`` otherwise.

        """
        pass

    def reverse(self):
        """Reverse the ``List``."""
        pass

    def index(self, record):
        """Find the index of the ``Node`` matching ``record`` in the ``List``.

        Returns
        -------
        int
            The zero-based index of the ``Node`` matching ``record``
            in the ``List``.  Returns -1 if ``record`` is not found.

        """
        pass

    def find_head(self):
        """Find the head the ``List``.

        Returns
        -------
        Node
            The head of the ``List``.

        """
        pass

    def find_tail(self):
        """Find the tail the ``List``.

        Returns
        -------
        Node
            The tail of the ``List``.

        """
        pass

    def insert_before(self, new, record):
        """Insert a ``Node`` in a ``List``.

        Insert ``Node`` ``node`` into the ``List`` before the ``Node``
        with record ``record``.  If no record is given, then prepend
        ``node`` onto the list.  If no record is found, then append
        ``node`` onto the list.

        """
        pass

    def insert_after(self, new, record):
        """Insert a ``Node`` in a ``List``.

        Insert ``new`` into the ``List`` after the ``Node`` with
        record ``record``.  If no record is given, then append
        ``node`` onto the list.  If no record is found, then append
        ``node`` onto the list.

        """
        pass

    def append(self, record):
        """Append ``record`` onto the end of the ``List``."""
        pass

    def delete(self, record):
        """Remove ``Node`` matching ``record`` from the ``List``.

        Returns
        -------
        Node
            The removed node or ``None`` if no node removed.  Removes
            the first ```Node`` matching ``record``.

        """
        pass

    def pop(self):
        """Remove ``Node`` from the end of the ``List``.

        Returns
        -------
        Node
            The removed node or ``None`` if empty.

        """
        pass
