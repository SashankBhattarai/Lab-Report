#4. Write a program to count the number of each character in a given string
#using a dictionary.
d={}
s="Tyrannosaurus"
for i in s: #Takes a letter from string
    if i not in d.keys(): #if its not already in the directory, it adds it
        d[i]=s.count(i) #count no. of i 
print(d)