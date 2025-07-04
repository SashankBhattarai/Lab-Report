n=int(input("Enter a number :"))
temp=n
r=0
while temp>0:
    r = r * 10 + (temp%10)
    temp = temp // 10

if r==n:
    print("Palindrome")
else:
    print("Not palindrome")
