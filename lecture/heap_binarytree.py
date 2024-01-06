# 힙은 완전이진트리로, 우선순위 큐를 구현하는데 주로 사용되며, 최대힙과 최소힙으로 나뉨
# 힙: 최대 힙의 경우 루트에 최대값이 위치하고, 최소 힙의 경우 루트에 최소값이 위치합니다. 혹은 이와 반대
# 힙은 BTS(이진탐색트리)와 다르다: 좌, 우 자식의 위치가 대소관계를 반영하지 않는다
# 이진 힙(Binary Heap)은 완전 이진 트리의 한 종류로서, 최대 힙(Max Heap)과 최소 힙(Min Heap)으로 나뉩니다
# 모든 이진 탐색 트리는 이진트리이지만, 모든 이진트리가 이진탐색트리는 아니다.
# 이진 트리: 최대값 또는 최소값이 특별한 위치에 있는 것이 아니라 트리 전체에 퍼져 있을 수 있습니다. 루트값이 최대 혹은 최소값이 아닐수도 있다.
# 이진탐색트리: 이진 트리의 한 종류로, 좌(작은값), 우(큰값) 대소 관계가 반영됨
# 완전 이진트리는 좌 -> 우 에서 순서대로 노드가 채워지는 것이고, 포화이진트리는 좌->우(순서대로) & 모든 노드가 채워져 있는 상태
# 힙은 우선순위 큐 와 같은 우선순위 기반의 연산을 수행 , 이진트리는 데이터를 표현, 탐색에 주로 사용
# 우선순위 큐는 FIFO(=큐) 와 달리 우선순위에 따라 먼저 나가게 됨.
# 운선순위 큐: '삽입 & 최우선순위 요소 삭제' 가 주요 연산 => 파이썬에서 'heap'모둘이나, 'queue.PriorityQueue'클래스 등을 사용하여 우선순위 큐를 구현할수있음
# 삽입과 추출의 방법은 똑같다
# 삽입시: 일단 힙의 젤 끝에 넣고 부모 위로 한 단계씩 올린다
# 추출할 때는 부모와 맨 끝의 자식의 위치를 바꾸고, 부모를 뺀다
# 루트에 있는 것이 힙의 구조를 만족시킬때 까지 한 단계를 내린다 / 루트- 힙의 최상단 부분
# 최대힙 - 루트가 최대값 / 최소힙 - 루트가 최소값 -> 이 특성을 이용해 우선순위 큐 등의 자료구조를 가짐
# self.items 는 힙에 저장되는 리스트 형태의 데이터이다. ex) self.items = [None, 10, 8, 9, 3, 2, 4]
# 일 때, self.items[1] 이 힙의 루트 노드가 된다.
# [None] 과 [] 는 차이점이 있는데, [None]의 경우 'None'이라는 하나의 요소를 가지고, 1의 길이를 가진다. 반면 []는 비어있는 리스트이고 0의 길이를 가짐
# 게다가 self.items = [None]은 유효한 파이썬 코드가 아니다. 'self.items[0] = None' 은 관습적인 선택이지만 빈 리스트로 시작하는 것도 가능하다

class BinaryMaxHeap:
    def __init__(self):
        # 계산 편의를 위해 0이 아닌 1번째 인덱스부터 사용한다. [None] 으로 시작하면 인덱스가 1부터 시작하지 않는다
        self.items = []

    # def __len__(self):
    #     return len(self.items) - 1  # 우리는 첫번째 요소가 None이므로 -1 을 해야함
    #     # __len__ 에서 '__' 은 len() 연산을 가능하게 하는 매직매서드(=일종의 예약되어 있다)
    #     # 이 메서드 덕분에 len 함수를 사용하면 자동적으로 -1 을 포함하여 계산된다.

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def _percolate_up(self):
        # percolate: 스며들다.
        cur = len(self.items) - 1   # 이렇게 하면 cur은 힙의 가장 끝 노드를 가리키게 됨
        # left 라면 2*cur, right 라면 2*cur + 1 이므로 parent 는 항상 cur // 2
        parent = cur // 2

        while parent > 0:
            if self.items[cur] > self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]

            cur = parent
            parent = cur // 2

    def extract(self):
        if len(self.items) - 1 < 1:
            return None

        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down(1)

        return root

    def _percolate_down(self, cur):
        biggest = cur           #  biggest , left , right는 인덱스를 가리킴
        left = 2 * cur
        right = 2 * cur + 1

        if left <= len(self.items) - 1 and self.items[left] > self.items[biggest]:
            biggest = left

        if right <= len(self.items) - 1 and self.items[right] > self.items[biggest]:
            biggest = right

        if biggest != cur:
            self.items[cur], self.items[biggest] = self.items[biggest], self.items[cur]
            self._percolate_down(biggest)
                      # self._percolate_down(biggest)를 통해 재귀적으로 호출하며 힙 성질을 만족하는 구조
        return cur
