import sys
from typing import Generator
import random
import pytest

from bst.bst import BinarySearchTree

# default is ~1000, due to Python not optimising tail recursion
sys.setrecursionlimit(100000)


@pytest.fixture(name="minimum")
def fixture_minimum() -> int:
    return 0


@pytest.fixture(name="maximum")
def fixture_maximum() -> int:
    return 10000


@pytest.fixture(name="range_gen")
def fixture_range_gen(minimum: int, maximum: int) -> range:
    return range(minimum, maximum)


@pytest.fixture(name="keys")
def fixture_keys(range_gen: range) -> Generator[int, None, None]:
    key_list = list(range_gen)
    random.shuffle(key_list)
    return (k for k in key_list)


@pytest.fixture(name="bst")
def fixture_bst(keys: Generator[int, None, None]) -> BinarySearchTree:
    # create a large BST
    tree = BinarySearchTree()
    for key in keys:
        tree.insert(key)
    # print(tree)
    return tree


@pytest.fixture(name="basic_bst")
def fixture_basic_bst() -> BinarySearchTree:
    # create a basic BST for insertion / deletion testing
    tree = BinarySearchTree()
    # 5 cases to test (see if-then-else clauses)
    keys = [3, 1, 7, 4, -2]
    for key in keys:
        tree.insert(key)
    # print(tree)
    return tree


def test_to_list(bst: BinarySearchTree) -> None:
    assert str(bst.to_list()) == str(bst)


def test_is_empty(bst: BinarySearchTree) -> None:
    assert not bst.is_empty()
    # test empty tree
    assert BinarySearchTree().is_empty()


def test_insert(basic_bst: BinarySearchTree) -> None:
    assert basic_bst.key and basic_bst.key == 3
    assert basic_bst.left and basic_bst.left.key == 1
    assert basic_bst.right and basic_bst.right.key == 7
    assert basic_bst.right and basic_bst.right.left and basic_bst.right.left.key == 4
    assert basic_bst.left and basic_bst.left.left and basic_bst.left.left.key == -2
    # test tree depth
    assert basic_bst.depth() == 3


def test_search(bst: BinarySearchTree, range_gen: range, minimum: int, maximum: int) -> None:
    for i in range_gen:
        node = bst.search(i)
        assert node and node.key == i
    # edge cases
    assert not bst.search(minimum - 1)
    assert not bst.search(maximum)


def test_predecessor(bst: BinarySearchTree, range_gen: range, minimum: int, maximum: int) -> None:
    for i in range_gen:
        if i > minimum:
            node = bst.predecessor(i)
            assert node and node.key == i - 1
        else:
            # edge case: smallest element does not have predecessor
            assert not bst.predecessor(i)
    # edge case
    node = bst.predecessor(maximum)
    assert node and node.key == maximum - 1


def test_successor(bst: BinarySearchTree, range_gen: range, minimum: int, maximum: int) -> None:
    for i in range_gen:
        if i < maximum - 1:
            node = bst.successor(i)
            assert node and node.key == i + 1
        else:
            # edge case: largest element does not have successor
            assert not bst.successor(i)
    # edge case
    node = bst.successor(minimum - 1)
    assert node and node.key == minimum


def test_minimum(bst: BinarySearchTree, minimum: int) -> None:
    actual_minimum = bst.minimum()
    assert actual_minimum and actual_minimum.key == minimum
    # test empty tree
    assert not BinarySearchTree().minimum()


def test_maximum(bst: BinarySearchTree, maximum: int) -> None:
    actual_maximum = bst.maximum()
    assert actual_maximum and actual_maximum.key == maximum - 1
    # test empty tree
    assert not BinarySearchTree().maximum()


def test_get_sorted_keys(bst: BinarySearchTree, range_gen: range) -> None:
    actual_sorted_keys = bst.get_sorted_keys()
    expected_sorted_keys = list(range_gen)
    assert actual_sorted_keys == expected_sorted_keys
    # test empty tree
    assert BinarySearchTree().get_sorted_keys() == []
