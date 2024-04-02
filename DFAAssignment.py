def automate(s):
    if len(s)<3:
        return "Rejected"

    if s[0] == '1':
        if s[1] == '0':
            if s[2] == '1':
                for i in range(3, len(s)):
                    if s[i] != '1':
                        return "Rejected" #This line iterates over the characters of the input string s starting from index 3 (the fourth character) till the end. It checks if any character other than '1' is encountered in this range. If any character other than '1' is found, it returns "Rejected".
                return "Accepted" #If the loop completes without finding any non-'1' characters, it means that all characters beyond the third position are '1's. In this case, the function returns "Accepted", indicating that the input string satisfies the specified conditions.
            return "Rejected" #If the second character of the input string s is not '0', it implies that the specified condition is not met, and the function returns "Rejected".
        return "Rejected" #If the first character of the input string s is not '1', it implies that the specified condition is not met, and the function returns "Rejected".
    
    
    return "Rejected" #This line serves as a default return statement. If none of the previous conditions are met, it means the input string does not satisfy the specified conditions, and the function returns "Rejected".

inputs=['1', '10101', '101', '10111', '01010',"010011","10011111","101111"]
for i in inputs:
    print(automate(i))