text=input("Text:")
freq={}
for char in text:
    if char.isalnum(): #only true for numbers and letters
        char.lower()
        if char not in freq:
            freq[char]=1
        else:
            freq[char]+=1
print(freq)