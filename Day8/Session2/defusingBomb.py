#leetcde1652
def defuseBomb(code,k):
    n=len(code)
    if k==0:
        return [0]*n
    ans=[0]*n
    for i in range(n):
        total=0
        if k>0:
            for j in range(1,k+1):
                total=total+code[(i+j)%n]
        else:
            for j in range(1,k+1):
                total+=code[((i-j)+n)%n]
        ans[i]=total
    return ans   
value=list(map(int,input().split()))
k=int(input())
print(defuseBomb(value,k))