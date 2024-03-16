#Project 1 for CS 341
#Section number: 010
#Semester: Spring 2024
#Written by: Kaitlyn Gaston, kg33
#Instructor: Marvin Nakayama, marvin@njit.edu

import string
import sys

#lowercase alphabet to reference to
alphabet = set(string.ascii_lowercase)

#starting state q1
def q1_g33(email, index):
    print("State: q1")
    #kicks out if the index is longer than the email length
    if index >= len(email):
        return False
    char = email[index]
    print("Character: " + char)
    #reads in next character
    index += 1
    if char in alphabet:
        return q2_g33(email, index)
    else: #trap state
        return q9_g33(email, index)

#state q2
def q2_g33(email, index):
    print("State: q2")
    if index >= len(email):
        return False
    char = email[index]
    print("Character: " + char)
    index += 1
    if char in alphabet: #loops into itself
        return q2_g33(email, index)
    elif char == ".": #goes back to q1
        return q1_g33(email, index)
    elif char == "@": #breaks loop
        return q3_g33(email, index)
    else: #any other character invalid/not in alphabet
        return q9_g33(email, index)

#state q3
def q3_g33(email, index):
    print("State: q3")
    if index >= len(email):
        return False
    char = email[index]
    print("Character: " + char)
    index += 1
    if char in alphabet: #much like q1 there must be at least one character in alphabet
        return q4_g33(email, index)
    else: #enters trap state if there is double @
        return q9_g33(email, index)

#state q4
def q4_g33(email, index):
    print("State: q4")
    if index >= len(email):
        return False
    char = email[index]
    print("Character: " + char)
    index += 1
    if char in alphabet: #loops like q2
        return q4_g33(email, index)
    elif char == ".": #progresses to q5, may be .gov or .gr
        return q5_g33(email, index)
    else:
        return q9_g33(email, index)

#state q5
def q5_g33(email, index):
    print("State: q5")
    if index >= len(email):
        return False
    char = email[index]
    print("Character: " + char)
    index += 1
    if char == "g": #may be part of .gov or .gr
        return q6_g33(email, index)
    elif char in alphabet: #not part of .gov or .gr, returns to q4
        return q4_g33(email, index)
    else: #trap state for ..
        return q9_g33(email, index)

#state q6
def q6_g33(email, index):
    print("State: q6")
    if index >= len(email):
        return False
    char = email[index]
    print("Character: " + char)
    index += 1
    if char == "o": #.go
        return q7_g33(email, index)
    elif char == "r": #.gr, moves to accepting state
        return q8_g33(email, index)
    elif char in alphabet: #resets to q4
        return q4_g33(email, index)
    elif char == ".": #goes to q5, may be part of S2
        return q5_g33(email, index)
    else:
        return q9_g33(email, index)

#state q7
def q7_g33(email, index):
    print("State: q7")
    if index >= len(email):
        return False
    char = email[index]
    print("Character: " + char)
    index += 1
    if char == "v": #detects .gov and moves to accepting state
        return q8_g33(email, index)
    elif char in alphabet: #resets to q4
        return q4_g33(email, index)
    elif char == ".": #goes to q5, may be part of S2
        return q5_g33(email, index)
    else:
        return q9_g33(email, index)

#accepting state q8
def q8_g33(email, index):
    print("State: q8")
    if index > len(email): #out of bounds
        return False
    elif index == len(email): #done reading characters so returns True
        return True
    else:
        char = email[index]
        print("Character: " + char)
        index += 1
    if char in alphabet:
        return q4_g33(email, index)
    elif char == ".":
        return q5_g33(email, index)
    else:
        return q9_g33(email, index)

#trap state q9
def q9_g33(email, index):
    print("State: q9")
    if index >= len(email):
        return False
    char = email[index]
    print("Character: " + char)
    index += 1
    for i in range(index, len(email)): #loops until end of string to show it is trapped
        print("State: q9")
        char = email[i]
        print("Character: " + char)
    print("State: q9")
    return False

#DFA function that starts the process
def DFA_g33(email):
    return q1_g33(email, 0)

#use the below comments to write to an output.txt file
#sys.stdout = open('output.txt', 'w')
print("Project 1 for CS 341\nSection number: 010\nSemester: Spring 2024\nWritten by: Kaitlyn Gaston, kg33\nInstructor: Marvin Nakayama, marvin@njit.edu\n")
n = int(input("Enter an integer >= 0 specifying the number of strings to be processed: ")) #user input
print("\nn =", n)
if n > 0:
    for i in range(n): #runs through all strings
        print()
        currString = input("Enter string {} of {}: ".format(i+1, n))
        print("\n"+currString)
        if DFA_g33(currString):
            print("Valid email: " + currString)
        else:
            print("Invalid email: " + currString)
else:
    print("No strings to process.")
#sys.stdout.close()
