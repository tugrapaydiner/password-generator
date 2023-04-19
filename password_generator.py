import random
import string

def generate_password(length, chars, has_lower, has_upper, has_digit, has_punct):
    password = ""
    for _ in range(length):
        while True:
            char = random.choice(chars)
            if (has_lower and char in string.ascii_lowercase) or \
               (has_upper and char in string.ascii_uppercase) or \
               (has_digit and char in string.digits) or \
               (has_punct and char in string.punctuation):
                password += char
                break
    return password

def main():
    generated_passwords = []

    password_length = 16
    password_chars = string.ascii_letters + string.digits + string.punctuation
    has_lower = True
    has_upper = True
    has_digit = True
    has_punct = True
    password = generate_password(password_length, password_chars, has_lower, has_upper, has_digit, has_punct)
    generated_passwords.append(password)
    print(f"Your new password is: {password}")

    # Ask the user if they want to generate another password
    while input("Do you want to generate another password? (y/n) ") == "y":
        password_length = int(input("Enter password length: "))
        has_lower = input("Include lowercase letters? (y/n) ") == "y"
        has_upper = input("Include uppercase letters? (y/n) ") == "y"
        has_digit = input("Include digits? (y/n) ") == "y"
        has_punct = input("Include punctuation? (y/n) ") == "y"

        # Create the set of allowed characters based on the user's input
        password_chars = ""
        if has_lower:
            password_chars += string.ascii_lowercase
        if has_upper:
            password_chars += string.ascii_uppercase
        if has_digit:
            password_chars += string.digits
        if has_punct:
            password_chars += string.punctuation

        password = generate_password(password_length, password_chars, has_lower, has_upper, has_digit, has_punct)
        generated_passwords.append(password)
        print(f"Your new password is: {password}")

if __name__ == "__main__":
    main()

    segsdgdsg