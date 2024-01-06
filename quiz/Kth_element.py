import heapq

from lecture.heap_binarytree import BinaryMaxHeap

def test_maxheap_we_made(lst, k):
    maxheap = BinaryMaxHeap()

    # for문 중요, 힙 정렬 시간복잡도 계산의 토대임
    for elem in lst:     # elem 은 리스트 lst의 각 원소를 나타냄
        maxheap.insert(elem)

        return [maxheap.extract() for _ in range(k)][k-1]
              #  ------------리스트------------------/ 인덱스

def test_maxheap_heapq(lst, k):
    return heapq.nlargest(k, lst)[-1]


assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 1) == 6
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 2) == 5
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 3) == 5
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 5) == 3
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 6) == 3
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 7) == 2
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 8) == 2
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 9) == 1


assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 1) == 6
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 2) == 5
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 3) == 5
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 5) == 3
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 6) == 3
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 7) == 2
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 8) == 2
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 9) == 1