N = int(input())
num_list = list(map(int, input().split()))
A_point = 0
B_point = 0
draw_count = 0
while len(num_list) != 0:
    if draw_count % 2 == 0:
        A_point += max(num_list)
        num_list.remove(max(num_list))
        draw_count += 1
    elif draw_count % 2 == 1:
        B_point += max(num_list)
        num_list.remove(max(num_list))
        draw_count += 1

print(A_point - B_point)