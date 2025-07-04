d1 = {'a':5,'b':8,'c':12}
d2 = {'b':3,'c':4,'d':10}

d = d1
for key in d2:
    if key in d1:
        d[key] += d2[key]  # add value if key exists in both
    else:
        d[key] = d2[key]   # merge

print(d)
