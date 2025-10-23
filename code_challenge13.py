print("===================================")
print("          ODD NUMBER SORTER")
print("===================================\n")

name = input("Enter your name: ").strip().title()
print(f"\nWelcome, {name}! This program will collect numbers from you,")
print("then show only the odd ones in sorted order.")
print("Type '0' when you are done.\n")

numbers = []

while True:
    try:
        num = int(input("Enter a number (0 to finish): "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue

    if num == 0:
        print("Input finished.\n")
        break
    numbers.append(num)

if numbers:
    odd_numbers = [n for n in numbers if n % 2 != 0]
    if odd_numbers:
        odd_numbers.sort()
        print("Odd numbers sorted in ascending order:")
        print(odd_numbers)
    else:
        print("No odd numbers were entered.")
else:
    print("You didn’t enter any numbers.")

print("\nThank you for using the Odd Number Sorter.")
