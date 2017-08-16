import random

def password_generator(length=8, simple=False):
    """ Generates a password

        Arguments:
        lenght -- password lenght. Default is 8 chars
        simple -- only letters and numbers
    """
    letters_numbers = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890abcdefghijklmnopqrstuvwxyz1234567890"
    rest = "!@#$%^&*()_+"

    if simple:
        seed = letters_numbers
    else:
        seed = letters_numbers + rest
    
    password = ""
    for i in range(length):
        random_position = random.randint(0, len(seed) - 1)
        password += seed[random_position]

    return password

def main():
    print(password_generator())
    print(password_generator(10))
    print(password_generator(10, True))

main()
