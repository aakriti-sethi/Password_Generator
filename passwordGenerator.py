import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("welcome to the python generator!")

letters_req = int(input("how many letters would you like in your password? "))

symbols_req = int(input("how many symbols would you like? "))

numbers_req = int(input("how many numbers would you like? "))


password = ""

for char in range(1, letters_req + 1):
    password += random.choice(letters)


for char in range(1, numbers_req +1):
    password += random.choice(numbers)


for char in range(1, symbols_req + 1):
    password += random.choice(symbols)


password_list = random.sample(password, len(password))

final = ""
for char in password_list:
    final += char

print(f"your password is {final}")