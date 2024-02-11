N = int(input())

cost = 0
kokuban = []
kokuban.append(N)
while len(kokuban) > 0:
    kokuban = [x for x in kokuban if x != 1]
    if len(kokuban) == 0:
        break
    first = kokuban[0]
    if first % 2 == 1:
        a = first // 2
        b = (first // 2) + 1
    else:
        a = first // 2
        b = first // 2
    kokuban.append(a)
    kokuban.append(b)
    cost += first
    kokuban.remove(first)

print(cost)