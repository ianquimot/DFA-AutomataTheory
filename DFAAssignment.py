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


#Description:
    #The given code defines a function automate(s) that takes a string s as input and checks whether the first three characters of the string satisfy certain conditions. If the first three characters satisfy the conditions, the function returns "Accepted"; otherwise, it returns "Rejected".
    #Parameters:
    #Alphabet: The alphabet of the DFA consists of the characters '0' and '1'.
    #States: The DFA doesn't explicitly define states. Instead, it directly checks the input string based on certain conditions.
    
# Explanation:
    # The DFA starts at the "Start" state and moves to the "Check 2nd" state if the first character is '1'.
    # In the "Check 2nd" state, if the second character is '0', it moves to the "Check 3rd" state.
    # In the "Check 3rd" state, if the third character is '1', it checks the remaining characters to ensure they are all '1's. If all remaining characters are '1's, the DFA accepts the input string; otherwise, it rejects the input string.
    # If any of the conditions are not met (e.g., the first character is not '1', the second character is not '0', or the third character is not '1'), the DFA immediately rejects the input string.
    # This DFA accepts input strings that start with '1', followed by '0', followed by '1', and then any number of '1's afterwards. Otherwise, it rejects the input string.