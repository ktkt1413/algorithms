import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
while True:
    pair = {
        ')' : '(',
        ']' : '['
    }
    opener = "(["
    closer = ")]"
    temp = []

    s = input()

    if s == '.':
        break

    for char in s:
        if char in opener:
            temp.append(char)
        elif char in closer and (not temp or pair[char] != temp.pop()):
            print("no")
            sys.exit()

    if len(temp) == 0:
        print("yes")
    else:
        print("no")