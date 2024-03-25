#Project 2 for CS 341
#Section number: 010
#Semester: Spring 2024
#Written by: Kaitlyn Gaston, kg33
#Instructor: Marvin Nakayama, marvin@njit.edu

import string
import sys

#alphabets to refer to
numbers = {'0','1','2','3','4','5','6','7','8','9'}
operators = {'+','-','*','/'}

#stack, append to push, pop to pop
stack = []

#starting state q1
def q1_g33(string, index):
    print("State before transition: q1")
    #kicks out if the index is longer than the string length
    if index >= len(string):
        return False
    char = string[index]
    stack.append(char)
    print("Read in symbol: " + char + "\tPopped: nothing" + "\tPushed: " + char)
    #iterates to next index
    index += 1
    if char == 'a':
        print("State after transition: q2")
        return q2_g33(string, index)
    else:
        print("PDA crashes in q1")
        return False

#state q2
def q2_g33(string, index):
    print("State before transition: q2")
    #kicks out if the index is longer than the string length
    if index >= len(string):
        return False
    char = string[index]
    #iterates to next index
    index += 1
    if char == 'b':
        stack.append(char)
        print("Read in symbol: " + char + "\tPopped: nothing" + "\tPushed: " + char)
        print("State after transition: q2")
        return q2_g33(string, index) #loops onto itself
    elif char == 'a':
        stack.append(char)
        print("Read in symbol: " + char + "\tPopped: nothing" + "\tPushed: " + char)
        print("State after transition: q3")
        return q3_g33(string, index) #moves onto q3 when it encounters an a
    else:
        print("PDA crashes in q2")
        return False

#state q3
def q3_g33(string, index):
    print("State before transition: q3")
    #kicks out if the index is longer than the string length
    if index >= len(string):
        return False
    char = string[index]
    #iterates to next index
    index += 1
    if char in numbers:
        stack.append(char)
        print("Read in symbol: " + char + "\tPopped: nothing" + "\tPushed: " + char)
        print("State after transition: q4")
        return q4_g33(string, index) #appends a number to be popped later upon reaching a .
    elif char == '.':
        print("Read in symbol: " + char + "\tPopped: nothing" + "\tPushed: nothing")
        print("State after transition: q4")
        return q4_g33(string, index) #push not necessary here
    elif char == '(': #optional ( loops onto itself if present, not required for all strings
        stack.append(char)
        print("Read in symbol: " + char + "\tPopped: nothing" + "\tPushed: " + char)
        print("State after transition: q3")
        return q3_g33(string, index)
    else:
        print("PDA crashes in q3")
        return False

#state q4
def q4_g33(string, index):
    print("State before transition: q4")
    #kicks out if the index is longer than the string length
    if index >= len(string):
        return False
    char = string[index]
    #iterates to next index
    index += 1
    if char == '.':
        if(stack[-1] in numbers): #checks that the top of the stack is a number
            print("Read in symbol: " + char + "\tPopped: " + stack[-1] + "\tPushed: nothing")
            stack.pop()
            print("State after transition: q5")
            return q5_g33(string, index) #pops the number on top of the stack, ensuring that all numbers have to have one decimal point
        else:
            print("PDA crashes in q4")
            return False
    elif char in numbers:
        print("Read in symbol: " + char + "\tPopped: nothing" + "\tPushed: nothing")
        print("State after transition: q5")
        return q5_g33(string, index) #handles multiple numbers before and after .
    else:
        print("PDA crashes in q4")
        return False

#state q5
def q5_g33(string, index):
    print("State before transition: q5")
    #kicks out if the index is longer than the string length
    if index >= len(string):
        return False
    char = string[index]
    #iterates to next index
    index += 1
    if char == 'a':
        if(stack[-1] == 'a'):
            print("Read in symbol: " + char + "\tPopped: " + char + "\tPushed: nothing")
            stack.pop()
            print("State after transition: q8")
            return q8_g33(string, index) #ensures a match to the first 'a' character in the string
        else:
            print("PDA crashes in q5")
            return False
    elif char == '.':
        if(stack[-1] in numbers):
            print("Read in symbol: " + char + "\tPopped: " + stack[-1] + "\tPushed: nothing")
            stack.pop()
            print("State after transition: q5")
            return q5_g33(string, index) #decimal point for multiple numbers before it, such as 55.
        else:
            print("PDA crashes in q5")
            return False
    elif char == ')':
        if(stack[-1] == '('):
            print("Read in symbol: " + char + "\tPopped: " + stack[-1] + "\tPushed: nothing")
            stack.pop()
            print("State after transition: q6")
            return q6_g33(string, index) #new state to handle ) followed by operation as well as matching parantheses
        else:
            print("PDA crashes in q5")
            return False
    elif char in numbers:
        print("Read in symbol: " + char + "\tPopped: nothing" + "\tPushed: nothing")
        print("State after transition: q5")
        return q5_g33(string, index) #repeating numbers before or after .
    elif char in operators:
        print("Read in symbol: " + char + "\tPopped: nothing" + "\tPushed: nothing")
        print("State after transition: q7")
        return q7_g33(string, index) #operation state
    else:
        print("PDA crashes in q5")
        return False

#state q6
def q6_g33(string, index):
    print("State before transition: q6")
    #kicks out if the index is longer than the string length
    if index >= len(string):
        return False
    char = string[index]
    #iterates to next index
    index += 1
    if char == ')':
        if(stack[-1] == '('):
            print("Read in symbol: " + char + "\tPopped: " + stack[-1] + "\tPushed: nothing")
            stack.pop()
            print("State after transition: q6")
            return q6_g33(string, index) #checks that every parantheses has a match
        else:
            print("PDA crashes in q6")
            return False
    elif char in operators:
        print("Read in symbol: " + char + "\tPopped: nothing" + "\tPushed: nothing")
        print("State after transition: q7")
        return q7_g33(string, index) #handles )operator
    elif char == 'a':
        if(stack[-1] == 'a'):
            print("Read in symbol: " + char + "\tPopped: " + char + "\tPushed: nothing")
            stack.pop()
            print("State after transition: q8")
            return q8_g33(string, index) #handles )a
        else:
            print("PDA crashes in q6")
            return False
    else:
        print("PDA crashes in q6")
        return False

#state q7
def q7_g33(string, index):
    print("State before transition: q7")
    #kicks out if the index is longer than the string length
    if index >= len(string):
        return False
    char = string[index]
    #iterates to next index
    index += 1
    if char == '(':
        stack.append('(')
        print("Read in symbol: " + char + "\tPopped: nothing" + "\tPushed: " + char)
        print("State after transition: q3")
        return q3_g33(string, index) #handles operator(
    elif char in numbers:
        stack.append(char)
        print("Read in symbol: " + char + "\tPopped: nothing" + "\tPushed: " + char)
        print("State after transition: q4")
        return q4_g33(string, index) #operand
    elif char == '.':
        print("Read in symbol: " + char + "\tPopped: nothing" + "\tPushed: nothing")
        print("State after transition: q4")
        return q4_g33(string, index) #operand
    else:
        print("PDA crashes in q7")
        return False

#state q8
def q8_g33(string, index):
    print("State before transition: q8")
    #kicks out if the index is longer than the string length
    if index >= len(string):
        return False
    char = string[index]
    #iterates to next index
    index += 1
    if char == 'b':
        if(stack[-1] == 'b'):
            print("Read in symbol: " + char + "\tPopped: " + stack[-1] + "\tPushed: nothing")
            stack.pop()
            print("State after transition: q8")
            return q8_g33(string, index) #loops onto itself
        else:
            print("PDA crashes in q8")
            return False
    elif char == 'a':
        if(stack[-1] == 'a'):
            print("Read in symbol: " + char + "\tPopped: " + stack[-1] + "\tPushed: nothing")
            stack.pop()
            print("State after transition: q9")
            return q9_g33(string, index) #moves to accepting state
        else:
            print("PDA crashes in q8")
            return False
    else:
        print("PDA crashes in q8")
        return False

#accepting state q9
def q9_g33(string, index):
    #accept state
    if index == len(string): #last element
        print("Reached accept state")
        return True
    else: #uneven a's or b's
        print("PDA crashes in q9")
        return False

#PDA function that starts the process
def PDA_g33(string):
    return q1_g33(string, 0)

#use the below comments to write to an output.txt file
#sys.stdout = open('output.txt', 'w')
print("Project 2 for CS 341\nSection number: 010\nSemester: Spring 2024\nWritten by: Kaitlyn Gaston, kg33\nInstructor: Marvin Nakayama, marvin@njit.edu\n")
n = int(input("Enter an integer >= 0 specifying the number of strings to be processed: ")) #user input
print("\nn =", n)
if n > 0:
    for i in range(n): #runs through all strings
        print()
        currString = input("Enter string {} of {}: ".format(i+1, n))
        print("\n"+currString)
        if PDA_g33(currString):
            print("Accepted: " + currString)
        else:
            print("Rejected: " + currString)
else:
    print("No strings to process.")
#sys.stdout.close()
