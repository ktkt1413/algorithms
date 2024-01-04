# 백준 괄호 문제

T = int(input())  # 입력받은 값은 string 이므로 int 형으로 변환 해줌
                  #
for i in range(T):
    stack = []
    str = input()  # "(" , ")" string 형태 그대로 사용함
    isVPS = True

    for s in str:
        if s == "(":
            stack.append(s)
        if s == ")":
            if stack:
                stack.pop()
            elif not stack:
                isVPS = False   # ")" <- 이건 있는데 stack에 "(" <- 이게 없을때 false
                break
    if not stack and isVPS:    # stack에 아무것도 없고, ")" <- 이것도 남아 있지 않을때
        print("YES")
    elif stack or not isVPS:   # stack에 "(" 이 남아 있거나, ")" <- 이게 남아 있을때
        print("NO")

