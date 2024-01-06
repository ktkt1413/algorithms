N = input()                                       #  map
A = set(input().split())
M = input()
target = list(input().split())

for num in target:
    print(1 if num in A else 0)
