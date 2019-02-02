# Write a python program to count number of words and characters in a file for each line and then print the output.
# Input: a file includes two line
# Python Course
# Deep learning class
# Output:
# Python Course --- “word”: 2, “letter”: 12
# Deep Learning class --- “word”: 3, “letter”: 17

file_name = input("What file contains our desired string? : ")      # instruct user to input file name

infile = open(file_name, 'r')       # opens desired file

word = 1        # there will be at least one word in the line; a space (in while loop) will indicate an additional word
letter = 0 - word   # set letters to 0

line = infile.readline()    # reads first line of file

while line != "":       # reads line in text until a blank spaces occurs in the text file

    for x in line:
        if x == " ":        # if there is a blank space word count increases by one
            word = word + 1
        else:               # if there is no blank space, assume that character is a letter and increase letter by one
            letter = letter + 1

    print(line, "--->", "word:", word, "letter:", letter)

    # reset letter and word count for next loop
    word = 1
    letter = 0

    line = infile.readline()
