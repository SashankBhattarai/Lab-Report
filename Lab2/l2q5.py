l=[23,12,17,14,13,12,25]
le=[]
prime=[]
for i in range (len(l)):
    if i%2==0:
        le.append(i)
print("Elements at even indexes",le)
for n in l:
    for i in range(2, n):
        if n%i==0:
            break
    else:
        prime.append(n)
print("Prime",prime)