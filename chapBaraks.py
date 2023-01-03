myList=list()
a = None

while a !=0 :
    a=int(input())
    myList.append(a)
    
myList.remove(0)
myList.reverse()
for i in myList:
    print(i)
print('-----')

a=int(input())
mylist=[]
while a!=0 :
    mylist.append(a)
    a=int(input())
    
mylist.reverse()
for i in mylist :
    print(i) 

numbers = []
num = input()

while (num!='0'):
    numbers.append(num)
    num = input()

numbers.reverse()
for i in numbers:
    print(i)

