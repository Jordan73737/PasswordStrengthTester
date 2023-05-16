while True:
    password_strength_result = 0
    password = input("Enter new password: ")
    # Password Length Check
    if len(password) >= 8:
        password_strength_result += 1

    # Password Digit Check
    for character in password:
        if character.isdigit():
            password_strength_result += 1
            break

    # Password Lowercase Letter Check
    for character in password:
        if character.islower():
            password_strength_result += 1
            break

    # Password Uppercase Letter Check
    for character in password:
        if character.isupper():
            password_strength_result += 1
            break

    # Special Character Check

    special_characters = "\"!?£$%^&*()-_+={[}]:;@'~#<,>./`¬\|¦"
    for character in password:
        if character in special_characters:
            password_strength_result += 1
            break

    if password_strength_result >= 5:
        print("That's a very strong password you got there!")

    elif password_strength_result == 4:
        print("That's a strong password")

    elif password_strength_result == 3:
        print("That's a decent password")

    elif password_strength_result <= 2:
        print("That's a weak password")

    elif password_strength_result <= 1:
        print("That's barely a password...")

    print(password_strength_result)



