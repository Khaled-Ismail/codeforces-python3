inp = input().split()
for i in range(len(inp)):
    inp[i] = int (inp[i])

ban_cost = inp[0]
budget = inp[1]
wanted_ban = inp[2]

total_cost = 0
borrow = 0

for i in range(0, wanted_ban):
    total_cost += ban_cost * (i+1)

if total_cost > budget:
    borrow = total_cost - budget

print(borrow)

