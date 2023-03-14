#Python Program to Find Vowels From a String
#defining a function

def get_vowels(String):
    return [each for each in String if each in "aeiou"]
get_string1 = "hello" # ['e', 'o']
get_string2 = "python is fun" # ['o', 'i', 'u']
get_string3 = "coding compiler" 
get_string4 = "12345xyz" 



print("The Vowels Are:  ",get_vowels(get_string1))

print("The Vowels Are:  ",get_vowels(get_string2))

print("The Vowels Are:  ",get_vowels(get_string3))

print("The Vowels Are:  ",get_vowels(get_string4))

