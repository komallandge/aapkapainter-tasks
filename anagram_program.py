# Write a code that checks if two given strings are anagrams
# Sample Input: Mary Army
# Output: Yes

def is_anagram(s1, s2):
    if len(s1) == len(s2):
        for s in s1:
            if s not in s2:
                return False
        return True
    return False


print(is_anagram("mary", "army"))