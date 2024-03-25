def q0(s):
    out= ""
    print(f'{s} from q0 -> q1')
    if s == '1':
        out = 1 #going to q1
    else:
        out = 4 # to -> 4

    return out


def q1(s):
    out= ""
    print(f'{s} from q1 -> q2')
    if s == '0':
        out = 2 #going to q2
    else:
        out = 4 # to -> 4

    return out

def q2(s):
    out= ""
    print(f'{s} from q2 -> q3')
    if s == '1':
        out = 3 #going to q3
    else:
        out = 4 # to -> 4

    return out

def accept(string):
    seq = 0
    for i in string:
        if seq == 0:
            seq = q0(i)
        elif seq == 1:
            seq = q1(i)
        elif seq == 2:
            seq = q2(i)

    return seq

while True:
    strInput = input('Enter input: ')
    print(accept(strInput))
    if accept(strInput) == 3:
        print('Accepted')
    else:
        print('Rejected')
        
    choice = input("Try again? Y/N: ")
    if choice == 'N':
        break