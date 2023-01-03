from re import I
from unicodedata import name


n = int(input())
names= list()

def checknames(x):
    t = ''
    for i in x : 
        if i not in t:
            t += i
    return len(t)

for _ in range(n):
    a = input()
    names.append(checknames(a))

print(max(names))