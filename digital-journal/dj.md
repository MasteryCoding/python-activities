# Digital Journal

## Introduction

In this activity we will write a digital journal program where we can read and write journals by handling files. 

## Overview

### Step 1: Write Journal

Let’s start by creating a function called `write_journal()` that will allow us to write a digital journal. 
In order to do so, we will: 

* Take a date as an input 
* Create a journal file named as the date input 
* Write the content on the journal 
* Close the journal 

You can start writing the function using this starter code: 
```py
def write_journal():
	# assign date as an input 
	# create a file named as the date 
	# assign content as an input
	# write the content on the file 
	# close the file  

    # hints
```

If needed, give additional instruction to students about steps to find the decimal value:
1. Starting from the highest bit, multiply the corresponding power of 2 IF the bit is holding 1 as its binary value 
2. Decrement the power by 1 and move to the second highest bit 
3. Iterate step 1 and 2 until the lowest bit is reached

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

    # hint: 
    # methods from Code Along activity can help you with the conversion
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