num = int(input())
num_list = list(map(int,input().split()))
count = 0

while all(x % 2 == 0 for x in num_list):
    num_list =[a // 2 for a in num_list]
    count += 1

print(count)