n=int(input())
m=n**2
x=len(str(n))
r=m%(10**x)
l=m//(10**x)
if l+r==n:
    print("Keprekar Number")
else:
    print("Not keprekar")

