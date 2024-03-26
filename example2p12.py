# Example 2.12 Design a DFA that accepts even number of a’s over ∑ = {a}.

def dfa_accept(input_string):
    state = 0
    for char in input_string:
        if char == 'a':
            if state == 0:
                state = 1
            elif state == 1:
                state = 0
        
        elif char != 'a':
            return False
        

    return state == 0


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
