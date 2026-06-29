s=input(("Enter the string"))
mid=len(s)//2
p1=s[:mid]
p2=s[mid:]
#reverse str
revp1=p1[::-1]
revp2=p2[::-1]
print(revp1+revp2)
    