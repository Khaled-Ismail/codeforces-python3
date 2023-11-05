inp=int(input())
res=0

for i in range (0, inp):
    stat=list(input())
    if (stat[0] == "+") or (stat[len(stat)-1] == "+"):
        res+=1
    elif (stat[0] == "-") or (stat[len(stat)-1] == "-"):
        res-=1
print(res)
