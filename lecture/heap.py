# 최대 힙 삽입
# 삽입과 추출의 방법은 똑같다
# 삽입시: 일단 힙의 젤 끝에 넣고 부모 위로 한 단계씩 올린다
# 추출할때는 부모와 맨 끝의 자식의 위치를 바꾸고, 부모를 뺀다
# 루트에 있는 것이 힙의 구조를 만족시킬때 까지 한 단계를 내린다 / 루트- 힙의 최상단 부분
# 최대힙 - 루트가 최대값 / 최소힙 - 루트가 최소값 -> 이 특성을 이용해 우선순위 큐 등의 자료구조를 가짐
#

def _percolate_up(self):
    cur = len(self)

    parent = cur //2

    while parent > 0:
        if self.itens[cur] > self.items[parent]:
            self.items[cur], self.items[parent]= self.items[parent], self.items[cur]

            cur = parent
            parent = cur //2     # 여기서 cur 과 parent 는 인덱스 값이다


def _percolate_down(self, cur):

def insert(self, k):


def extract(self):
    if len(self) < 1:
        return None

    root = self.items[1]
    self.items[1] = self.items[-1]  # 루트와 힙의 마지막 값을 바꿈
    self.items.pop()   # 힙의 마지막 값을 빼냄(원래 루트값)
    self._percorate_down(1)

    return root
