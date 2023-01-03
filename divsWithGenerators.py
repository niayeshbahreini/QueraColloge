
def divs(n):
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            yield i
    yield n
number = divs(4)
print(list(number))

print('''''or you can write: ''''')

def divs(n):
    for i in range(1, n+1):
        if n % i == 0:
            yield i
    #yield n
number = divs(4)
print(list(number))