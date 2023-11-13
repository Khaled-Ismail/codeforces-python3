inp = list(input())
inp_dict = {}
count = 0
for i in range (0, len(inp)):
    inp_dict[inp[i]] = 0
for i in range (0, len(inp)):
    inp_dict[inp[i]] += 1
for x in inp_dict.values():
    count += 1
if count % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

