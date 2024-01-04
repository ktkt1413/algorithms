class Node:
    def __init__(self, val, next=None):    # next=None을 하지 않으면 next에 반드시 매개변수를 지정해줘야함
        self.val = val
        self.next = next

class Queues:
    def __init__(self):
        self.front = None  # 일반적으로 front는 큐에서 사용하는 용어이고, top는 스택에서 사용한는 용어이다

    def push(self, val):
        if not self.front:
            self.front = Node(val, None)
            return

        node = self.front  #가장 앞쪽 노드를 찾아 감
        while node.next:   #node.next가 있다면 while문이 돌아감
            node = node.next
        node.next = Node(val, None)   # 큐의 처음에서 node.next가 없는 끝까지 가서 새로운 노드를 생성후 큐에 붙여준다

    def pop(self):
        if not self.front:
            return None

        node = self.front   # 첫번째 노드를 꺼내서 ~~
        self.front = self.front.next  # self.front에 할당된 기존 노드 값 대신 바로 다음 값을 할당해줌
        return node.val        # ~~ 여기에서 반환

    def is_empty(self):
        return self.front is None  # is None 은 None 값의 유무를 확인 후 true or false 값을 반환함
