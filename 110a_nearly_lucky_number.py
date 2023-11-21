inp = list(input())

out = "NO"
flag = False
flag_4_prsnt = False
flag_7_prsnt = False
count_lucky = 0
for i in range(len(inp)):
    if inp[i] == '7':
        flag_7_prsnt = True
        count_lucky += 1
    elif inp[i] == '4':
        flag_4_prsnt = True
        count_lucky += 1
    else:
        flag = True

if count_lucky == 4 or count_lucky == 7:
    if flag_4_prsnt == True or flag_7_prsnt == True:
        out = "YES"

print(out)
