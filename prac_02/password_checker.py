"""

CP1404/CP5632 - Practical

Password checker "skeleton" code to help you get started

"""

MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password\nYour password must be between {} and {} characters, and contain:\n"
          "\t1 or more lowercase characters\n\t1 or more lowercase characters\n\t1 or more numbers"
          .format(MIN_LENGTH, MAX_LENGTH))

    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)

    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your " + str(
        len(password)) + " character password is valid: " + password)


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) > 15 or len(password) < 5:
        return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1
    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False
    if SPECIAL_CHARS_REQUIRED and count_special == 0:
        return False
    # if we get here (without returning False), then the password must be valid

    return True


main()
