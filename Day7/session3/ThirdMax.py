#third max using binary search
def thirdMax(nums):
    unique=set(nums)
    unique=sorted(unique,reverse=True)
    #Sort in dec ord
    #Return third element
    if len(unique)>=3:
        return unique[2]
    return unique[0]
#main

nums=list(map(int,input().split()))
print(thirdMax(nums))