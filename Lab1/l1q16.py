positive = 0
negative = 0
zero = 0
for i in range(10):
    num = int(input(f"Enter integer #{i+1}: "))    
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print(f"Positive numbers: {positive}")
print(f"Negative numbers: {negative}")
print(f"Zeros: {zero}")