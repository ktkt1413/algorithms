import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

carNum = int(input())
inCar = {}
OutCar = []
count = 0

for i in range(carNum):
    car = input().strip()
    inCar[car] = i
for j in range(carNum):
    OutCar.append(input().strip())

for i in range(carNum - 1):
    for j in range(i + 1, carNum):
        if inCar[OutCar[i]] > inCar[OutCar[j]]:
            count += 1
            break

print(count)