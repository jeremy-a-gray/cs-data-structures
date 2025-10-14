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

from ds import Node


def test_should_stringify_node():
    """Should stringify a ``Node``."""
    assert str(Node("one")) == "one"


def test_should_reproduce_node():
    """Should reproduce a ``Node``."""
    assert repr(Node("one")) == "Node('one')"


def test_should_contain_record():
    """Should contain a record."""
    a = Node("one")

    assert hasattr(a, "record")
    assert a.record == "one"


def test_should_contain_next():
    """Should contain a next reference."""
    a = Node("one")

    assert hasattr(a, "next")
    assert a.next is None
