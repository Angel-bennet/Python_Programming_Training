a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    if b>c:
        print(b)
    else:
        print(c)
elif b>c:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if a>b:
        print(a)
    else:
        print(b)

#or
if (a>=b and a<=c) or (a<=b and a>=c):
    print(a)
elif (b>=a and b<=c) or (b<=a and b>=c):
    print(b)
else:
    print(c)

