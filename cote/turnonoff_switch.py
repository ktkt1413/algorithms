#  백준코드 1244 스위치 켜고 끄기
#  남자: 자기가 받은 번호의 배수에 해당하는 스위치를 온오프 한다(예외상태-자신만)
#  여자: 자신이 받은 수를 중심으로 가장 긴 펠린드롬을 찾아 스위치 상태를 바꾼다(예외상태- 자신만)
#  온오프 하는 코드는 on 이면 off로 off면 on 으로 바꿈
#  입력으로 스위치 상태가 주어지고, 첫째줄: 스위치 갯수, 둘째줄: 스위치 상태( 켜짐-0, 꺼짐-1),
#  셋째줄 : 학생 수, 넷째줄: 남학생 -1 + 스윗치 갯수 , 다섯째줄: 여학생 -2 + 스위치 갯수
import sys
sys.stdin = open("input.txt", "r")

def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return


input = sys.stdin.readline

N = int(input())
switch = [-1] + list(map(int, input().split()))  # -1 은 리스트 내 인덱스와 스윗치 갯수를 동일하게 맞춰주기 위해서 넣음
students = int(input())


for _ in range(students):
    gender, num = map(int, input().split())
    if gender == 1:
        for i in range(num, N+1, num):
            change(i)
    else:
        change(num)
        for j in range(N//2):    #  스위치를 중심으로 양 쪽으로 똑같이 이동하기 때문에 나누기 2를 하고 나머지를 버림
            if num + j > N or num - j < 1:   #  인덱스 0 은 스위치가 아닌 -1 이라는 숫자가 존재하므로 1 보다 작을 수 없음
                break
            elif switch[num + j] == switch[num - j]:
                change(num + j)
                change(num - j)
            else:
                break
for i in range(1, N+1):
    print(switch[i], end=" ")
    if i % 20 == 0:            #  한 줄에 20개씩 출력
        print()


