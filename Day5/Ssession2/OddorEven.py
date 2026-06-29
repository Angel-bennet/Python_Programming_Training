num=[1,2,3,4,5,6]
num=list(map(int,input()))
even=list(filter(lambda y:y%2==0,num))
print(even)