
def comb(n, k):
    ans =1 
    for i in range(n - k + 1 , n + 1):
        ans *=i
        
    for i in range (1, k + 1):
        ans /= i 
        print(i)
    return ans
    
comb(5,3)