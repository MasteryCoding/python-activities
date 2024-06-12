def write_journal():
	date = input("Enter the date of the journal: ")
	open(date,'x')
	
	content = input("Enter the content of the journal: ")
	with open(date,'w') as file:
		file.write(content) 
	
def read_journal():
	date = input("Enter the date: ")
	with open(date,'r') as file:
	    print(file.read())

keyword = input("Choose a keyword r(read) /w(write) /c(close): ")

while (keyword != "c"):
	if(keyword == "r"):
		read_journal()
	elif(keyword == "w"):
		write_journal()
	else:
		print("Chose a wrong keyword.")
	keyword = input("Choose a keyword r(read) / w(write) / c(close): ")