#  리트코드21. 두 정렬리스트의 병합
#  두개의 정렬된 리스트를 오름차순으로 합병하여라
#  두개의 리스트는 오름차순으로 정렬되어져 있다
#  두개의 집합의 요소를 비교하여 작은 요소가 앞으로 옴

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1 : ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return None