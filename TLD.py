S = input()
T = []
for i, char in enumerate(S):
    if char == ".":
        T.append(i)

index = max(T)
S = S[index+1:]
print(S)