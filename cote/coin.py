#  백준 문제 11047번
# 문제: 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다.
# 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
# 첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.
# Ai 는 Ai-1의 배수이다 -> 이 조건이 있었기 때문에 아래의 식으로 풀수있었음

# 예제 입력
# 10 4200
# 1                                예제 출력
# 5                                6
# 10
# 50                     ->
# 100
# 500
# 1000
# 5000
# 10000
# 50000

# import sys
# sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline

n, k = map(int, input().split)
coins = [int(input()) for _ in range(n)]
ans = 0
for i in range(n-1, -1, -1):  #  n - 1에서 시작헤서 0 까지 1씩 감소하는 반복문
    ans += k // coins[i]  #  현재 동전으로 거슬러 줄 수 있는 최대 개수
    k %= coins[i]         #  현재 동전으로 최대한 거슬러 주고 남은 금액을 K에 업데이트
print(ans)
