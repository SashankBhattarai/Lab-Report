l=[]
n=int(input("How many elements?"))
for i in range (0,n):
    a=int(input("Elements:"))
    l.append(a)
#using built in functions
print(f"Max={max(l)} \nMin={min(l)}")
ascending=l
ascending.sort()
print(f"Ascending:{ascending}")
print(f"Removing duplicate elements:{set(l)}")

#without using built in functions
max_=l[0]
for num in l:
    if num>max_:
        num=max_
print(f"Max={max_}")
min_=l[0]
for num in l:
    if num<min_:
        num=min_
print(f"Min={min_}")

ascending=l
for i in range (len(ascending)):
    for j in range (i+1,len(ascending)):
        if ascending[i]>ascending[j]:
            t=ascending[i]
            ascending[i]=ascending[j]
            ascending[j]=t
print(f"Ascending:{ascending}")

set=[]
for item in l:
    if item not in set:
        set.append(item)
print(f"Removing duplicate elements:{set}")
