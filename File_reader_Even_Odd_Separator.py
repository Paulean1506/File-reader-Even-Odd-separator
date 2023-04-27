# Paulean Marguerette F. Parrish
# Bscpe 1-4
# Problem no. 1
# Write a Python program that reads a text file named numbers.txt that contains 20 integers. 
# The program will create two other text file; the first text file will be named even.txt that will contains all even numbers extracted 
# from the numbers.txt. The second text file will be named odd.txt that will contains all odd numbers extracted from the numbers.txt.

# Header design
import pyfiglet

print(" \033[93mHello! I hope you're having a great day!!! ".center(70, "="))

# Ask for the name of the user
user_name = input("\033[95mMay I know your name? \033[0m")
print("\033[93mThank you", user_name,  "you may now proceed to the program!")

# Open the numbers.txt and read the file
with open('numbers.txt', 'r') as input_file:

    # Open two empty text files; even.txt and odd.txt
    with open('even.txt', 'w') as even_file, open('odd.txt', 'w') as odd_file:
        # Iterate over each line of the input file
        for line in input_file:
            # Convert the line to an integer
            num = int(line.strip())

            # Check if the number is even, then write the number in the even.txt file
            if num % 2 == 0:
                even_file.write(str(num) + '\n')