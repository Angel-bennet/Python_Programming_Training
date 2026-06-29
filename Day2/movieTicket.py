n=int(input())
category=int(input())
if n>=15 and category==1:
    print('price is',n*200-(0.25*200*n))
elif n>15 and category!=1:
    print('price is',n*200-(0.2*200*n))
elif n<15 and category==1:
    print('price is',n*200-(0.05*200*n))

else:
    print("price is",n*200)

#or
amt=200*n
d=0
if n>=15:
    d+=20
if category==1:
    d+=5
if d>0:
    amt=amt-(amt*d/100)
    if n>=15 and category==1:
        print("applied discount")
    elif n>15:
        print("Max discount")
    else: 
        print('Student discount')
else:
    print('No discount')
