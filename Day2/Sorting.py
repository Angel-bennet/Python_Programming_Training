a=int(input())
b=int(input())
c=int(input())
d=int(input())
largest=0
if a>b and a>c and a>d:
    largest=a
elif b>c and b>d :
    largest=b
elif  c>d :
    largest=c
else:
    largest=d
print("largest value is",largest)

# using priority queue