N = int(input())
inputs = []
daburi_count = 0
for _ in range(N):
    num = int(input())
    inputs.append(num)

new_list = list(set(inputs))

print(len(new_list))