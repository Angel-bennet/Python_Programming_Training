#Dp program approach
def climbStairs(n):
    if n<=3:
        return n
    a,b=3,2
    cur_val=0
    for i in range(3,n):
        cur_val=a+b
        b=a
        a=cur_val
    return cur_val
n=int(input())
print(climbStairs(n))