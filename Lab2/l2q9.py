import random as r
s=set()
for i in range (0,100):
    a=r.randint(0,30)
    if a not in s:
        s.add(a)
    if len(s)==10:
        break
print(s)
