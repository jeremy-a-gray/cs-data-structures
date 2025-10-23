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

"""Nodes."""


class Node:
    """Represent a node."""

    def __init__(self, record):
        """Initialize a ``Node``.

        Initialize a ``Node`` with a `record`` and ``next`` reference
        to the next item in the sequence.

        Parameters
        ----------
        record
            The value to be stored in the node.

        """
        self.record = record
        self.next = None

    def __repr__(self):
        """Reproduce a ``Node``."""
        return f"Node({self.record!r})"

    def __str__(self):
        """Stringify a ``Node``."""
        return f"{self.record!s}"


class DoublyLinkedNode:
    """Represent a doubly linked node."""

    def __init__(self, record):
        """Initialize a ``DoublyLinkedNode``.

        Initialize a ``DoublyLinkedNode`` with a `record`` and
        ``next`` and ``prev`` references to the next and previous
        items in the sequence.

        Parameters
        ----------
        record
            The value to be stored in the node.

        """
        self.record = record
        self.prev = None
        self.next = None

    def __repr__(self):
        """Reproduce a ``DoublyLinkedNode``."""
        return f"DoublyLinkedNode({self.record!r})"

    def __str__(self):
        """Stringify a ``DoublyLinkedNode``."""
        return f"{self.record!s}"
