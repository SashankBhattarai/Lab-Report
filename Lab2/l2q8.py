u=set()
for i in range (0,40):
    u.add(i)
f={4,7,9,11,12,14,21,26,32,36,38}
c={2,7,9,10,11,12,13,16,17,18,22,26}
print(f"Students who play both sports:{f.intersection(c)}")
print(f"Students who play football:{f}")
print(f"Students who play cricket:{c}")
print(f"Students who play neither:{u-(f.union(c))}")