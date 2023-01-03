#print(sum([1 if i== '1'else 0 for i in str(bin(int(input())))]))

print("{n:b}".format(n = int(input())).count('1'))

print("or you can write : ")

print("{:b}".format(int(input())).count('1'))
