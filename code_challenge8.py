
number = int(input("Enter a number: "))

print(f"\nMultiplication table for {number}:")

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
