def binary_to_decimal(num):
    binary_str = str(num)
    decimal_num = 0
    power = len(binary_str) - 1
    for bit in binary_str:
        if bit == '1':
            decimal_num = decimal_num + (2 ** power)
        power -= 1
    return decimal_num

def num_to_ASCII(num): 
	char = chr(num)
	return char

# students can replace 1000001 to the number of their choice. 
print(1000001, "is", binary_to_decimal(1000001), "in decimal.")
print("Binary number", 1000001, "represents", num_to_ASCII(binary_to_decimal(1000001)), "in ASCII.")