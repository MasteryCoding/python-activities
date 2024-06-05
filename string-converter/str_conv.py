def vowelsOnly(input_string):
    vowel_string = ""
    for char in input_string:
        if char.lower() in "aeiou":
            vowel_string += char
    return vowel_string
    
def swapCase(input_string):
    swapped_string = ""
    for char in input_string:
        if char.islower(): 
            swapped_string += char.upper() 
        elif char.isupper(): 
            swapped_string += char.lower()
    return swapped_string
    
string_input = input("Enter a string: ")
print("Vowels: " , vowelsOnly(string_input))
print("Swapped String: " , swapCase(string_input))