#  백준 2493번 탑
n = int(input())
tower = list(map(int, input().split()))
ans = [0]*n
#  타워의 최대 높이 : 10 ** 8
#  stack의 값들은 (탑의 높이, 탑의 위치)로 해주자
#  stack을 사용하여 먼저 들어 온 값을 조회하는 것이 유리하다

stack = [(10 ** 8 + 1, 0)]  # -> 탑이 최대한 높을수 있는 크기 +1 보다 큰 크기의 탑이 올 수 없음
for i in range(n):
    h = tower[i]
    #  현재 위치 보다 왼쪽에 있는 탑 중 더 낮은 탑은 확인할 필요가 X
    while stack[-1][0] < h:  # stack[-1][0]에서 stack(3,20) 이라면
        stack.pop()          # [0] = 3, [-1] = 20 이다
    #  while 문 탐색이 끝났다 = stack 마지막 값이 우리가 찾는 탑의(높이, 위치)
    #  stack이 비어있지 않는 이유 : 초기값 설정
    ans[i] = stack[-1][1]
    stack.append((h, i + 1))

print(*ans)