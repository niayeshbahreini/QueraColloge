n = int(input())
employees = dict()

for _ in range(n):
    name , lastName = input().split()
    if name in employees:
        employees[name]+=1
    else:
        employees[name] =1
name_counts = employees.values()
print(max(name_counts))