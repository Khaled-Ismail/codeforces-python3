inp = input()
inp = list(input())

count_A = 0
count_D = 0

for i in range(len(inp)):
    if (inp[i] == 'A'):
        count_A += 1
    elif (inp[i] == 'D'):
        count_D += 1

if (count_A > count_D):
    print("Anton")
elif (count_D > count_A):
    print("Danik")
else:
    print("Friendship")
