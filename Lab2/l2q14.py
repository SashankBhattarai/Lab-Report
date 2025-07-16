p = {"Pen": 10,"Notebook": 50,"Pencil": 5,"Eraser": 7}

np = input("Enter new product name(n to skip): ")
if np!="n":
    price = float(input("Price: "))
    p[np] = price
    print(f"{np} added.")

#Update price(ptu=product to update)
ptu = input("Enter product name to update price(n to skip): ")
if ptu!="n":
    if ptu in p:
        new_price = float(input("Enter new price: "))
        p[ptu] = new_price
        print(f"Price of {ptu} updated to {new_price}.")
    else:
        print(f"{ptu} not found in the list.")

# Minimum and maximum price
low = float(input("Enter minimum price: "))
high = float(input("Enter maximum price: "))

print(f"Product in the price range {low} to {high}:")
found=0
for name, price in p.items():
    if low <= price <= high:
        print(f"{name}: {price}")
        found = 1
if found==0:
    print("No product found in this range.")
