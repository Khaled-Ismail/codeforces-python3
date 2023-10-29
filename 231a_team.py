problem_count=int(input())
problems=[]
solve_count = 0
for i in range (problem_count):
    problems.append(input())
for i in range (0, problem_count):
    problems[i].split()
    if problems[i].count('1') >= 2:
        solve_count+=1
print(solve_count)
