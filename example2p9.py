def dfa_accept(input_string):
    state = 0  # Initial state where both counts are even
    for char in input_string:
        if char == '0':
            if state == 0:
                state = 1
            elif state == 1:
                state = 0
            elif state == 2:
                state = 3
            elif state == 3:
                state = 2
        elif char == '1':
            if state == 0:
                state = 2
            elif state == 1:
                state = 3
            elif state == 2:
                state = 0
            elif state == 3:
                state = 1

    # Accept only if the final state is 0
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