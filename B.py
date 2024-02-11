Q = int(input())
query_list = []
A = []
Answer = []
for _ in range(Q):
    query_list.append(list(map(int,input().split())))

for i in range(Q):
    if query_list[i][0] == 1:
        A.append(query_list[i][1])
    else:
        length = len(A)
        Answer.append(A[length - query_list[i][1]])

str_list = list(map(str,Answer))

for num in str_list:
    print(num)
    


