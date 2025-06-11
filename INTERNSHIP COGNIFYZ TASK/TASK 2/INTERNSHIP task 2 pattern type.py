def pyramid_for_loop(rows):
    print("\n🔷 Pyramid Pattern using FOR Loop\n")
    for i in range(1, rows + 1):
        # Print leading spaces
        for j in range(rows - i):
            print(" ", end="")
        # Print stars
        for k in range(2 * i - 1):
            print("*", end="")
        print()  # New line after each row

def triangle_while_loop(rows):
    print("\n🔷 Right-Angled Triangle using WHILE Loop\n")
    i = 1
    while i <= rows:
        j = 1
        while j <= i:
            print("*", end=" ")
            j += 1
        print()  # New line after each row
        i += 1

def menu():
    print("\n🧩 Task 2: Pattern Generator")
    print("1. Pyramid Pattern (FOR Loop)")
    print("2. Right-Angled Triangle (WHILE Loop)")
    print("3. Exit")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            rows = int(input("Enter number of rows for pyramid: "))
            pyramid_for_loop(rows)
        elif choice == '2':
            rows = int(input("Enter number of rows for triangle: "))
            triangle_while_loop(rows)
        elif choice == '3':
            print("👋 Exiting Task 2. Thank you!")
            break
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")
