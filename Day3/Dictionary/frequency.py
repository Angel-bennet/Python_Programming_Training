n=list(map(int,input().split()))
k=int(input("threshold point"))
freq={}
for i in n: #initialise the dictionary
    freq[i]=freq.get(i,0)+1 #get key-value-> num-count
for key,count in freq.items(): #checkingvalues
    if count>k:
        print(f"{k}:{count} times")