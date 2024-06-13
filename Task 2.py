# Task 2: Calculator

# Importing the necessary libraries

# Defining the variables
a = input ("Enter operand 1: ")
b = input ("Enter operand 2: ")

# Taking the operation as input
print ("Enter the operation you want to perform: ")
print ("1. Addition")
print ("2. Subtraction")
print ("3. Multiplication")
print ("4. Division")
print ("5. Modulus")
print ("6. Exponentiation")
print ("7. Floor Division")

choice = input ("Enter your choice: ")

# Performing the operation
if choice == '1':
        print ("The result is: ", int(a) + int(b))
elif choice == '2':
        print ("The result is: ", int(a) - int(b))
elif choice == '3':
        print ("The result is: ", int(a) * int(b))
elif choice == '4':
        print ("The result is: ", int(a) / int(b))
elif choice == '5':
        print ("The result is: ", int(a) % int(b))
elif choice == '6':
        print ("The result is: ", int(a) ** int(b))
elif choice == '7':
        print ("The result is: ", int(a) // int(b))
else:
        print ("Invalid choice")