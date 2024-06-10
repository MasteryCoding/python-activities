# Binary to ASCII

## Introduction

In this activity we're going to write a program that converts binary number to decimal number and convert number to its corresponding ASCII character. Then we will print statements converting binary numbers to ASCII characters through the program we wrote.

## Overview

### Step 1: Binary to Decimal

Let's start with writing a function called `binary_to_decimal`, which will do the following:

* Convert the data type of input to String 
* Find the largest power the input holds
*(Hint: The largest power of binary number is 1 less than the digit position of its largest bit)*
* Find the coressponding decimal value of each bit of the input
* Sum up the values to the variable storing decimal representation 

Then we will return the decimal number of the input.

You can start writing codes using this starter code: 
```py
def binary_to_decimal(num):
    # convert 'num' to String
	# create a variable to store the result
	# find the largest power 'num' holds 
    # find the corresponding decimal value of each bit of 'num'
    # sum it up to the result variable 
	return # the result variable
```


#### Solution

```py
def binary_to_decimal(num):
    binary_str = str(num)
    decimal_num = 0
    power = len(binary_str) - 1
    for bit in binary_str:
        if bit == '1':
            decimal_num = decimal_num + (2 ** power)
        power -= 1
    return decimal_num
```
#### Test Code

If it makes sense for the activity to have test code you can provide the code here:

```py
print(binary_to_decimal(1100))
print(binary_to_decimal(1110110))
print(binary_to_decimal(10))
```
When you run the code, you should see the following on your screen: 

```py
12
118
2
```

### Step 2: Number to ASCII Character 

Now let's write a function called `num_to_ASCII` which will return the ASCII character that corressponds to the input:

Here is the starter code you can begin with: 
```py
def num_to_ASCII(num): 
	# find num's ASCII character 
	return # the character 
```

#### Solution

```py
def num_to_ASCII(num): 
	char = chr(num)
	return char
```

#### Test Code

If it makes sense for the activity to have test code you can provide the code here:

```py
print(num_to_ASCII(80))
print(num_to_ASCII(89))
print(num_to_ASCII(84))
print(num_to_ASCII(72))
print(num_to_ASCII(79))
print(num_to_ASCII(78))
print(num_to_ASCII(33))
```

When you run the code, you should see the following on your screen: 

```py
P
Y
T
H
O
N
!
```

### Step 3: Print Statements

Using functiosn we wrote in Step 1 and 2, let's print the following statements: 

* `(Binary number of your choice) is (the number’s decimal number) in decimal`
* `Binary number (binary number of your choice) represents (number’s corresponding ASCII character) in ASCII`
* Note that alphabets corresponds to 65(**1000001** in binary) through 122(**1111010**) in ASCII 



#### Solution

```py
print([number that student has chosen], "is", binary_to_decimal(num), "in decimal.")
print("Binary number ", [number that student has chosen], "represents ", num_to_ASCII(binary_to_decimal(num)), "in ASCII.")
```

## Conclusion

Now you can convert binary numbers easily with the program we just wrote! 
You can also try creating a secret message using binary number and ASCII characters. 