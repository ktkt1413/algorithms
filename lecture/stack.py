class Node:
    def __init__(self, item, next):
        self.item = item  # 현재 노드가 저장하는 데이터
        self.next = next  # 다음 노드를 가리키는 링크 , prev(previous) 는 이전 노드를 가리키는 링크이다

class Stack:
     def __init__(self):
         self.top = None     # self.top에 None 값을 할당한다

     def push(self, val):
         self.top = Node(val, self.top)  # self top에 값을 넣어라

     def pop(self):
         if not self.top:  # 만약 top가 비어있다면
             return None

         node = self.top  # 노드는 현재 top값을 지정한다
         self.top = self.top.next  # 현재 top값을 다음 순서 값(2번째 값)으로 지정한다

         return node.item   # 현재 top값을 출력하고, 2번째 값이 1번째 top값으로 온다

     def is_empty(self):
         return self.top is None  # self.top값이 None 값인지 유무에 따라 T/F 로 값을 할당한다



