# Task 3: Password Generator

# Importing the necessary libraries
from random import choice

# Defining the function to generate a password
def generate_password(n):
    # Defining the characters to be used in the password
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;:,.<>?`~"
    # Generating the password
    password = "".join(choice(characters) for i in range(n))
    # Returning the password
    return password

# Taking the length of the password as input
n = int(input("Enter the length of the password: "))
# Generating the password
password = generate_password(n)
# Printing the password
print("The generated password is:", password)