
odd_sum = 0

print("ODD NUMBER ACCUMULATOR")
print("Enter 10 numbers. We'll sum only the odd ones!")

for i in range(1, 11):
    number = int(input(f"Enter number {i}: ")) 
    
    if number % 2 != 0:
        odd_sum += number 

print(f"\nSum of all odd numbers: {odd_sum}")
