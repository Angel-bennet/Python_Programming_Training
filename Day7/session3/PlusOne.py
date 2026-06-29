#leetcode66
def plusOne(dig):
    n=len(dig)
    for i in range(n-1,-1,-1):
        if dig[i]<9:
            dig[i]+=1
            return dig
        dig[i]=0
    return[1]+dig
        

dig=[1,2,9]
print(plusOne(dig))