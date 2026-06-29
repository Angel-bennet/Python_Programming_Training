#leetcode 1011
def shippingCapacity(weights,days):
    left=1
    right=sum(weights) #worst case scenario 65 tones in 1 day
    answer=right
    while left<=right:
        mid=left+(right-left)//2
        total_days=1 #worst case using i day
        current_load=0
        for weight in weights:
            if current_load+weight>mid:
                total_days=total_days+1
                current_load=0
            current_load+=weight
        if total_days<=days:
            answer=mid
            right=mid-1
        else:
            left=mid+1
    return(answer)
print(shippingCapacity([1,2,3,4,5,6,7,8,9,10],5))