#leetcode 283
#two pointer approach
# 1.left
# 2.right
def moveZeroes(nums):
    left=0
    for right in range(len(nums)):
        if nums[right]!=0:
            nums[right],nums[left]=nums[left],nums[right]
            left=left+1
    return nums
nums=[12,0,3,0,4]
print(moveZeroes(nums))