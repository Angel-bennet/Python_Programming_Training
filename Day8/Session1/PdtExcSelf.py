def productExcSelf(nums):
    n=len(nums)
    ans=[1]*n
    prefix=1
    #Prefix array
    for i in range(n):
        ans[i]=prefix
        prefix*=nums[i]
    suffix=1
    #suffix array
    for i in range(n-1,-1,-1):
        ans[i]*=suffix
        suffix*=nums[i]

    return ans
print(productExcSelf([1,2,3,4]))
