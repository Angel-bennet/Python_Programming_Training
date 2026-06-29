# Leetcode125
s=input()        
cleaned=""
for ch in s:
    s=s.replace(" ",'')
    if ch.isalnum():
        cleaned+=ch.lower()
    if cleaned==cleaned[::-1]:
        print(True)
    else:
        print(False)