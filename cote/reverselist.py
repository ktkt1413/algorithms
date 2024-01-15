# leetcode, reverse list  역방향 연결리스트
#  리스트를 역순으로 넣어줌

from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


example = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
solution = Solution()
reversed_head = solution.reverseList(example)
while reversed_head:
    print(reversed_head.val, end="")
    reversed_head = reversed_head.next