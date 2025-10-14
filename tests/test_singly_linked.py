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

"""Singly-linked list tests."""

from ds import List


def test_should_stringify_empty_list():
    """Should stringify an empty list."""
    a = List()

    assert str(a) == "[]"


def test_should_stringify_one_item_list():
    """Should stringify a one item list."""
    a = List("one")

    assert str(a) == "['one']"


def test_should_stringify_many_item_list():
    """Should stringify a many item list."""
    a = List("one", "two", "three")

    assert str(a) == "['one', 'two', 'three']"


def test_should_reproduce_empty_list():
    """Should reproduce an empty list."""
    a = List()

    assert repr(a) == "List()"


def test_should_reproduce_one_item_list():
    """Should reproduce a one item list."""
    a = List("one")

    assert repr(a) == "List('one')"


def test_should_reproduce_many_item_list():
    """Should reproduce a many item list."""
    a = List("one", "two", "three")

    assert repr(a) == "List('one', 'two', 'three')"


def test_should_find_head_of_empty_list():
    """Should find the head of an empty list."""
    a = List()

    assert a.find_head() is None


def test_should_find_head_of_nonempty_list():
    """Should find the head of a non-empty list."""
    a = List("one", "two", "three")

    assert a.find_head().record == "one"
    assert a.find_head().next.record == "two"
    assert a.find_head().next.next.record == "three"


def test_should_find_tail_of_empty_list():
    """Should find the tail of an empty list."""
    a = List()

    assert a.find_tail() is None


def test_should_find_tail_of_nonempty_list():
    """Should find the tail of a non-empty list."""
    a = List("one", "two", "three")

    assert a.find_tail().record == "three"
    assert a.find_tail().next is None


def test_should_find_len_of_empty_list():
    """Should find the length of an empty list."""
    a = List()

    assert len(a) == 0


def test_should_find_len_of_nonempty_list():
    """Should find the length of a non-empty list."""
    a = List("one", "two", "three")

    assert len(a) == 3


def test_should_append_empty():
    """Should append to an empty list."""
    record = "one"

    a = List()

    a.append(record)

    assert a.head.record == record


def test_should_append_non_empty():
    """Should append to a non-empty list."""
    a = List("one", "two")

    a.append("three")

    assert a.head.record == "one"
    assert a.head.next.record == "two"
    assert a.head.next.next.record == "three"
    assert a.head.next.next.next is None


def test_should_implement_iter_empty():
    """Should implement iterator protocol for an empty list."""
    a = List()

    assert [item.record for item in a] == []


def test_should_implement_iter_nonempty():
    """Should implement iterator protocol for a non-empty list."""
    a = List("one", "two", "three")

    assert [item.record for item in a] == ["one", "two", "three"]


def test_should_index_empty():
    """Should index an empty list."""
    a = List()

    assert a.index("one") == -1


def test_should_index_nonempty_match():
    """Should index a non-empty list with a match."""
    a = List("one", "two", "three")

    assert a.index("one") == 0
    assert a.index("two") == 1
    assert a.index("three") == 2


def test_should_index_nonempty_no_match():
    """Should index a non-empty list without a match."""
    a = List("one", "two", "three")

    assert a.index("four") == -1


def test_should_pop_empty():
    """Should pop an empty list."""
    a = List()

    assert a.pop() is None


def test_should_pop_nonempty():
    """Should pop a non-empty list."""
    a = List("one", "two", "three")

    tail = a.pop()
    assert tail == "three"
    assert len(a) == 2


def test_should_delete_empty():
    """Should delete an empty list."""
    a = List()

    assert a.delete("one") is None


def test_should_delete_nonempty_match_head():
    """Should delete a non-empty list with a head match."""
    a = List("one", "two", "three")

    record = a.delete("one")
    assert record == "one"
    assert len(a) == 2
    assert a.head.record == "two"
    assert a.head.next.record == "three"
    assert a.head.next.next is None


def test_should_delete_nonempty_match_middle():
    """Should delete a non-empty list with a middle match."""
    a = List("one", "two", "three")

    record = a.delete("two")
    assert record == "two"
    assert len(a) == 2
    assert a.head.record == "one"
    assert a.head.next.record == "three"
    assert a.head.next.next is None


def test_should_delete_nonempty_match_tail():
    """Should delete a non-empty list with a tail match."""
    a = List("one", "two", "three")

    record = a.delete("three")
    assert record == "three"
    assert len(a) == 2
    assert a.head.record == "one"
    assert a.head.next.record == "two"
    assert a.head.next.next is None


def test_should_delete_nonempty_no_match():
    """Should delete a non-empty list without a match."""
    a = List("one", "two", "three")

    assert a.delete("four") is None
    assert len(a) == 3
    assert a.head.record == "one"
    assert a.head.next.record == "two"
    assert a.head.next.next.record == "three"


def test_should_insert_after_empty():
    """Should insert after with an empty list."""
    a = List()
    a.insert_after("one", "zero")

    assert len(a) == 1
    assert a.head.record == "one"
    assert a.head.next is None


def test_should_insert_after_nonempty_match_head():
    """Should insert after on a non-empty list with a head match."""
    a = List("one", "two", "three")

    a.insert_after("zero", "one")

    assert len(a) == 4
    assert a.head.record == "one"
    assert a.head.next.record == "zero"
    assert a.head.next.next.record == "two"
    assert a.head.next.next.next.record == "three"
    assert a.head.next.next.next.next is None


def test_should_insert_after_nonempty_match_middle():
    """Should insert after on a non-empty list with a middle match."""
    a = List("one", "two", "three")

    a.insert_after("zero", "two")

    assert len(a) == 4
    assert a.head.record == "one"
    assert a.head.next.record == "two"
    assert a.head.next.next.record == "zero"
    assert a.head.next.next.next.record == "three"
    assert a.head.next.next.next.next is None


def test_should_insert_after_nonempty_match_tail():
    """Should insert after on a non-empty list with a tail match."""
    a = List("one", "two", "three")

    a.insert_after("zero", "three")

    assert len(a) == 4
    assert a.head.record == "one"
    assert a.head.next.record == "two"
    assert a.head.next.next.record == "three"
    assert a.head.next.next.next.record == "zero"
    assert a.head.next.next.next.next is None


def test_should_insert_after_nonempty_no_match():
    """Should insert after on a non-empty list without a match."""
    a = List("one", "two", "three")

    a.insert_after("zero", "four")

    assert len(a) == 4
    assert a.head.record == "one"
    assert a.head.next.record == "two"
    assert a.head.next.next.record == "three"
    assert a.head.next.next.next.record == "zero"
    assert a.head.next.next.next.next is None


def test_should_insert_before_empty():
    """Should insert before with an empty list."""
    a = List()
    a.insert_before("one", "zero")

    assert len(a) == 1
    assert a.head.record == "one"
    assert a.head.next is None


def test_should_insert_before_nonempty_match_head():
    """Should insert before on a non-empty list with a head match."""
    a = List("one", "two", "three")

    a.insert_before("zero", "one")

    assert len(a) == 4
    assert a.head.record == "zero"
    assert a.head.next.record == "one"
    assert a.head.next.next.record == "two"
    assert a.head.next.next.next.record == "three"
    assert a.head.next.next.next.next is None


def test_should_insert_before_nonempty_match_middle():
    """Should insert before on a non-empty list with a middle match."""
    a = List("one", "two", "three")

    a.insert_before("zero", "two")

    assert len(a) == 4
    assert a.head.record == "one"
    assert a.head.next.record == "zero"
    assert a.head.next.next.record == "two"
    assert a.head.next.next.next.record == "three"
    assert a.head.next.next.next.next is None


def test_should_insert_before_nonempty_match_tail():
    """Should insert before on a non-empty list with a tail match."""
    a = List("one", "two", "three")

    a.insert_before("zero", "three")

    assert len(a) == 4
    assert a.head.record == "one"
    assert a.head.next.record == "two"
    assert a.head.next.next.record == "zero"
    assert a.head.next.next.next.record == "three"
    assert a.head.next.next.next.next is None


def test_should_insert_before_nonempty_no_match():
    """Should insert before on a non-empty list without a match."""
    a = List("one", "two", "three")

    a.insert_before("zero", "four")

    assert len(a) == 4
    assert a.head.record == "one"
    assert a.head.next.record == "two"
    assert a.head.next.next.record == "three"
    assert a.head.next.next.next.record == "zero"
    assert a.head.next.next.next.next is None


def test_should_reverse_empty():
    """Should reverse an empty list."""
    a = List()
    a.reverse()

    assert len(a) == 0
    assert a.head is None


def test_should_reverse_one_item():
    """Should reverse a one item list."""
    a = List("one")
    a.reverse()

    assert len(a) == 1
    assert a.head.record == "one"
    assert a.head.next is None
    assert hasattr(a.head, "prev") is False


def test_should_reverse_many_items():
    """Should reverse a many item list."""
    a = List("one", "two", "three")
    a.reverse()

    assert len(a) == 3
    assert a.head.record == "three"
    assert a.head.next.record == "two"
    assert a.head.next.next.record == "one"
    assert a.head.next.next.next is None
    assert hasattr(a.head, "prev") is False
