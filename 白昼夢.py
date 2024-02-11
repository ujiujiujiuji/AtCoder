S = input()

flag = True


def hantei(S):
    mistake_count = 0
    while flag:
        for word in ["dream","dreamer","erase","eraser"]:
            if len(S) == 0:
                return "YES"
            elif mistake_count == 4:
                return "NO"
            elif S.endswith(word):
                S = S[:-len(word)]
                mistake_count = 0
            else:
                mistake_count += 1

print(hantei(S))
    





