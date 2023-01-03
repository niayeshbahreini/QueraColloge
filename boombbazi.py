n, m = map(int, input().split())
base = [[0] * (m+2) for i in range(n+2)]
k = int(input())
for i in range(k):
	x, y = map(int, input().split())
	base[x][y] = '*'

def check(x ,y):
    pos = [-1, 0, +1]
    if base[x][y] != '*':
        for i in pos:
            for j in pos:
                if i!=0 or j!=0:
                    if base[x+i][y+j] == '*':
                        base[x][y] += 1


for i in range(1,n+1):
	for j in range(1,m+1):
		check(i,j)
for i in range(1,n+1):
	for j in range(1,m+1):
		print(base[i][j], end=' ')
	print('')