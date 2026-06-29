n=int(input())
if n<=100 and n>0:
    result=n*1.50
elif n<=200 and n>100:
    result=(100*1.50)+(n-100)*2.50
else:
    result=(100*1.50)+(100*2.50)+(n-200)*4
print(result)
# OR
n=int(input())
if n<=100 and n>0:
    print(n*1.50)
elif n<=200 and n>100:
    print(100*1.50+(n-100)*2.50)
else:
    print(100*1.50+100*2.50+(n-200)*4)
