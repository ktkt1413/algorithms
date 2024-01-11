#  백준 카드 합체 놀이
#  card 오름차순 -> 최소 숫자 2개 끼리 더해서 m번 시행 = 가장 작은 합의 수
#  리스트를 힙 으로 만들어서 루트에 최소 숫자만 꺼내서 조합하면 시간복잡도를 logN으로 만들수 있음


from typing import List
class Solution:
    def cardGame(self, n: int, m: int, cards: List[int] ) -> int:

        # n, m = map(int, input().split())
        # cards = list(map(int, input().split()))

        for i in range(m):
            cards.sort()
            card = cards[0] + cards[1]
            cards[0], cards[1] = card, card

        sumCards = sum(cards)
        print(sumCards)

#  강사님 코드

from heapq import heapify, heappush, heappop

n, m = map(int, input().split())
arr = list(map(int, input().split()))
heapify(arr)
for _ in range(m):
    #  heappop / heappush 는 log n 에 처리가 가능 -> O(m log n)
    #  만일 min 이나 index() 등의 함수를 사용했다면? -> O(mn)
    s = heappop(arr) + heappop(arr)
    heappush(arr, s)
    heappush(arr, s)
print(sum(arr))
