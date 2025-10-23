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

"""List node tests."""

from ds import DoublyLinkedNode, Node


def test_should_stringify_node():
    """Should stringify a ``Node``."""
    assert str(Node("one")) == "one"


def test_should_reproduce_node():
    """Should reproduce a ``Node``."""
    assert repr(Node("one")) == "Node('one')"


def test_node_should_contain_record():
    """Should contain a record."""
    a = Node("one")

    assert hasattr(a, "record")
    assert a.record == "one"


def test_node_should_contain_next():
    """Should contain a next reference."""
    a = Node("one")

    assert hasattr(a, "next")
    assert a.next is None


def test_should_stringify_doubly_linked_node():
    """Should stringify a ``DoublyLinkedNode``."""
    assert str(DoublyLinkedNode("one")) == "one"


def test_should_reproduce_doubly_linked_node():
    """Should reproduce a ``DoublyLinkedNode``."""
    assert repr(DoublyLinkedNode("one")) == "DoublyLinkedNode('one')"


def test_doubly_linked_node_should_contain_record():
    """Should contain a record."""
    a = DoublyLinkedNode("one")

    assert hasattr(a, "record")
    assert a.record == "one"


def test_doubly_linked_node_should_contain_prev():
    """Should contain a prev reference."""
    a = DoublyLinkedNode("one")

    assert hasattr(a, "prev")
    assert a.prev is None


def test_doubly_linked_node_should_contain_next():
    """Should contain a next reference."""
    a = DoublyLinkedNode("one")

    assert hasattr(a, "next")
    assert a.next is None
