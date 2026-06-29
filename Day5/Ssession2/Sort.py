n=[
    ("Aslaha",25),
    ("Dinix",23),
    ("Susanne",25)
]
sort=sorted(
    n,
    key=lambda x:x[1] #sort by age
)
print(sort)
#max()
n=[
    ("Aslaha",25),
    ("Dinix",23),
    ("Susanne",25)
]
sort=max(
    n,
    key=lambda x:x[1] #sort by age
)
print(sort)
#min()
n=[
    ("Aslaha",25),
    ("Dinix",23),
    ("Susanne",25)
]
sort=min(
    n,
    key=lambda x:x[1] #sort by age
)
print(sort)