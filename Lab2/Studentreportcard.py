# Dictionary ko bhitra dictionary ko bhitra dictionary
students = {
        101: {"name": "Suraj", "marks": {"Math": 80, "Science": 75, "English": 85}},
        102: {"name": "Samrat", "marks": {"Math": 40, "Science": 30, "English": 35}},
        103: {"name": "Hari", "marks": {"Math": 90, "Science": 95, "English": 85}}
}

# Add a student
rn = input("Enter new roll number (n to skip): ")
if rn != "n":
    rn = int(rn)
    name = input("Enter student name:")
    math = int(input("Math:"))
    sci = int(input("Science:"))
    eng = int(input("English:"))
    students[rn] = {"name": name, "marks": {"Math": math, "Science": sci, "English": eng}}
    print(f"{name} added.")

# View all data
print("All student reports:")
for r, data in students.items(): # r =101, data= {"name": "Alice", "marks": {"Math": 80, "Science": 75, "English": 85}}
    print(f"{r},{data}")

# Display topper
highest = 0
for data in students.values():
    avg = sum(data["marks"].values())/len(students)
    if avg > highest:
        highest = avg

print(f"Toppers:")
for r, data in students.items():
    avg = sum(data["marks"].values())/3 #Sum of data in values of "marks"(skip key)
    if avg == highest:
        print(f"{r},{data}")

# Search by roll number
srn = input("Enter roll number to search (n to skip): ")
if srn != "n":
    srn = int(srn)
    if srn in students:
        print(f"{students[srn]}")
    else:
        print("Student not found.")

# Students who failed in one or more subjects
print("Students who failed in one or more subjects:")
found = 0
for r, data in students.items():
    for subject, mark in data["marks"].items():
        if mark < 40:
            print(f"{r,data}")
            found = 1
            break
if found == 0:
    print("No student failed.")

# Update marks
um = input("Enter roll number to update marks (n to skip): ")
if um != "n":
    um = int(um)
    if um in students:
        print(f"Old marks: {students[um]['marks']}")
        math = int(input("New Math marks: "))
        sci = int(input("New Science marks: "))
        eng = int(input("New English marks: "))
        students[um]["marks"] = {"Math": math, "Science": sci, "English": eng}
        print("Marks updated.")
    else:
        print("Student not found.")