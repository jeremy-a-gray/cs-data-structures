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

    def __init__(self):
        """Initialize a ``Queue``."""
        pass

    def __repr__(self):
        """Reproduce a ``Queue``."""
        pass

    def __str__(self):
        """Stringify a ``Queue``."""
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
