#Python Program to Find Vowels From a String
#defining a function

def get_vowels(String):
    return [each for each in String if each in "aeiou"]
get_string1 = "hello" # ['e', 'o']
get_string2 = "python is fun" # ['o', 'i', 'u']
get_string3 = "coding compiler" # ['o', 'i', 'o', 'i', 'e']
get_string4 = "12345xyz" # []


#Let's print vowels from the given strigns
#Vowels from first string

#Vowels from second string
print("The Vowels Are:  ",get_vowels(get_string1))

#Vowels from third string
print("The Vowels Are:  ",get_vowels(get_string2))

print("The Vowels Are:  ",get_vowels(get_string3))

print("The Vowels Are:  ",get_vowels(get_string4))

