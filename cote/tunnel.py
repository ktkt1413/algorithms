#  백준 2002 - 터널 , 추월 문제
# sol. input으로 받은 n개를 기준으로 2개의 리스트를 만든다
#      각 요소의 인덱스 순서가 바뀐 것을 확인하고, 이전 보다 인덱스가 작아진 것이 추월차량

from typing import List
class Tunnel:
    def tunnel(self) -> int:
        cars = int(input())
        entrance = {}
        out = []
        count = 0

        for i in range(cars):
            car = input()
            entrance[car] = i

        for j in range(cars):
            car = input()
            out.append(car)

        for i in range(cars - 1):
            for j in range(i+1, cars):
                if entrance[out[i]] > entrance[out[j]]:
                    count += 1
                    break

        print(count)

# 강사님 문제 풀이
n = int(input())

#  memo[차 번호]= 들어갈 때의 순서
memo = {}
for i in range(n):
    x = input()
    memo[x] = i

#memo2[차 번호]= 나갈 때의 순서
memo2 = {}
for i in range(n):
    x = input()
    memo2[x] = i

keys = list(memo.keys())
ans = set()  #  중복 제거

#  들어간 순서와 나간 순서의 대소 관계가 바뀌면 추월이 일어난 것

for k1 in keys:
    for k2 in keys:
        if k1 in memo2 and k2 in memo2:
            if memo[k1] < memo[k2] and memo2[k1] > memo2[k2]:
                ans.add(k2)
print(len(ans))



