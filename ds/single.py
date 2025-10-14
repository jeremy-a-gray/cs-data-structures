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

from .node import Node


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
        # Empty list.
        if self.isEmpty():
            return 0

        # Non-empty list.  Start at the head.
        cur = self.head
        length = 1

        # Iterate until there is no next.
        while cur.next is not None:
            cur = cur.next
            length += 1

        return length

    def __iter__(self):
        """Iterate over the list."""
        cur = self.head

        while cur is not None:
            yield cur
            cur = cur.next

    def isEmpty(self):
        """Determine if the ``List`` is empty.

        Returns
        -------
        bool
            ``True`` if the ``List`` is empty, ``False`` otherwise.

        """
        return True if self.head is None else False

    def reverse(self):
        """Reverse the ``List``."""
        if self.isEmpty():
            return

        last = None
        next = None
        cur = self.head

        # Iterate over list.
        while cur is not None:
            next = cur.next
            cur.next = last
            last = cur
            cur = next

        self.head = last

        return

    def index(self, record):
        """Find the index of the ``Node`` matching ``record`` in the ``List``.

        Returns
        -------
        int
            The zero-based index of the ``Node`` matching ``record``
            in the ``List``.  Returns -1 if ``record`` is not found.

        """
        ind = 0
        cur = self.head

        # Iterate until there is no next.
        while cur is not None:
            if cur.record == record:
                return ind

            cur = cur.next
            ind += 1

        return -1

    def find_head(self):
        """Find the head the ``List``.

        Returns
        -------
        Node
            The head of the ``List``.

        """
        return self.head

    def find_tail(self):
        """Find the tail the ``List``.

        Returns
        -------
        Node
            The tail of the ``List``.

        """
        # Empty list.
        if self.isEmpty():
            return self.head

        # Non-empty list.  Start at the head.
        cur = self.head

        # Iterate until there is no next.
        while cur.next is not None:
            cur = cur.next

        return cur

    def insert_before(self, new, record):
        """Insert a ``Node`` in a ``List``.

        Insert ``Node`` ``node`` into the ``List`` before the ``Node``
        with record ``record``.  If no record is given, then prepend
        ``node`` onto the list.  If no record is found, then append
        ``node`` onto the list.

        """
        node = Node(new)

        if self.isEmpty():
            self.head = node
            self.head.next = None
            return

        last = None
        cur = self.head

        # Iterate until there is no next.
        while cur is not None:
            if cur.record == record:
                # Append the node.
                if cur == self.head:
                    node.next = self.head
                    self.head = node
                else:
                    last.next = node
                    node.next = cur

                return

            last = cur
            cur = cur.next

        # No match.
        last.next = node
        node.next = None

        return

    def insert_after(self, new, record):
        """Insert a ``Node`` in a ``List``.

        Insert ``new`` into the ``List`` after the ``Node`` with
        record ``record``.  If no record is given, then append
        ``node`` onto the list.  If no record is found, then append
        ``node`` onto the list.

        """
        node = Node(new)

        if self.isEmpty():
            self.head = node
            self.head.next = None
            return

        last = None
        cur = self.head

        # Iterate until there is no next.
        while cur is not None:
            if cur.record == record:
                # Append the node.
                node.next = cur.next
                cur.next = node

                return

            last = cur
            cur = cur.next

        # No match.
        last.next = node
        node.next = None

        return

    def append(self, record):
        """Append ``record`` onto the end of the ``List``."""
        node = Node(record)

        # Empty list.
        if self.isEmpty():
            self.head = node
            node.next = None
            return

        # Non-empty list; get the tail.
        cur = self.find_tail()

        # Append ``node`` and fix the tail.
        cur.next = node
        node.next = None

    def delete(self, record):
        """Remove ``Node`` matching ``record`` from the ``List``.

        Returns
        -------
        Node
            The removed node or ``None`` if no node removed.  Removes
            the first ```Node`` matching ``record``.

        """
        cur = self.head
        last = None

        # Iterate until there is no next.
        while cur is not None:
            if cur.record == record:
                # Delete the node.
                if cur == self.head:
                    self.head = self.head.next
                else:
                    last.next = cur.next

                # Return the match.
                return record

            last = cur
            cur = cur.next

        # No match.
        return None

    def pop(self):
        """Remove ``Node`` from the end of the ``List``.

        Returns
        -------
        Node
            The removed node or ``None`` if empty.

        """
        # Empty list.
        if self.isEmpty():
            return None

        # Non-empty list.  Start at the head.
        cur = self.head

        # Iterate until there is no next.
        while cur.next is not None:
            last = cur
            cur = cur.next

        # Fix tail.
        last.next = None

        # Return former tail.
        return cur.record
