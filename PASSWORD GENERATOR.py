import random
import string

def generate_password(length):
    """
    Generate a random password of specified length.
    """
    # Define characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password by randomly selecting characters from the defined set
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Simple Password Generator!")
    length = int(input("Enter the length of the password: "))
    
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
