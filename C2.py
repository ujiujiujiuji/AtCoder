from functools import cache
N = int(input())

@cache
def cal(N):
    if N == 1:
        return 0
    elif N == 2:
        return 2
    else:
        if N % 2 == 0:
            a = N // 2
            return N + 2*cal(a)
        else:
            a = N // 2
            b = (N // 2) + 1
            total = N + cal(a) + cal (b)
            return total


print(cal(N))