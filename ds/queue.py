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

from .node import DoublyLinkedNode  # noqa:  F401


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
        pass

    def __iter__(self):
        """Iterate over the ``Queue``.

        Iterate over the queue from head to tail by dequeuing to
        enable iterator protocol.

        """
        pass

    def isEmpty(self):
        """Determine if the ``Queue`` is empty.

        Returns
        -------
        bool
            ``True`` if the ``Queue`` is empty, ``False`` otherwise.

        """
        pass

    def enqueue(self, record):
        """Enqueue a ``record`` onto the tail of a ``Queue``.

        Parameters
        ----------
        record
            The record to be enqueued.

        """
        pass

    def dequeue(self):
        """Dequeue the head of a ``Queue``.

        Returns
        -------
        record
            The record from the head of the queue.

        """
        pass
