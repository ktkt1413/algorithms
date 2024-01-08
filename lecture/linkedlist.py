#  연결리스트
#  어레이 = [], 00000 -> 파이썬의 리스트. 접근 쉬움 but  삽입 어려움 -> 데이터 접근이 빈번할 때 0(1)
#  링크드리스트 = 0-0-0-0-0 -> 직접 구현해야함. 접근 어려움 but 삽입 쉬움 -> 삽입,삭제가 빈번할 때 O(1)
# 파이썬에서는 하나의 클래스가 정의된 파일을 모듈이라고 부릅니다. 모듈은 다른 파이썬 파일에서 import 문을 사용하여 가져와 사용할 수 있습니다.
# 이러한 모듈화된 구조를 사용하면 프로젝트가 커지더라도 코드를 조직화하고 관리하기 쉬워집니다. but 여러개의 클래스를 하나의 파일에 정의해도 그 파일 자체가 모둘로 사용될 수 있다.

class Person:
    def __init__(self, name):
        self.name = name

    def sayhello(self, to):
        print(f"hello {to}, I'm {self.name}")


rtan = Person("rtanny")
rtan.sayhello("hanghae")


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val, None)
            return

        node = self.head   #  self.head로 이동. node를 생성하진 않았음
        while node.next:
            node = node.next  #  node.next로 이동

        node.next = ListNode(val, None)  #  생성자 노드 생성

class Palindromes:

    def palindrome(self):
        arr = []

        if not self.head:
            return True

        node = self.head
        while node:
            arr.append(node.val)
            node = node.next

        while len(arr) > 1:
            if arr.pop(0) != arr.pop():
                return False

        return True