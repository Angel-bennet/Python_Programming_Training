n=int(input())
# for i in range(2*n-1,0,-2):
#     print(' '*(2*n-i)+'* '*i)
# for i in range(3,2*n,2):
#     print(' '*(2*n-i)+'* '*i)
# or
for i in range(n):
    print(' '*(n-i-1),end=' ')
    print('*'*(2*i+1))
for i in range(n-2,-1,-1):
    print(' '*(n-i-1),end=' ')
    print('*'*(2*i+1))