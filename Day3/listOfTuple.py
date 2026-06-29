tup_list=eval(input())
k=int(input())
pdt=1
for i in tup_list:
    pdt=pdt*i[k]
print(f"Product:{k}:{pdt}")