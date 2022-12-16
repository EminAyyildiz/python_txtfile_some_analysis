


import sys
from collections import defaultdict

filename = input("Enter the name of the file:")
#input is taken from the user. The goal here is to ask the user on which file to operate.
output_file = open(filename, 'r')
#It opens the file entered in the input as output and reads it here.
lines = 0
words = 0
characters = 0
#Here we equalize the number of lines, characters, and words to 0 so that it does not make an incorrect count and does not give an error of definition.
for line in output_file :
    wordslist = line.split()
    lines = lines + 1
    words = words + len(wordslist)
    characters = characters + len(line)
print(lines)
print(words)
print(characters)
#Here, we find the number of words, lines and characters used with the for loop and print them to our screen.
