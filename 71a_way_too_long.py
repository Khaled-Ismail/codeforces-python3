count=int(input())
arr=[]
for i in range(0, count):
    word=input()
    if len(word) >10:
        word=word[0]+str(len(word)-2)+word[len(word)-1]
    arr.append(word)
for i in range (0, len(arr)):
    print(arr[i])
