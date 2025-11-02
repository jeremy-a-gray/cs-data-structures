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

from .node import DoublyLinkedNode


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
        # Empty list.
        if self.isEmpty():
            return 0

        # Traverse the list.
        cur = self.head
        length = 0

        while cur is not None:
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
        """Determine if the list is empty.

        Returns
        -------
        bool
            ``True`` if the list is empty, ``False`` otherwise.

        """
        return True if self.head is None else False

    def reverse(self):
        """Reverse the list."""
        # Empty list.
        if self.isEmpty():
            return

        next = None
        cur = self.head

        # Iterate over list.
        while cur is not None:
            next = cur.next
            cur.next = cur.prev
            cur.prev = next
            cur = next

        # Reset head and tail.
        tmp = self.head
        self.head = self.tail
        self.tail = tmp

        return

    def index(self, record):
        """Find the index of the matching ``record`` in the list.

        Returns
        -------
        int
            The zero-based index of the node matching ``record`` in
            the list.  Returns -1 if ``record`` is not found.

        """
        # Traverse the list.
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
        """Find the head the list.

        Returns
        -------
        DoublyLinkedNode
            The head of the list.

        """
        return self.head

    def find_tail(self):
        """Find the tail the list.

        Returns
        -------
        DoublyLinkedNode
            The tail of the list.

        """
        return self.tail

    def insert_before(self, new, record=None):
        """Insert a node into the list.

        Insert a new node with record ``new`` into the list before the
        node with record ``record``.  If no record is given, then
        prepend the new node onto the list.  If no record is found,
        then append the new node onto the list.

        """
        # Build the node.
        node = DoublyLinkedNode(new)

        # Empty list.
        if self.isEmpty():
            self.append(new)

            return

        # Prepend on no record.
        if record is None:
            node.prev = None
            self.head.prev = node
            node.next = self.head
            self.head = node

            return

        # Traverse the list.
        cur = self.head

        while cur is not None:
            if cur.record == record:
                # Prepend the node.
                if cur == self.head:
                    node.prev = None
                    self.head.prev = node
                    node.next = self.head
                    self.head = node
                else:
                    node.prev = cur.prev
                    node.next = cur
                    cur.prev.next = node
                    cur.prev = node

                return

            cur = cur.next

        # Append if no match.
        self.append(new)

        return

    def insert_after(self, new, record=None):
        """Insert a node in the list.

        Insert a new node with record ``new`` into the list after the
        node with record ``record``.  If no record is given, then
        append the new node onto the list.  If no record is found,
        then append the new node onto the list.

        """
        # Build the node.
        node = DoublyLinkedNode(new)

        # Empty list.
        if self.isEmpty():
            self.append(new)

            return

        # Traverse the list.
        cur = self.head

        while cur is not None:
            if cur.record == record:
                # Append the node.
                if cur == self.tail:
                    self.append(new)
                else:
                    node.prev = cur
                    node.next = cur.next
                    cur.next.prev = node
                    cur.next = node

                return

            cur = cur.next

        # Append if no match.
        self.append(new)

        return

    def append(self, record):
        """Append ``record`` onto the end of the list.

        Parameters
        ----------
        record
            The value to be appended to the list.

        """
        # Build the node.
        node = DoublyLinkedNode(record)

        # Empty list.
        if self.isEmpty():
            self.head = node
            self.tail = node
            self.head.next = None
            self.head.prev = None
            self.tail.next = None
            self.tail.prev = None

            return

        # Non-empty list; append the node and fix the tail.
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

        return

    def delete(self, record):
        """Remove the node matching ``record`` from the list.

        Returns
        -------
        record
            The ``record`` from the removed node or ``None`` if no
            node was removed.  Removes the first node matching
            ``record``.

        """
        # Traverse the list.
        cur = self.head

        while cur is not None:
            if cur.record == record:
                # Delete the node.
                if cur == self.head:
                    self.head = self.head.next
                    self.head.prev = None
                elif cur == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None
                else:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev

                # Return the match.
                return record

            cur = cur.next

        # No match.
        return None

    def pop(self):
        """Remove the tail node from the list.

        Returns
        -------
        record
            The record of the removed node or ``None`` if empty.

        """
        # Empty list.
        if self.isEmpty():
            return None

        # Pop the node and fix the tail.
        node = self.tail

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev

        # Return former tail.
        return node.record
