fruit_list = []

def show_menu():
    print("\n=== Fruit List Program ===")
    print("1. Add a fruit")
    print("2. View all fruits")
    print("3. Remove a fruit")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        fruit = input("Enter the name of the fruit to add: ").strip()
        if fruit:
            if fruit not in fruit_list:
                fruit_list.append(fruit)
                print(f"'{fruit}' has been added to your list.")
            else:
                print(f"'{fruit}' is already in your list.")
        else:
            print("You didn't enter a fruit name.")

    elif choice == "2":
        if fruit_list:
            print("\nYour fruit list:")
            for i, f in enumerate(fruit_list, 1):
                print(f"{i}. {f}")
        else:
            print("\nYour fruit list is empty.")

    elif choice == "3":
        if fruit_list:
            fruit_to_remove = input("Enter the name of the fruit to remove: ").strip()
            if fruit_to_remove in fruit_list:
                fruit_list.remove(fruit_to_remove)
                print(f"'{fruit_to_remove}' has been removed.")
            else:
                print(f"'{fruit_to_remove}' was not found in your list.")
        else:
            print("Your fruit list is empty — nothing to remove.")

    elif choice == "4":
        print("\nThank you for using the Fruit List Program! Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
