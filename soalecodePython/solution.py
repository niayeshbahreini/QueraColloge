



    



def solve(path):
    count = 0
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if not len(line) == 0 and not line.startswith('#'):
                count += 1
    return count
    


def solve(path):
    i=0
    with open(path) as file:
        for row in file:
            line=row.strip()
            if line !='' and line.startswith('#')== False:
                i+=1
    return i

