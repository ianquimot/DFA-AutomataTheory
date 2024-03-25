# Example 2.10: Design a DFA that accepts all the strings with at most 3 a’s

def dfa_accept(input_string):
    state = 0  # Initial state
    for char in input_string:
        if char == 'a':
            if state < 3:  # Accept 'a' only if less than 3 'a's encountered
                state += 1
            else:
                state = 4  # More than 3 'a's encountered, transition to reject state
        elif char != 'b':
            return False  # Reject if input contains any other character

    # Accept if final state is 0, 1, 2, or 3
    return state != 4

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
