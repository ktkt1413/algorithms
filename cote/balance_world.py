#  백준.4949 - 균형잡힌 세상
#  여는 괄호와 닫는 괄호를 딕셔너리로 만든다
#  닫는 괄호가 먼저 나오면 No를 출력, 여는 괄호 닫는 괄호 짝이 안 맞아도 False

class Solution:
    def balanceWorld(self, s: str) -> bool:
        pair = {
            ')' : '(',
            ']' : '['
        }
        opener = "(["
        closer = ")]"
        temp = []

        for char in s:
            if char == '.':
                break
            elif char in opener:
                temp.append(char)
            elif char in closer and pair[char] == temp[-1]:
                temp.pop()

        if len(temp) == 0 :
            print("yes")
        else:
            print("no")



#  강사님 코드
while True:  #  -->  . 이 나올때 까지 while문이 돌꺼임
    line = input()
    if line == '.':
        break
    flag = True
    stack = []
    for c in line:
        if c == "[" or c == "(":
            stack.append(c)
        elif c == "]":
            if not stack or stack.pop() != "[":
                flag = False
                break
            elif c == ")":
                if not stack or stack.pop() != "(":
                    flag = False
                    break
    if stack:
        flag = False
    if flag:
        print("yes")
    else:
        print("no")


