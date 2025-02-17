# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

from collections import Counter
def checkPermutation1(str1, str2):
    # If the lengths are different, they can't be permutations of each other
    if len(str1) != len(str2):
        return False
    # Count the frequency of characters in both strings
    return Counter(str1) == Counter(str2)


def checkPermutation2(s1, s2):
  if len(s1)!=len(s2):
    return False
  
  count = [0] * 26
  
  for char in str1:
    count[ord(char) - ord('a')] += 1  
  for char in str2:
      count[ord(char) - ord('a')] -= 1 
  
  return all(c == 0 for c in count)
