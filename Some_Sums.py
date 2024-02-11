N, A, B = list(map(int,input().split()))

count = 0

for i in range(1,N+1):
    str1 = str(i)
    length = len(str1)
    total = 0
    for j in range(length):
        total += int(str1[j])
    if A <= total <= B:
        count += i

print(count)