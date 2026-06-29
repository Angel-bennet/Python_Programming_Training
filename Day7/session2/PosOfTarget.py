#leetcode34
def find_first(nums,target):
    left=0 #intial value
    right=len(nums)-1 #last value
    ans=-1
    while left<=right:
        mid=left+(right-left)//2
        if nums[mid]==target:
            ans=mid
            right=mid-1
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1

    return ans
def find_last(nums,target):
    left=0 #intial value
    right=len(nums)-1 #last value
    ans=-1
    while left<=right:
        mid=left+(right-left)//2
        if nums[mid]==target:
            ans=mid
            left=mid+1
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1

    return ans
nums=[5,7,7,8,8,9]
target=8
fir_index=find_first(nums,target)
last_index=find_last(nums,target)
print([fir_index,last_index])

