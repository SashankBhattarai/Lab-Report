#3. Write a Python function that accepts a list and returns a new list with only
#the even numbers from the original list.
l=[]
even=[]
for i in range (5):
    a=int(input("Add to l1:"))
    l.append(a)
for j in l:
    if j%2==0:
        even.append(j)
print(even)