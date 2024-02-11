N = int(input())
num_list = list(map(int,input().split()))

flag = True
initial_people = 0
def hantei(initial_people, num_list):
    for i, num in enumerate(num_list):
        initial_people += num
        if initial_people < 0:
            return False
    return True

def hantei2(initial_people, num_list):
    if (sum(num_list) + initial_people) >= 0:
        for i, num in enumerate(num_list):
            initial_people += num
            if initial_people < 0:
                return False      
        return True
    else:
        return False

while True:
    if hantei2(initial_people, num_list):
        break
    else:
        initial_people += 1

print(initial_people + sum(num_list))



