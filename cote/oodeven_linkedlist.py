#  리트코드.328 - 홀짝 연결리스트
#  주어진 링크드 리스트의 짝수번째 인덱스를 뒤로 넘기고 홀수번째 인덱스를 앞으로
#  sol. 1. 헤드가 없을 경우 예외처리
#       2. 짝수번째 인덱스를 홀수번째 인덱스 뒤로(짝수번째만 리스트에 담고, for문이 끝난뒤 그대로 다시 붙임)
#       3. 나누기2를 했을때 0이 나올때와 1이 나올때 리스트를 따로 만듦
#       4. 홀수 리스트를 링크드리스트에 먼저 담고, 짝수 리스트를 링크드리스트에 담는다
#       but 제약조건에 공간복작도가 O(1)이므로 새로운 리스트를 생성, 부착이 불가
#       => 홀수는 홀수끼리 붙이고, 짝수는 짝수끼리 붙임
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None

    odd = odd_head = head
    even = even_head = head.next

    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next
        #  odd는 현재 가리키는 노드 -> 현재 가리키는 노드는 'odd.next.next' 이므로
        #  변경사항을 업데이트 해줌

    odd.next = even_head

    return odd_head

