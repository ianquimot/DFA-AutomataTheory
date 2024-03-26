# Example 2.13 DFA that accepts odd number of 1’s on {0, 1}.

def dfa_accept(input_string):
    state = 0
    for char in input_string:
        if char == '1':
            if state == 0:
                state = 1
            elif state == 1:
                state = 0
        
        elif char == '0':
            if state == 0:
                state = 0
            elif state == 1:
                state = 1

    return state == 1


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