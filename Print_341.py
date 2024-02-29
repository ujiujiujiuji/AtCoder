N = int(input())
num_list = []
for i in range(N+N+1):
    if i%2 == 0:
        num_list.append(str(1))
    else:
        num_list.append(str(0))

print("".join(num_list))
