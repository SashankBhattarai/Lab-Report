d={}
n=int(input("How many key values do you want to enter?"))

for i in range (n):
    key=input(f"Enter key {i+1} :")
    value=int(input("Enter value :"))
    d[key]=value            ####

search=input("What key do you want to search for?")
if search in d:
    print(d[search])