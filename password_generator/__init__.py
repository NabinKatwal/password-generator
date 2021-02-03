from password_generator.generator import generator
from password_generator.validator import validator
import sys

# choice = 'B'
flag = 1
print("Welcome to password Validator and Generator!")
while flag == 1:
    print("""
        Choose one option(A/B/C/D):\n
        A: Validate Password\n
        B: Generate Password\n
        C: Save Generated Password(s)\n
        D: Exit""")
    choice = str(input("Pick One>>").upper()).strip()

    if choice == 'A':
        pass

    elif choice == 'B':
        pass

    elif choice == 'C':
        pass

    elif choice == 'D':
        print("Closing the program!!")
        sys.exit()

    else:
        print("Invalid Choice, Pick Again!")