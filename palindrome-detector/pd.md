# Palindrome Detector

## Introduction

Palindrome is a word that has the same spelling when it is read backwards such as radar, tenet, noon, etc. 

In this activity, we are going to write a program that detects the palindrome and find out features of palindromic numbers. 

## Overview

### Step 1: Detecting Palindrome

Let's write a function called `is_palindrome` that tells whether the given word is a palindrome or not. 
To do this, the function will: 

* Generate a word that spells the given word backwards 
* Compare two words 
 
Then the program will return the result of the comparison as boolean. 

Use this starter code to begin: 
```py
def is_palindrome(word):
	# split the 'word' into a list of characters
    # generate a reversed 'word' with the list
	# compare the reversed word and the 'word'
	return # the result as boolean 

	# hint
    # list() splits the word into a list of characters 
    # methods from Code Along activity will help you with reversion
```

#### Solution

```py
def is_palindrome(word):
	characters = list(word)
	characters.reverse()
	reversed_word = ''.join(characters)
	if (reversed_word.lower() == word.lower()):
		return True
	else:
		return False
```
#### Test Code

If it makes sense for the activity to have test code you can provide the code here:

```py
print(is_palindrome("WoW"))
print(is_palindrome("palindrome"))
print(is_palimdrome("Hannah")) 
```
When you run the code, you should see the following on your screen: 

```py
True
False
True
```

### Step 2: Palindromic Perfect Square 

Did you know that numbers can be palindromes like `121`,`34543` as well? 

Now let’s find palindromic numbers that are a perfect square by writing a function `is_perfect_sq` that does:

* Check if the number is palindrome 
* Calculate the square root of the number
* Check if the number is a perfect square 

Then the program will return the result of calculation as boolean. 

Use this starter code to begin: 
```py
def is_perfect_sq(num):
	# check if the 'num' is palindrome using Step 1  
	# calculate the square root of the 'num'
	# check if the the 'num' is a perfect square 
	return # the result as boolean 

	# hints 
	# 'num' should be String to be run in 'is_palindrome'
	# square root can be written as to the power of 0.5
	# perfect square should always have their roots as integers
```
If needed, give additional instructions about writing expression that tells whether the number is integer or not

#### Solution

```py
def is_perfect_sq(num):
	if (is_palindrome(str(num)) == True):
		square_root = num ** 0.5
		if square_root % 1 == 0:
			return True
		else:
			return False
```

#### Test Code

If it makes sense for the activity to have test code you can provide the code here:

```py
print(is_perfect_sq(12321))
print(is_perfect_sq(67876))
print(is_perfect_sq(12345678987654321))
```

When you run the code, you should see the following on your screen: 

```py
True
False
True
```

### Step 3: Print Results 

Now let’s print the results in full sentences so that people who do not know what our program does can also easily understand the results. 

Using the code we wrote from Step 1 and 2, print the following statements:

```py 
“Is (word of your choice) palindrome?: (the result)”

“Is (number of your choice) palindrome?: (the result)”

“Is (number of your choice) palindromic perfect square?: (the result)”

# hint: String and Boolean can only be concatenated with commas.
```

#### Solution

```py
print("Is [word that student has chosen] palindrome?:" , is_palindrome("[word that student has chosen]"))
print("Is [number that student has chosen] palindrome?:" , is_palindrome("[number that student has chosen]"))
print("Is [number that student has chosen] palindromic perfect sqaure?:" , is_perfect_sq([number that student has chosen]))
```

## Conclusion

Congratulations! You successfully completed programming the Palindrome detector. 

(Pssst: actually... there is one fun fact about palindromic perfect squares hidden in the activity. Find this out by printing out the `square_root` of numbers!) 

For teachers:

The fun fact is that **Palindromic numbers starting from 1,2,3 and so on will always be a perfect square for series of 1.** 

* For example: 
* 12321 is a perfect square of 111
* 12345654321 is a perfect square of 111111
* 12345678987654321 is a perfect square of 111111111

Students can print out `square_root`of numbers by editing `is_perfect_sq(num)` as the following:

```py
def is_perfect_sq(num):
	if (is_palindrome(str(num)) == True):
		square_root = num ** 0.5
        print(square_root) #added line
		if square_root % 1 == 0:
			return True
		else:
			return False

```