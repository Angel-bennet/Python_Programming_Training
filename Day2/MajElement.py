nums=[3,2,3]
c=0
candidate=0
for num in nums:
    if c==0:
        candidate=num
    if num==candidate:
        c+=1
    else:
        c-=1
print(candidate)
