import sys
input = sys.stdin.readline
n = int(input())
data = []
for i in range(n):
    data.append(int(input()))
data=sorted(data)
for i in data:
    print(i)