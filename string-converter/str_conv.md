# String Converter 

## Introduction

In this activity we're going to write two functions that convert the string input into different versions: the string with its vowels only and the string with their cases swapped. 

## Overview

### Step 1: Vowels Only

Let's start with writing a function called `vowelsOnly`that returns the vowels of the string input. In order to do so, we will:

* Define the function with the correct syntax
* Take a string input into the function using parameter
* Create a new string where we can store the vowels
* Compare each character of the string with vowels
* Add the character if it is a vowel
* Return the new string 

#### Solution

```py
def vowelsOnly(input_string):
    vowel_string = ""
    for char in input_string:
        if char.lower() in "aeiou":
            vowel_string += char
    return vowel_string
```
#### Test Code

If it makes sense for the activity to have test code you can provide the code here:

```py
print(vowelsOnly("meow"))
```
When you run the code, you should see the following on your screen: 

```py
eo
```

### Step 2: Swapped case

Now let's write a function called `get_winner()` which will return the string where its cases are swapped. To complete this, we will:

* Define the function with the correct syntax
* Take a string input into the function using parameter
* Create a new string where we can store the case-swapped string
* Go through the each character and swap its case
* Store the swapped character to the new string
* Return the new string

#### Solution

```py
def swapCase(input_string):
    swapped_string = ""
    for char in input_string:
        if char.islower(): 
            swapped_string += char.upper() 
        elif char.isupper(): 
            swapped_string += char.lower()
    return swapped_string
```

#### Test Code

If it makes sense for the activity to have test code you can provide the code here:

```py
print(swapCase("I LOVE cats"))
```

When you run the code, you should see the following on your screen: 

```py
i love CATS
```

### Step 3: Adding Input

Since we want to convert the string input, let's replace `meow` and `I LOVE cats` to input statements. We will have to: 

* Assign `string_input` to an input statement 
* Write print statements showing two converted versions of the string input 

#### Solution

```py
string_input = input("Enter a string: ")

print("Vowels: ", vowelsOnly(string_input))
print("Swapped String: ", swapCase(string_input))
```

## Conclusion

There you have your own String Converter! Test your program by giving different string inputs. 