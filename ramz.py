k = int(input())
password = input()

wheels = [input() for i in range(k)]

result = 0

for i in range(k):
    idx = wheels[i].index(password[i])
    result += idx if idx < 5 else 9-idx

print(result)


print('----------')


k = int(input())

secret_key = input()

place = list()


def check_secret(key, numbers):
    reverse_numbers = numbers[::-1]
    if key in numbers:
        n = numbers.find(key)
        m = reverse_numbers.find(key)
        if n <= m:
            place.append(n)
        else:
            place.append(m + 1)

    return place


if len(secret_key) > k:
    print('Error')
else:
    for i in secret_key:
        a = input()
        check_secret(i, a)
    print(sum(place))


print('----------')

k = int(input())

s = input()

a = [input() for i in range(k)]

cnt = 0

for i in range(k):
    tmp = a[i].find(s[i])
    cnt += min(9 - tmp , tmp)

print(cnt)
