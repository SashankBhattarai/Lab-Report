def add():
    try:
        name = input("Name: ")
        phone = input("Phone: ")
        with open("contacts.txt", "a") as f:
            f.write(name + "," + phone + "\n")
        print("Saved")
    except Exception as e:
        print("Error while adding:", e)

def view():
    try:
        with open("contacts.txt", "r") as f:
            lines = f.readlines()
            if len(lines) == 0:
                print("No contacts found")
            else:
                for l in lines:
                    print(l.strip())
    except FileNotFoundError:
        print("contacts.txt not found")

def search():
    try:
        x = input("search: ")
        found = False
        with open("contacts.txt", "r") as f:
            for l in f:
                if x in l:
                    print("Found:", l.strip())
                    found = True
        if not found:
            print("No contact found")
    except FileNotFoundError:
        print("contacts.txt not found")

while True:
    print("\n1 Add\n2 View\n3 Search\n4 Exit")
    c = input(">> ")
    if c == "1":
        add()
    elif c == "2":
        view()
    elif c == "3":
        search()
    elif c == "4":
        break
    else:
        print("Invalid choice")
