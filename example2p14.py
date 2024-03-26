# Example 2.14 Design a DFA that contains 001 as substring in all strings over ∑ = {0, 1}.

def dfa_accept(input_string):
    state = 0
    for char in input_string:
        if char == '0':
            if state == 0:
                state = 1
            elif state == 1:
                state = 2
            elif state == 2:
                state = 2
            elif state == 3:
                state = 3

        
        elif char == '1':
            if state == 0:
                state = 0
            elif state == 1:
                state = 0
            elif state == 2:
                state = 3
            elif state == 3:
                state = 3

    return state == 3

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