N, Y = list(map(int, input().split()))

def cal(N,Y):
    max_10000 = Y // 10000

    for i in range(max_10000+1):
        rest1 = Y - i*10000
        max_5000 = rest1 // 5000
        for j in range(max_5000+1):
            rest2 = rest1 - j*5000
            if rest2 % 1000 == 0 and i+j+(rest2//1000) == N:
                return i,j,(rest2//1000)


result = cal(N,Y)
if result is not None:
    a,b,c = result
    print(a,b,c)
else:
    print(-1,-1,-1)