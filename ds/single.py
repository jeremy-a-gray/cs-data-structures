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

    def __init__(self):
        """Initialize the ``List``."""
        pass

    def __repr__(self):
        """Reproduce the ``List``."""
        pass

    def __str__(self):
        """Stringify the ``List``."""
        pass

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

    def index(self, node):
        """Find the index of ``Node`` ``node`` in the ``List``.

        Returns
        -------
        int
            The zero-based index of the ``Node`` ``node`` in the ``List``.

        """
        pass

    def head(self):
        """Find the head the ``List``.

        Returns
        -------
        Node
            The head of the ``List``.

        """
        pass

    def tail(self):
        """Find the tail the ``List``.

        Returns
        -------
        Node
            The tail of the ``List``.

        """
        pass

    def insert_before(self, node, record):
        """Insert a ``Node`` in a ``List``.

        Insert ``Node`` ``node`` into the ``List`` before the ``Node``
        with record ``record``.  If no record is given, then prepend
        ``node`` onto the list.  If no record is found, then append
        ``node`` onto the list.

        """
        pass

    def insert_after(self, node, record):
        """Insert a ``Node`` in a ``List``.

        Insert ``Node`` ``node`` into the ``List`` after the ``Node``
        with record ``record``.  If no record is given, then append
        ``node`` onto the list.  If no record is found, then append
        ``node`` onto the list.

        """
        pass

    def append(self, node):
        """Append ``Node`` ``node`` onto the end of the ``List``."""
        pass

    def delete(self, node):
        """Remove ``Node`` ``node`` from the ``List``.

        Returns
        -------
        Node
            The removed node.

        """
        pass

    def pop(self, node):
        """Remove ``Node`` ``node`` from the end of the ``List``.

        Returns
        -------
        Node
            The removed node.

        """
        pass
