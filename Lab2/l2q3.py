a=input("Sentence:")
a=a.lower()
words=a.split()
unique_words=[]
freq=[]
for word in words:
    if word in unique_words:
        key=unique_words.index(word)
        freq[key]+=1
    else:
        unique_words.append(word)
        freq.append(1)
print("\nWord Frequencies:")
for i in range(len(unique_words)):
    print(f"{unique_words[i]}: {freq[i]}")