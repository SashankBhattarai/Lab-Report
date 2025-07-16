import statistics as s

t = (2, 7, 21, 4, 19, 6, 7, 11, 23)
l = list(t)
l.sort() 

total = 0
for i in t:
    total += i

n = len(t)
avg = total / n
print("Average =", avg)

median = s.median(l)
mode = s.mode(l)
print("Median =", median)
print("Mode =", mode)