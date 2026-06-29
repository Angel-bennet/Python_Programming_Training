#Dynamic Programming
str=input()
n=len(str)
dp=[0]*(n+1) #->[0,0,0.....]
#Initialization
dp[0]=1
dp[1]=1
for i in  range(2,n+1):
    #single_digit
    one_dig=int(str[i-1:i])
    if 1<=one_dig<=9:
        dp[i]=dp[i]+dp[i-1]
    two_dig=int(str[i-2:i])
    if 10<=two_dig<=26:
        dp[i]+=dp[i-2]
print(dp[n])