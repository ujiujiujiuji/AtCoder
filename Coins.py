A = int(input())
B = int(input())
C = int(input())
X = int(input())
count = 0
max_500 = X // 500  
upper_500 = min(max_500,A)
for i in range(0,upper_500+1):
    rest1 = X - i*500
    max_100 = rest1 // 100
    upper_100 = min(max_100,B)
    for j in range(0,upper_100+1):
        rest2 = rest1 - j*100
        max_50 = rest2 // 50 
        if max_50 <= C:
            count += 1

print(count)

