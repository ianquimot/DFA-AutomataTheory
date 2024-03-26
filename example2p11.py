# Example 2.11 Draw a DFA that recognizes the set of all strings starting with prefix ab with alphabets from ∑ = {a. b}. 

def dfa_accept(input_string):
    state = 0
    for char in input_string:
        if char == 'a':
            if state == 0:
                state = 1
            elif state == 2:
                state = 2
            elif state == 3:
                state = 3

        elif char == 'b':
            if state == 0:
                state = 3
            elif state == 1:
                state = 2
            elif state == 3:
                state = 3

    return state == 2

# Test the DFA
while True:
    input_string = input("Enter input string: ")
    if dfa_accept(input_string):
        print("Accepted")
    else:
        print("Rejected")

    choice = input('Try Again? Y/N: ')
    if choice == 'N':
        break