a=input("Sentence: ")
a=a.lower()
vowels=set()
for i in range (0,len(a)):
    if (a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u"):
            vowels.add(a[i])
print(vowels)