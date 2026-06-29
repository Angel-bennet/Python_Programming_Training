c=int(input())
if c>=0 and c<1:
    print("No rain")
elif c>=1 and c<5:
    print('Light rain')
elif c>=5 and c<10:
    print('moderate rain')
else:
    print("Heavy rain")