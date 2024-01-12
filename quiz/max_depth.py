from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def make_tree_by(lst, idx):
    parent = None
    if idx < len(lst):
        value = lst[idx]
        if value is None:    #  '== None' 은 객체의 동등성, 'is None' 은 객체의 정체성
            return

        parent = TreeNode(value)
        parent.left = make_tree_by(lst, 2 * idx + 1)
        parent.right = make_tree_by(lst, 2 * idx + 2)

    return parent

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = deque([root])
        depth = 0

        while q:
            depth += 1
            for _ in range(len(q)):
                cur = q.popleft()
                if cur is not None:
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
        return depth

#  이진트리 최대 깊이


def test_max_depth(lst):
    root = make_tree_by(lst, 0)
    if not root:
        return 0

    q = deque([root])
    depth = 0

    while q:
        depth += 1
        for _ in range(len(q)):
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

    return depth


assert test_max_depth(lst=[]) == 0
assert test_max_depth(lst=[3, 9, 20, None, None, 15, 7]) == 3

def test_invert_btree(lst):
    if not lst:
        return []

    def invert(parent):
        if parent:
            parent.left, parent.right = invert(parent.right), invert(parent.left)
            return parent

    root = make_tree_by(lst, 0)
    return make_lst_by(invert(root))


assert test_invert_btree(lst=[]) == []
assert test_invert_btree(lst=[2]) == [2]
assert test_invert_btree(lst=[2, 1, 3, 5, 6, 2, 3]) == [2, 3, 1, 3, 2, 6, 5]
assert test_invert_btree(lst=[4, 2, 7, 1, 3, 6, 9]) == [4, 7, 2, 9, 6, 3, 1]

def make_lst_by(root):
    if not root:
        return []

    lst = []
    q = deque([root])

    while q:
        node = q.popleft()
        lst.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return lst