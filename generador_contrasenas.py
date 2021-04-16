import random


def password_generetor():
    mayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    minus = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    simbols = ['!', '@', '$', '%', '&', '*', '(', ')', '_', '|' ]
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0' ]

    characters =  mayus + minus + simbols + numbers

    password = []

    for i in range(10):
        characters_random = random.choice(characters)
        password.append(characters_random)

    password = "".join(password)
    return password



def run():
    password = password_generetor()
    print('Your new password is: ' + password)



if __name__ == '__main__':
    run()
