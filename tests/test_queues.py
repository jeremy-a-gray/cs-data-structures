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

"""Queue tests."""

from ds import Queue


def test_should_stringify_empty_queue():
    """Should stringify an empty queue."""
    a = Queue()

    assert str(a) == "[]"


def test_should_stringify_one_item_queue():
    """Should stringify a one item queue."""
    a = Queue("one")

    assert str(a) == "['one']"


def test_should_stringify_many_item_queue():
    """Should stringify a many item queue."""
    a = Queue("one", "two", "three")

    assert str(a) == "['one', 'two', 'three']"


def test_should_reproduce_empty_queue():
    """Should reproduce an empty queue."""
    a = Queue()

    assert repr(a) == "Queue()"


def test_should_reproduce_one_item_queue():
    """Should reproduce a one item queue."""
    a = Queue("one")

    assert repr(a) == "Queue('one')"


def test_should_reproduce_many_item_queue():
    """Should reproduce a many item queue."""
    a = Queue("one", "two", "three")

    assert repr(a) == "Queue('one', 'two', 'three')"


def test_should_find_len_of_empty_queue():
    """Should find the length of an empty queue."""
    a = Queue()

    assert len(a) == 0


def test_should_find_len_of_nonempty_queue():
    """Should find the length of a non-empty queue."""
    a = Queue("one", "two", "three")

    assert len(a) == 3


def test_should_say_empty_is_empty():
    """Should say an empty queue is empty."""
    a = Queue()

    assert a.isEmpty() is True


def test_should_say_nonempty_is_nonempty():
    """Should say a non-empty queue is non-empty."""
    a = Queue("one", "two", "three")

    assert a.isEmpty() is False


def test_should_dequeue_empty():
    """Should dequeue an empty queue."""
    a = Queue()

    assert a.dequeue() is None


def test_should_dequeue_nonempty_len_one():
    """Should dequeue a non-empty, length one queue."""
    a = Queue("one")

    head = a.dequeue()
    assert head == "one"
    assert len(a) == 0
    assert a.head is None
    assert a.tail is None


def test_should_dequeue_nonempty_len_two():
    """Should dequeue a non-empty, length two queue."""
    a = Queue("one", "two")

    head = a.dequeue()
    assert head == "one"
    assert len(a) == 1
    assert a.head.record == "two"
    assert a.head.prev is None
    assert a.head.next is None
    assert a.tail.record == "two"
    assert a.tail.prev is None
    assert a.tail.next is None


def test_should_dequeue_nonempty_len_three():
    """Should dequeue a non-empty, length three queue."""
    a = Queue("one", "two", "three")

    head = a.dequeue()
    assert head == "one"
    assert len(a) == 2
    assert a.head.record == "two"
    assert a.head.prev is None
    assert a.head.next.record == "three"
    assert a.head.next.next is None


def test_should_repeatedly_dequeue():
    """Should repeatedly dequeue a queue."""
    a = Queue("one", "two", "three")

    head = a.dequeue()
    assert head == "one"
    assert len(a) == 2
    assert a.head.record == "two"
    assert a.head.prev is None
    assert a.head.next.record == "three"
    assert a.head.next.next is None

    head = a.dequeue()
    assert head == "two"
    assert len(a) == 1
    assert a.head.record == "three"
    assert a.head.prev is None
    assert a.head.next is None
    assert a.tail.record == "three"
    assert a.tail.prev is None
    assert a.tail.next is None

    head = a.dequeue()
    assert head == "three"
    assert len(a) == 0
    assert a.head is None
    assert a.tail is None

    head = a.dequeue()
    assert head is None
    assert len(a) == 0
    assert a.head is None
    assert a.tail is None


def test_should_enqueue_empty():
    """Should enqueue onto an empty queue."""
    a = Queue()

    a.enqueue("one")

    assert len(a) == 1
    assert a.head.record == "one"
    assert a.head.prev is None
    assert a.head.next is None
    assert a.tail.record == "one"
    assert a.tail.prev is None
    assert a.tail.next is None


def test_should_enqueue_nonempty():
    """Should enqueue onto a non-empty queue."""
    a = Queue("one")

    a.enqueue("two")

    assert len(a) == 2
    assert a.head.record == "one"
    assert a.head.prev is None
    assert a.head.next.record == "two"
    assert a.tail.record == "two"
    assert a.tail.prev.record == "one"
    assert a.tail.next is None
