#leetcode69
#brute
# def sqrt(x):
#     i=0
#     while i*i<=x:
#         i+=1
#     return i-1
# print(sqrt(8))
#binary search
def sqrt(x):
    left=0
    right=x
    while left<=right:
        mid=left+(right-left)//2
        if mid*mid==x:
            return mid
        elif mid*mid<x:
            left=mid+1
        else:
            right=mid-1
    return right
print(sqrt(int(input())))

