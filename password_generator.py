import secrets
import string

# Ask the user for the password length
try:
    length = int(input("Enter password length: "))

# Handle invalid input
except ValueError:
    print("Error: Please enter a valid number.")

else:
    # Check the minimum password length
    if length < 12:
        print("Error: Password must be at least 12 characters long.")

    else:
        # Create a collection of available characters
        characters = string.ascii_letters + string.digits + string.punctuation

        # Start with an empty password
        password = ""

        # Securely select and add random characters
        for i in range(length):
            password = password + secrets.choice(characters)

        # Display the generated password
        print("Your password is:", password)
