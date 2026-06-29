#leetcode326
def checkPowOfThree(n):
    if n<=0:
        return False
    while n%3==0:
        n//=3
    return n==1
n=int(input())
print(checkPowOfThree(n))
