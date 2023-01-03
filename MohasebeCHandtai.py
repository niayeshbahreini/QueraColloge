def calc(num):
    avg_num = sum(num) / len(num)

    if(len(num)%2 == 0):
       middle_num =  (num[int((len(num) - 1) / 2)] + num[int((len(num) - 1) / 2) + 1]) / 2
    else:
      middle_num =  num[int( (len(num) - 1) / 2)]

    max_num = max(num)
    return (avg_num, middle_num, max_num)

calc([1, 2, 6])


print("--------")

def calc(a: list) -> tuple:
    avg_a = sum(a)/len(a)
    max_a = max(a)
    if len(a)%2 ==1:
        median_a = sorted(a)[len(a) // 2]
    else:
        median_a = (sorted(a)[len(a)//2 - 1] + sorted(a)[len(a)//2]) / 2

    return (avg_a,median_a,max_a)