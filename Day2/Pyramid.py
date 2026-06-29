n=int(input())
# for i in range(1,2*n,2):
#     print(' '*(2*n-i)+'* '*i)
# #or
for i in range(n):
    print(' '*(n-i-1),end=' ')
    print('*'*(2*i+1))