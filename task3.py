import random
import string

def generate_password(password_length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]
    password += random.choices(all_characters, k=password_length - 4)
    random.shuffle(password)
    return ''.join(password)

while True:
    password_length = int(input("Enter the desired password length: "))
    password = generate_password(password_length)
    print("Generated Password:", password)
    response = input("Do you want to create another password? (yes/no): ").strip().lower()
    if response == 'no':
        print("generated password is used.")
        break
    elif response == 'yes':
        print("Generating a new password...")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
