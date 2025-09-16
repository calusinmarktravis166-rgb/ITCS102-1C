number = eval(input("Enter a number --> "))
factorial = 2 
for x in range(number, 5, -2):
    factorial *= x
print("The factorial of ",number, "is",factorial)    