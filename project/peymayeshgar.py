class Reverse:
    def __init__(self,ls):
        self.ls = ls
        self.lst = ls.copy()


    def __iter__(self):
        return self

    def __next__(self):
        if len(self.lst) == 0:
            raise StopIteration
        return self.lst.pop()

ls = [10, 20, 30]
for i in Reverse(ls):
    print(i)
print(ls)