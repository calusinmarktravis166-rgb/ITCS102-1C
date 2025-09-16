
import random

numbers = [random.randint(2, 120) for _ in range(12)]

print("Generated numbers:", numbers)

total = 0
for num in numbers:

    if num % 2 == 0:
        total += num

print("Sum of even numbers:", total)
