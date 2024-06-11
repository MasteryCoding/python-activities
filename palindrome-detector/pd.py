def is_palindrome(word):
	characters = list(word)
	characters.reverse()
	reversed_word = ''.join(characters)
	if (reversed_word.lower() == word.lower()):
		return True
	else:
		return False
	
def is_perfect_sq(num):
	if (is_palindrome(str(num)) == True):
		square = num ** 0.5
		if square % 1 == 0:
			return True
		else:
			return False
		
# students can replace 'radar' and '12321' to the word and number of their choice.
print("Is radar palindrome?:" , is_palindrome("radar"))
print("Is 13531 palindrome?:" , is_palindrome("13531"))
print("Is 13531 palindromic perfect sqaure?:" , is_perfect_sq(13531))