from typing import Any, Self


class BinarySearchTree:
    # Definition and operations: https://courses.grainger.illinois.edu/cs225/fa2023/resources/bst/
    # Fully recursive implementation using 1 class

    def __init__(self, key: Any | None = None) -> None:
        self._key: Any | None = key
        self._left: Self | None = None
        self._right: Self | None = None

    @property
    def key(self) -> Any | None:
        return self._key

    @property
    def left(self) -> Self | None:
        return self._left

    @property
    def right(self) -> Self | None:
        return self._right

    def __str__(self) -> str:
        # recursive calls
        return f"[{self._left}, {self._key}, {self._right}]"

    def to_list(self) -> list[Any]:
        return [
            self._left.to_list() if self._left else None,
            self._key,
            self._right.to_list() if self._right else None,
        ]

    def depth(self) -> int:
        left_depth = self._left.depth() if self._left else 0
        right_depth = self._right.depth() if self._right else 0
        return max(left_depth, right_depth) + 1

    def is_empty(self) -> bool:
        return self._key is None

    def insert(self, key: Any) -> None:
        if self.is_empty():
            self._key = key
        elif key < self._key:
            if self._left:
                self._left.insert(key)
            else:
                self._left = BinarySearchTree(key)  # type: ignore[assignment]
        else:
            if self._right:
                self._right.insert(key)
            else:
                self._right = BinarySearchTree(key)  # type: ignore[assignment]

    def delete(self, key: Any) -> Self | None:
        pass

    def search(self, key: Any) -> Self | None:
        if self.is_empty():
            return None
        if key == self._key:
            return self
        if key < self._key and self._left:
            return self._left.search(key)
        if self._right:
            return self._right.search(key)
        return None

    def predecessor(self, key: Any) -> Self | None:
        if self.is_empty():
            return None
        if key > self._key:
            potential_predecessor = self._right.predecessor(key) if self._right else None
            return self if not potential_predecessor else potential_predecessor
        if self._left:
            return self._left.predecessor(key)
        return None

    def successor(self, key: Any) -> Self | None:
        if self.is_empty():
            return None
        if key < self._key:
            potential_successor = self._left.successor(key) if self._left else None
            return self if not potential_successor else potential_successor
        if self._right:
            return self._right.successor(key)
        return None

    def maximum(self) -> Self | None:
        if self.is_empty():
            return None
        if self._right:
            return self._right.maximum()
        return self

    def minimum(self) -> Self | None:
        if self.is_empty():
            return None
        if self._left:
            return self._left.minimum()
        return self

    def _successors(self, key: Any) -> list[Any]:
        lst = [key]
        next_node = self.successor(key)
        if next_node:
            lst.extend(self._successors(next_node.key))
        return lst

    def get_sorted_keys(self) -> list[Any]:
        if self.is_empty():
            return []
        minimum = self.minimum()
        return self._successors(minimum.key) if minimum else []
