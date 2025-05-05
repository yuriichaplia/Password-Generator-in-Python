import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\nWelcome to the Password Generator Program!")
nr_letters = int(input("\nHow many letters would you like to have in your password?: "))
nr_symbols = int(input(f"How many symbols would you like to have in your password?: "))
nr_numbers = int(input(f"How many numbers would you like to have in your password?: "))

password = ""
for letters1 in range(0, nr_letters):
    password += random.choice(letters)
for symbols1 in range(0, nr_symbols):
    password += random.choice(symbols)
for numbers1 in range(0, nr_numbers):
    password += random.choice(numbers)

shuffled_password = list(password)
random.shuffle(shuffled_password)
result = ''.join(shuffled_password)

print(f"\nYour password: {result}")



