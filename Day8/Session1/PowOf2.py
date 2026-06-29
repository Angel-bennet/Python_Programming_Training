#leetcode231
def chechPowOfTwo(n):
    return n>0 and (n&(n-1)==0) #bit manipuation
n=int(input())
print(chechPowOfTwo(n))
