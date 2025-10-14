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
        """Initialize a ``Node``."""
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

    def __init__(self):
        """Initialize a ``DoublyLinkedNode``."""
        pass

    def __repr__(self):
        """Reproduce a ``DoublyLinkedNode``."""
        pass

    def __str__(self):
        """Stringify a ``DoublyLinkedNode``."""
        pass
