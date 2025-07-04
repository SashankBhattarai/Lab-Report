n=["Rudy","Nana","Bob","Eris","Norn","Bob","Rudy","Norn","Bob"]
count={}
for name in n:
    if name not in count:
        count[name]=1
    else:
        count[name]+=1
print(count)