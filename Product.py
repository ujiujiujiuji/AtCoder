str1, str2 = list(map(int, input().split()))
result = str1 * str2
if result % 2 == 1:
    print("Odd")
else:
    print("Even")
