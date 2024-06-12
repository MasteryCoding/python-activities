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

    # hints:
    # with() keyword automatically closes the file after running the code
```

#### Solution

```py
def write_journal():
	date = input("Enter the date of the journal: ")
	open(date,'x')
	
	content = input("Enter the content of the journal: ")
	with open(date,'w') as file:
		file.write(content) 
```

#### Test Code

If it makes sense for the activity to have test code you can provide the code here:

```py
write_journal()
```
When you run the code, you should see the file named as the date you chose and the content you wrote inside the file. 

Note: Your journal name should not include slash(`/`) since it will cause an FileNotFound error 

### Step 2: Read Journal

Now let's write a function called `read_journal` which will show us the content of the journal we chose by doing the following: 

* Take a date as an input
* Open a journal file that has a name matching the input 
* Output the content of the journal 

Here is the starter code you can begin with: 
```py
def read_journal():
	# assign date as an input
	# open a file with a name matching the date 
	# read the content of the file
	# print the content 
    # close the file
```

#### Solution

```py
def read_journal():
	date = input("Enter the date: ")
	with open(date,'r') as file:
	    print(file.read())
```

#### Test Code

If it makes sense for the activity to have test code you can provide the code here:

```py
read_journal()
```

When you run the code, try running it with the file you created from Step 1. 
You should see the content of the file as an output. 

### Step 3: Finalize the program

To use two functions in our program, let’s make a feature that will allow us to choose between reading, writing, and closing a journal. We will:

* Take a keyword of each function as an input 
* Run the function that corresponds to the keyword 
* Output the error message if wrong keyword is taken as an input
* Ask for a keyword iteratively until we close the journal

#### Solution

```py
keyword = input("Choose a keyword r(read) / w(write) / c(close): ")

while (keyword != "c"):
	if (keyword == "r"):
		read_journal()
	elif (keyword == "w"):
		write_journal()
	else:
		print("Wrong Keyword")
	keyword = input("Choose a keyword r(read) / w(write) / c(close): ")
```
(Keywords of students' choice do not have to match with those from the solution.)

## Conclusion

There you have your own digital journal! 
Try it out by writing journals and reading them. 