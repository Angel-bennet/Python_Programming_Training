#leetcode9
def palindromeCheck(x):
    rev=0
    if x<0 or(x%10==0 and x!=0):
        return False
    while x>rev:
        dig=x%10
        rev=rev*10+dig
        x//=10
    return x==rev or x==rev//10
x=int(input())
print(palindromeCheck(x))