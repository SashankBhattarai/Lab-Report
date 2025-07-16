stack = []
queue = []

def push():
    element = input("Enter element to push onto stack: ")
    stack.append(element)
    print(f"{element} pushed to stack.")

def pop():
    if stack:
        element = stack.pop()
        print(f"{element} popped from stack.")
    else:
        print("Stack is empty.")

def enqueue():
    element = input("Enter element to enqueue into queue: ")
    queue.append(element)
    print(f"{element} enqueued to queue.")

def dequeue():
    if queue:
        element = queue.pop(0)
        print(f"{element} dequeued from queue.")
    else:
        print("Queue is empty.")

def display():
    print("\nCurrent Stack:", stack)
    print("Current Queue:", queue)

while True:
    print("\nChoose an operation:")
    print("1. Push (Stack)")
    print("2. Pop (Stack)")
    print("3. Enqueue (Queue)")
    print("4. Dequeue (Queue)")
    print("5. Display both")

    choice = input("Enter your choice (1-5)(Enter to exit): ")

    if choice == '1':
        push()
    elif choice == '2':
        pop()
    elif choice == '3':
        enqueue()
    elif choice == '4':
        dequeue()
    elif choice == '5':
        display()
    else:
        break