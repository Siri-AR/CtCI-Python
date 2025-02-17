# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

# With additional data structure(set)
def isUnique1(str):
  if len(set(str))==len(str):
    return True
  else:
    return False

# Without additional data structure
def isUnique2(str):
  for i in range(len(str)-1):
    for j in range(i+1, len(str)):
      if s[i]!=s[j]:
        return True
  return False

# Optimized without additional data structure
def isUnique3(str):
    bitmask = 0  # Bitmask to track characters
    for char in str:
        bit_index = ord(char) - ord('a')  
        if bitmask & (1 << bit_index): 
            return False
        bitmask |= (1 << bit_index)  
    return True
