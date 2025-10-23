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

"""Stack tests."""

from ds import Stack


def test_should_stringify_empty_stack():
    """Should stringify an empty stack."""
    a = Stack()

    assert str(a) == "[]"


def test_should_stringify_one_item_stack():
    """Should stringify a one item stack."""
    a = Stack("one")

    assert str(a) == "['one']"


def test_should_stringify_many_item_stack():
    """Should stringify a many item stack."""
    a = Stack("one", "two", "three")

    assert str(a) == "['one', 'two', 'three']"


def test_should_reproduce_empty_stack():
    """Should reproduce an empty stack."""
    a = Stack()

    assert repr(a) == "Stack()"


def test_should_reproduce_one_item_stack():
    """Should reproduce a one item stack."""
    a = Stack("one")

    assert repr(a) == "Stack('one')"


def test_should_reproduce_many_item_stack():
    """Should reproduce a many item stack."""
    a = Stack("one", "two", "three")

    assert repr(a) == "Stack('one', 'two', 'three')"


def test_should_find_len_of_empty_stack():
    """Should find the length of an empty stack."""
    a = Stack()

    assert len(a) == 0


def test_should_find_len_of_nonempty_stack():
    """Should find the length of a non-empty stack."""
    a = Stack("one", "two", "three")

    assert len(a) == 3


def test_should_say_empty_is_empty():
    """Should say an empty stack is empty."""
    a = Stack()

    assert a.isEmpty() is True


def test_should_say_nonempty_is_nonempty():
    """Should say a non-empty stack is non-empty."""
    a = Stack("one", "two", "three")

    assert a.isEmpty() is False


def test_should_pop_empty():
    """Should pop an empty stack."""
    a = Stack()

    assert a.pop() is None


def test_should_pop_nonempty_len_one():
    """Should pop a non-empty, length one stack."""
    a = Stack("one")

    tail = a.pop()
    assert tail == "one"
    assert len(a) == 0
    assert a.head is None
    assert a.tail is None


def test_should_pop_nonempty_len_two():
    """Should pop a non-empty, length two stack."""
    a = Stack("one", "two")

    tail = a.pop()
    assert tail == "two"
    assert len(a) == 1
    assert a.head.record == "one"
    assert a.head.prev is None
    assert a.head.next is None
    assert a.tail.record == "one"
    assert a.tail.prev is None
    assert a.tail.next is None


def test_should_pop_nonempty_len_three():
    """Should pop a non-empty, length three stack."""
    a = Stack("one", "two", "three")

    tail = a.pop()
    assert tail == "three"
    assert len(a) == 2
    assert a.head.record == "one"
    assert a.head.prev is None
    assert a.head.next.record == "two"
    assert a.head.next.next is None


def test_should_repeatedly_pop():
    """Should repeatedly pop a stack."""
    a = Stack("one", "two", "three")

    tail = a.pop()
    assert tail == "three"
    assert len(a) == 2
    assert a.head.record == "one"
    assert a.head.prev is None
    assert a.head.next.record == "two"
    assert a.head.next.next is None

    tail = a.pop()
    assert tail == "two"
    assert len(a) == 1
    assert a.head.record == "one"
    assert a.head.prev is None
    assert a.head.next is None
    assert a.tail.record == "one"
    assert a.tail.prev is None
    assert a.tail.next is None

    tail = a.pop()
    assert tail == "one"
    assert len(a) == 0
    assert a.head is None
    assert a.tail is None


def test_should_push_empty():
    """Should push onto an empty stack."""
    a = Stack()

    a.push("one")

    assert len(a) == 1
    assert a.head.record == "one"
    assert a.head.prev is None
    assert a.head.next is None
    assert a.tail.record == "one"
    assert a.tail.prev is None
    assert a.tail.next is None


def test_should_push_nonempty():
    """Should push onto a non-empty stack."""
    a = Stack("one")

    a.push("two")

    assert len(a) == 2
    assert a.head.record == "one"
    assert a.head.prev is None
    assert a.head.next.record == "two"
    assert a.tail.record == "two"
    assert a.tail.prev.record == "one"
    assert a.tail.next is None
