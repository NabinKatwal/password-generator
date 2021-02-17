import random

def generate(length):
    counter = 1
    password_list = []
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '&', '_']
    while True:
        if counter<length-2:
            password_list.append(random.choice(alphabet))
        elif counter>=length-2 and counter<length-1:
            password_list.append(random.choice(numbers))
        else:
            password_list.append(random.choice(symbols))
        if counter == length:
            break
        counter+=1

    print(str(password_list))

generate(10)