#  백준 1920 수찾기 문제
#  N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
#  입력: 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.
#  출력: M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
# sol. 두번째 줄과 4번째 줄을 읽는다 -> 네번째 줄의 숫자가 두번째 줄에 포함되는지 유무에 따라 1과 0으로 표현
# -> 1과 0 은 각 줄을 달리 한다
# 방법1. set은 중복을 허용하지 않으므로 탐색속도를 높여준다.
# 방법2. 이진탐색을 사용할수있다

N = int(input())
A = set(map(int, input().split()))  # set함수는 중복을 허용하지 않음-> 탐색속도 빨라짐
M = int(input())
target = map(int, input().split())   #  list로 굳이 형변환을 해주지 않아도 됨. 'target'이 여러번
                                     #  사용되거나 수정을 해야할 경우 list()로 형변환을 해주어야 함
for num in target:
    print(1 if num in A else 0)

#  방법2 -> int로 형 변환하지 않고 input()시 받는 str로도 바로 검사가 가능하므로 map을 사용하지 않아도 됨
N = input()                                       #  map
A = set(input().split())
M = input()
target = list(input().split())

for num in target:
    print(1 if num in A else 0)
