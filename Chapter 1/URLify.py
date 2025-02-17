"""
URLify: Write a method to replace all spaces in a string with %20. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: If implementing in Java, please use a character array so that you can perform this operation in place.)
EXAMPLE
Input: 'Mr John Smith    ', 13
Output: 'Mr%20John%20Smith'
"""

def urlify(s, trueLength):
    s = list(s)
    idx = trueLength - 1
    i = len(s) - 1
    while idx >= 0:
        if s[idx] == ' ':
            s[i] = '0'
            s[i-1] = '2'
            s[i-2] = '%'
            i -= 3  
        else:
            s[i] = s[idx]
            i -= 1
        idx -= 1
    return ''.join(s)
