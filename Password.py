import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=True):
    # Define character sets
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    # Ensure the user has selected at least one character type
    if not characters:
        raise ValueError("At least one character type must be selected.")
    
    # Randomly select characters from the available pool
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    # Get user inputs
    length = int(input("Enter the desired password length: "))
    
    # Ask user about the complexity
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    
    # Generate and print password
    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(e)

# Run the program
if __name__ == "__main__":
    main()
