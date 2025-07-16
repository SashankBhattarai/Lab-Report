s = {"Ram": [85, 90, 78],"Shyam": [92, 88, 95],"Hari": [70, 65, 72]}

print("Average marks of each student:")
for name in s:
    marks =s[name]
    avg = sum(marks) / len(marks)
    print(f"{name}:{avg}")

topper = ""
havg = 0

for name in s:
    marks =s[name]
    avg = sum(marks) / len(marks)
    if avg > havg:
        havg = avg
        topper = name

print(f"Topper: {topper} with avg marks {havg:}")

print("Updating marks)")
s["Samrat"] = [98, 94, 96] 


print("Updated avg marks of each student:")
for name in s:
    marks =s[name]
    avg = sum(marks) / len(marks)
    print(f"{name}: {avg}")


topper = ""
havg = 0

for name in s:
    marks =s[name]
    avg = sum(marks) / len(marks)
    if avg > havg:
        havg = avg
        topper = name

print(f"New Topper: {topper} with avg marks {havg}")
