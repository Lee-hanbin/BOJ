# BOJ_1946_silver1-ė ėėŽė

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    lst = [0] * n
    for i in range(n):
        lst[i] = list(map(int, input().split()))
    lst.sort()
    cnt = 1
    chk = lst[0][1]

    for k in range(1, n):
        if chk > lst[k][1]:
            cnt += 1
            chk = lst[k][1]

    print(cnt)