from math import pow, sqrt 

# Function to calculate the hypotenuse of a triangle using Pythagorean Theorem
def calculate_hypotenuse(side1, side2):
    #Returns hypotenuse of a triangle.

    #Parameters:
    #    side1 (float):The length of one side of the triangle.
    #    side2 (float):The length of the other side of the triangle.

    #Returns:
    #    hypotenuse (float):The hypotenuse of the triangle. 

    return sqrt(pow(side1, 2) + pow(side2, 2))

print(calculate_hypotenuse(2.0,2.0))
print(calculate_hypotenuse(12.0,12.0))

print("\n#-----------------------------------------------------#\n")

# Read foobar.txt and print each line with a comma "," appended
file = open('foobar.txt', 'r')
for line in file:
    lineWithoutNewLine = line.replace("\n", "")
    print(f"{lineWithoutNewLine},")
file.close()

print("\n#-----------------------------------------------------#\n")

# fibo library (installed the py-fibonacci module locally using 'pip install py-fibonacci')
from fibonacci import fibonacci

# Function to calculate the fibonacci sequence up to the nth number and display the info
# in a user-friendly manner
def fibonacci_info(n):
    #Prints fibonacci sequence information up to the nth number.

    #Parameters:
    #    n (int):The number of up to which to calculate the fibonacci sequence.

    #Returns:
    #    None.

    if n < 1:
        print(f"ERROR: You entered {n}")
        print("The input must be >= 1")
    else:
        sequence = fibonacci(n)
        print(f"The fibonacci sequence up to {n} is {sequence}")

fibonacci_info(100)

print("\n#-----------------------------------------------------#\n")

import sys

# Function to take two arguments from the user and print both arguments out
def sys_out():
    #Prints the two user-provided arguments.

    #Parameters:
    #    None. (Parameters are indirectly provided when the main.py file is run from the terminal/command line)

    #Returns:
    #    None.

    if len(sys.argv) < 3:
        print("Error: Please provide 2 arguments")
    else:
        arg_1 = sys.argv[1]
        arg_2 = sys.argv[2]

        print(f"first argument: {arg_1}")
        print(f"second argument: {arg_2}")

sys_out()

print("\n#-----------------------------------------------------#\n")

# Function to take user input and decrement using a while loop until the input
# becomes <= -1
def user_input_decrement():
    #Prints decremented user input.

    #Parameters:
    #    n (int):The user input to decrement. (Provided by user at run-time)

    #Returns:
    #    None. 

    try:
        n = int(input('Enter a number: '))   

        # Make a copy of the user input n since it's generally not a good
        # practise to modify function inputs
        n_copy = n
        
        while n_copy >= -1:
            n_copy -= 5
            print(n_copy)
    except:
        print("ERROR: Please type a number")

user_input_decrement()