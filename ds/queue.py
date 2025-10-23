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

"""Queues."""

from .node import DoublyLinkedNode


class Queue:
    """Represent a queue."""

    def __init__(self, *args):
        """Initialize the ``Queue``.

        Initialize the ``Queue``.  Enqueue any items in ``args`` to
        the queue in order.

        Parameters
        ----------
        args : list
            Items to enqueue onto the queue.

        """
        self.head = None
        self.tail = None

        for item in args:
            self.enqueue(item)

    def __repr__(self):
        """Reproduce the ``Queue``."""
        return "Queue(" + ", ".join([f"'{item!s}'" for item in self]) + ")"

    def __str__(self):
        """Stringify the ``Queue``."""
        return "[" + ", ".join([f"'{item!s}'" for item in self]) + "]"

    def __len__(self):
        """Find the length of the ``Queue``.

        Returns
        -------
        int
            The length of the queue.

        """
        cur = self.head
        count = 0

        while cur is not None:
            count += 1
            cur = cur.next

        return count

    def __iter__(self):
        """Iterate over the ``Queue``.

        Iterate over the stack from head to tail to enable iterator
        protocol.

        """
        cur = self.head

        while cur is not None:
            yield cur
            cur = cur.next

        return

    def isEmpty(self):
        """Determine if the ``Queue`` is empty.

        Returns
        -------
        bool
            ``True`` if the ``Queue`` is empty, ``False`` otherwise.

        """
        return True if len(self) == 0 else False

    def enqueue(self, record):
        """Enqueue a ``record`` onto the tail of a ``Queue``.

        Parameters
        ----------
        record
            The record to be enqueued.

        """
        # Build the node.
        node = DoublyLinkedNode(record)

        # Push onto the tail.
        node.prev = self.tail
        node.next = None
        self.tail = node

        if self.head is None:
            # List was empty; set head to node.
            self.head = node
        else:
            # List was not empty; fix next of old tail.
            node.prev.next = node

        return

    def dequeue(self):
        """Dequeue the head of a ``Queue``.

        Returns
        -------
        record
            The record from the head of the queue.

        """
        if self.head is None:
            return None

        record = self.head.record

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next

        return record
