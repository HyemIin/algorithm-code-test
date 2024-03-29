import sys
import math

input=sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

dp = [0]*(n+1)
dp[1] = 1
for i in range(1,n+1):
    if math.sqrt(i) == int(math.sqrt(i)):
        dp[i] = 1
    else:
        dp[i] = i
        for j in range(1,int(math.sqrt(i))+1):
            if dp[i] > dp[i-j*j]+1:
                dp[i] = dp[i-j*j]+1

print(dp[n])