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

"""Doubly-linked list tests."""

from ds import DoublyLinkedList


def test_should_stringify_empty_list():
    """Should stringify an empty list."""
    a = DoublyLinkedList()

    assert str(a) == "[]"


def test_should_stringify_one_item_list():
    """Should stringify a one item list."""
    a = DoublyLinkedList("one")

    assert str(a) == "['one']"


def test_should_stringify_many_item_list():
    """Should stringify a many item list."""
    a = DoublyLinkedList("one", "two", "three")

    assert str(a) == "['one', 'two', 'three']"


def test_should_reproduce_empty_list():
    """Should reproduce an empty list."""
    a = DoublyLinkedList()

    assert repr(a) == "DoublyLinkedList()"


def test_should_reproduce_one_item_list():
    """Should reproduce a one item list."""
    a = DoublyLinkedList("one")

    assert repr(a) == "DoublyLinkedList('one')"


def test_should_reproduce_many_item_list():
    """Should reproduce a many item list."""
    a = DoublyLinkedList("one", "two", "three")

    assert repr(a) == "DoublyLinkedList('one', 'two', 'three')"


def test_should_find_head_of_empty_list():
    """Should find the head of an empty list."""
    a = DoublyLinkedList()

    assert a.find_head() is None


def test_should_find_head_of_nonempty_list():
    """Should find the head of a non-empty list."""
    a = DoublyLinkedList("one", "two", "three")

    assert a.find_head().record == "one"
    assert a.find_head().prev is None
    assert a.find_head().next.record == "two"


def test_should_find_tail_of_empty_list():
    """Should find the tail of an empty list."""
    a = DoublyLinkedList()

    assert a.find_tail() is None


def test_should_find_tail_of_nonempty_list():
    """Should find the tail of a non-empty list."""
    a = DoublyLinkedList("one", "two", "three")

    assert a.find_tail().record == "three"
    assert a.find_tail().next is None
    assert a.find_tail().prev.record == "two"


def test_should_find_len_of_empty_list():
    """Should find the length of an empty list."""
    a = DoublyLinkedList()

    assert len(a) == 0


def test_should_find_len_of_nonempty_list():
    """Should find the length of a non-empty list."""
    a = DoublyLinkedList("one", "two", "three")

    assert len(a) == 3


def test_should_append_empty():
    """Should append to an empty list."""
    record = "one"

    a = DoublyLinkedList()

    a.append(record)

    assert len(a) == 1
    assert a.head.record == record
    assert a.tail.record == record
    assert a.head == a.tail
    assert a.head.prev is None
    assert a.head.next is None
    assert a.tail.prev is None
    assert a.tail.next is None


def test_should_append_non_empty():
    """Should append to a non-empty list."""
    a = DoublyLinkedList("one", "two")

    a.append("three")

    assert len(a) == 3
    assert a.head.record == "one"
    assert a.head.prev is None
    assert a.head.next.record == "two"
    assert a.tail.record == "three"
    assert a.tail.prev.record == "two"
    assert a.tail.next is None


def test_should_implement_iter_empty():
    """Should implement iterator protocol for an empty list."""
    a = DoublyLinkedList()

    assert [item.record for item in a] == []


def test_should_implement_iter_nonempty():
    """Should implement iterator protocol for a non-empty list."""
    a = DoublyLinkedList("one", "two", "three")

    assert [item.record for item in a] == ["one", "two", "three"]


def test_should_index_empty():
    """Should index an empty list."""
    a = DoublyLinkedList()

    assert a.index("one") == -1


def test_should_index_nonempty_match():
    """Should index a non-empty list with a match."""
    a = DoublyLinkedList("one", "two", "three")

    assert a.index("one") == 0
    assert a.index("two") == 1
    assert a.index("three") == 2


def test_should_index_nonempty_no_match():
    """Should index a non-empty list without a match."""
    a = DoublyLinkedList("one", "two", "three")

    assert a.index("four") == -1


def test_should_pop_empty():
    """Should pop an empty list."""
    a = DoublyLinkedList()

    assert a.pop() is None
    assert len(a) == 0
    assert a.head is None
    assert a.tail is None


def test_should_pop_nonempty_len_one():
    """Should pop a non-empty, length one list."""
    a = DoublyLinkedList("one")

    tail = a.pop()
    assert tail == "one"
    assert len(a) == 0
    assert a.head is None
    assert a.tail is None


def test_should_pop_nonempty_len_two():
    """Should pop a non-empty, length two list."""
    a = DoublyLinkedList("one", "two")

    tail = a.pop()
    assert tail == "two"
    assert len(a) == 1
    assert a.head.record == "one"
    assert a.head.prev is None
    assert a.head.next is None
    assert a.tail.record == "one"
    assert a.tail.prev is None
    assert a.tail.next is None
    assert a.head == a.tail


def test_should_pop_nonempty_len_three():
    """Should pop a non-empty, length three list."""
    a = DoublyLinkedList("one", "two", "three")

    tail = a.pop()
    assert tail == "three"
    assert len(a) == 2
    assert a.head.record == "one"
    assert a.head.prev is None
    assert a.head.next == a.tail
    assert a.tail.record == "two"
    assert a.tail.prev == a.head
    assert a.tail.next is None


def test_should_delete_empty():
    """Should delete an empty list."""
    a = DoublyLinkedList()

    assert a.delete("one") is None
    assert len(a) == 0
    assert a.head is None
    assert a.tail is None


def test_should_delete_nonempty_match_head():
    """Should delete a non-empty list with a head match."""
    a = DoublyLinkedList("one", "two", "three")

    record = a.delete("one")
    assert record == "one"
    assert len(a) == 2
    assert a.head.record == "two"
    assert a.head.prev is None
    assert a.head.next == a.tail
    assert a.head == a.tail.prev
    assert a.tail.record == "three"
    assert a.tail.next is None


def test_should_delete_nonempty_match_middle():
    """Should delete a non-empty list with a middle match."""
    a = DoublyLinkedList("one", "two", "three")

    record = a.delete("two")
    assert record == "two"
    assert len(a) == 2
    assert a.head.record == "one"
    assert a.head.prev is None
    assert a.head.next == a.tail
    assert a.head == a.tail.prev
    assert a.tail.record == "three"
    assert a.tail.next is None


def test_should_delete_nonempty_match_tail():
    """Should delete a non-empty list with a tail match."""
    a = DoublyLinkedList("one", "two", "three")

    record = a.delete("three")
    assert record == "three"
    assert len(a) == 2
    assert a.head.record == "one"
    assert a.head.prev is None
    assert a.head.next == a.tail
    assert a.head == a.tail.prev
    assert a.tail.record == "two"
    assert a.tail.next is None


def test_should_delete_nonempty_no_match():
    """Should delete a non-empty list without a match."""
    a = DoublyLinkedList("one", "two", "three")

    assert a.delete("four") is None
    assert len(a) == 3
    assert a.head.prev is None
    assert a.head.record == "one"
    assert a.head.next.record == "two"
    assert a.head.next.next == a.tail
    assert a.tail.prev.prev == a.head
    assert a.tail.record == "three"
    assert a.tail.next is None


def test_should_insert_after_empty():
    """Should insert after with an empty list."""
    a = DoublyLinkedList()
    a.insert_after("one", "zero")

    assert len(a) == 1
    assert a.head.record == "one"
    assert a.head.prev is None
    assert a.head.next is None
    assert a.head == a.tail


def test_should_insert_after_nonempty_match_head():
    """Should insert after on a non-empty list with a head match."""
    a = DoublyLinkedList("one", "two", "three")

    a.insert_after("zero", "one")

    assert len(a) == 4
    assert a.head.record == "one"
    assert a.head.prev is None
    assert a.head.next.record == "zero"
    assert a.head.next.prev == a.head
    assert a.head.next.next.record == "two"
    assert a.head.next.next.prev.prev == a.head
    assert a.head.next.next.next == a.tail
    assert a.head.next.next.next.prev.prev.prev == a.head
    assert a.tail.prev.prev.prev == a.head
    assert a.tail.record == "three"
    assert a.tail.next is None


def test_should_insert_after_nonempty_match_middle():
    """Should insert after on a non-empty list with a middle match."""
    a = DoublyLinkedList("one", "two", "three")

    a.insert_after("zero", "two")

    assert len(a) == 4
    assert a.head.record == "one"
    assert a.head.prev is None
    assert a.head.next.record == "two"
    assert a.head.next.next.record == "zero"
    assert a.head.next.next.next == a.tail
    assert a.tail.prev.prev.prev == a.head
    assert a.tail.record == "three"
    assert a.tail.next is None


def test_should_insert_after_nonempty_match_tail():
    """Should insert after on a non-empty list with a tail match."""
    a = DoublyLinkedList("one", "two", "three")

    a.insert_after("zero", "three")

    assert len(a) == 4
    assert a.head.record == "one"
    assert a.head.prev is None
    assert a.head.next.record == "two"
    assert a.head.next.next.record == "three"
    assert a.head.next.next.next == a.tail
    assert a.tail.prev.prev.prev == a.head
    assert a.tail.record == "zero"
    assert a.tail.next is None


def test_should_insert_after_nonempty_no_match():
    """Should insert after on a non-empty list without a match."""
    a = DoublyLinkedList("one", "two", "three")

    a.insert_after("zero", "four")

    assert len(a) == 4
    assert a.head.record == "one"
    assert a.head.prev is None
    assert a.head.next.record == "two"
    assert a.head.next.next.record == "three"
    assert a.head.next.next.next == a.tail
    assert a.tail.prev.prev.prev == a.head
    assert a.tail.record == "zero"
    assert a.tail.next is None


def test_should_insert_after_none_empty():
    """Should insert after no record with an empty list."""
    a = DoublyLinkedList()
    a.insert_after("one")

    assert len(a) == 1
    assert a.head.record == "one"
    assert a.head.prev is None
    assert a.head.next is None
    assert a.head == a.tail


def test_should_insert_after_none_nonempty():
    """Should insert after no record on a non-empty list."""
    a = DoublyLinkedList("one", "two", "three")

    a.insert_after("zero")

    assert len(a) == 4
    assert a.head.record == "one"
    assert a.head.prev is None
    assert a.head.next.record == "two"
    assert a.head.next.next.record == "three"
    assert a.head.next.next.next == a.tail
    assert a.tail.prev.prev.prev == a.head
    assert a.tail.record == "zero"
    assert a.tail.next is None


def test_should_insert_before_empty():
    """Should insert before with an empty list."""
    a = DoublyLinkedList()
    a.insert_before("one", "zero")

    assert len(a) == 1
    assert a.head.record == "one"
    assert a.head.prev is None
    assert a.head.next is None
    assert a.head == a.tail


def test_should_insert_before_nonempty_match_head():
    """Should insert before on a non-empty list with a head match."""
    a = DoublyLinkedList("one", "two", "three")

    a.insert_before("zero", "one")

    assert len(a) == 4
    assert a.head.record == "zero"
    assert a.head.prev is None
    assert a.head.next.record == "one"
    assert a.head.next.next.record == "two"
    assert a.head.next.next.next == a.tail
    assert a.tail.prev.prev.prev == a.head
    assert a.tail.record == "three"
    assert a.tail.next is None


def test_should_insert_before_nonempty_match_middle():
    """Should insert before on a non-empty list with a middle match."""
    a = DoublyLinkedList("one", "two", "three")

    a.insert_before("zero", "two")

    assert len(a) == 4
    assert a.head.record == "one"
    assert a.head.prev is None
    assert a.head.next.record == "zero"
    assert a.head.next.next.record == "two"
    assert a.head.next.next.next == a.tail
    assert a.tail.prev.prev.prev == a.head
    assert a.tail.record == "three"
    assert a.tail.next is None


def test_should_insert_before_nonempty_match_tail():
    """Should insert before on a non-empty list with a tail match."""
    a = DoublyLinkedList("one", "two", "three")

    a.insert_before("zero", "three")

    assert len(a) == 4
    assert a.head.record == "one"
    assert a.head.prev is None
    assert a.head.next.record == "two"
    assert a.head.next.next.record == "zero"
    assert a.head.next.next.next == a.tail
    assert a.tail.prev.prev.prev == a.head
    assert a.tail.record == "three"
    assert a.tail.next is None


def test_should_insert_before_nonempty_no_match():
    """Should insert before on a non-empty list without a match."""
    a = DoublyLinkedList("one", "two", "three")

    a.insert_before("zero", "four")

    assert len(a) == 4
    assert a.head.record == "one"
    assert a.head.prev is None
    assert a.head.next.record == "two"
    assert a.head.next.next.record == "three"
    assert a.head.next.next.next == a.tail
    assert a.tail.prev.prev.prev == a.head
    assert a.tail.record == "zero"
    assert a.tail.next is None


def test_should_insert_before_none_empty():
    """Should insert before no record with an empty list."""
    a = DoublyLinkedList()
    a.insert_before("one")

    assert len(a) == 1
    assert a.head.record == "one"
    assert a.head.prev is None
    assert a.head.next is None
    assert a.head == a.tail


def test_should_insert_before_none_nonempty():
    """Should insert before no record on a non-empty."""
    a = DoublyLinkedList("one", "two", "three")

    a.insert_before("zero")

    assert len(a) == 4
    assert a.head.record == "zero"
    assert a.head.prev is None
    assert a.head.next.record == "one"
    assert a.head.next.next.record == "two"
    assert a.head.next.next.next == a.tail
    assert a.tail.prev.prev.prev == a.head
    assert a.tail.record == "three"
    assert a.tail.next is None


def test_should_reverse_empty():
    """Should reverse an empty list."""
    a = DoublyLinkedList()
    a.reverse()

    assert len(a) == 0
    assert a.head is None
    assert a.tail is None
    assert a.head == a.tail


def test_should_reverse_one_item():
    """Should reverse a one item list."""
    a = DoublyLinkedList("one")
    a.reverse()

    assert len(a) == 1
    assert a.head.record == "one"
    assert a.head.prev is None
    assert a.head.next is None
    assert a.head == a.tail


def test_should_reverse_many_items():
    """Should reverse a many item list."""
    a = DoublyLinkedList("one", "two", "three")
    a.reverse()

    assert len(a) == 3
    assert a.head.record == "three"
    assert a.head.prev is None
    assert a.head.next.record == "two"
    assert a.head.next.prev.record == "three"
    assert a.tail == a.head.next.next
    assert a.tail.record == "one"
    assert a.tail.prev.record == "two"
    assert a.tail.next is None
