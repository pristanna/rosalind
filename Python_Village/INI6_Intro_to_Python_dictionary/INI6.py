# Nice (but different) solution with flowchart and code execution visualization: https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-12.php

# Open input file for reading
fin = open("rosalind_ini6.txt", "r")

# Openfile for writing - if the file already exist, delete it and create again
fout = open("rosalind_ini6.out.txt", "w")

# Read a content of the file
s = fin.read()

# Get rid of end of line \n
s = s.strip()

# Convert the string into the list - otherwise the count method on string is searching for all substrings
# I need to count just exact matches of whole words which is done by method count on lists
list = s.split(' ')

# Create an empty dictionary
dict={}

# Cycle to count frequency of each word from the list
for word in list:

    dict[word] = list.count(word) # Count number of occurences of the word and append it to the dictionary

# Getting the output as I desire using items method
for key, value in dict.items():
    fout.write(key + " " + str(value) + "\n")

fin.close()
fout.close()
