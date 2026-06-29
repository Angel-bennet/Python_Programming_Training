n=int(input())
pdt=1
while n!=0:
    p=n%10
    n=n//10
    pdt=pdt*p
print(pdt)