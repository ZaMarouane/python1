####################
#This script counts how many characters are in a given word or sentence.
#Author: Marouane
#date: 3/05/2024
###################

import time

word = input("Enter a word or sentence: ")
letter = input("Enter the character you want to count: ")
count = 0
for i in word:
    if i == letter:
        count += 1  # This increase the var count by 1 each time i == letter

print("Calculating")
time.sleep(2)

print(f'there are {count} "{letter}" in "{word}"')
