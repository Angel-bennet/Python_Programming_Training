n=input()
inc=True
dec=True
for i in range(len(n)-1):
    if int(n[i+1])!=int(n[i])+1:
        inc=False
    if int(n[i+1])!=int(n[i])-1:
        dec=False
if inc:
    print("Increasing fancy Number")
elif dec:
    print("Decreasing fancy Number")
else:
    print("Not Fancy Number")