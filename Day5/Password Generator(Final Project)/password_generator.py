# Password Generator Project
import random
import string

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+']

print("Welcome to the PyPassword Generator")

n_letters = int(input("How many letters would you like in your password?\n"))
n_symbols = int(input("How may symbols would you like? \n"))
n_numbers = int(input("How many numbers would you like? \n"))

total_rand_password = ""

for char in range(0, n_letters):
    random_char = random.choice(letters)
    total_rand_password += random_char

for symbol in range(0, n_symbols):
    random_symbol = random.choice(symbols)
    total_rand_password += random_symbol

for number in range(0, n_numbers):
    random_number = random.choice(numbers)
    total_rand_password += random_number

# Easy Level
print("Easy Level")
print(f"Your Password is: {total_rand_password}")

# Hard Level
print("Hard Level")
# 1- using random.sample(population, k)
#    Returns a random sample from a sequence of length k.
print("--- By using random.sample() ---")
print(f"Your Password is: {''.join(random.sample(total_rand_password, len(total_rand_password)))}")

# 2- using random.shuffle(x)
#    This is used to shuffle the sequence in place. A sequence can be any list/tuple containing elements.

# Convert from (string) to list
password_list = []
password_list[:0] = total_rand_password

random.shuffle(password_list)
print("--- By using random.shuffle() ---")
print(f"Your Password is: {''.join(password_list)}")
