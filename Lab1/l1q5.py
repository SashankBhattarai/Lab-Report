s = set()
for i in range(2, 51):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        s.add(i)
print(s)
  
check=int(input("which number do you want to check?"))
if check in s:
    print(f"{check} is prime")
else:
    print(f"{check} is not prime")