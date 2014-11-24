#!/usr/bin/env python

def main():
	test_word = raw_input("Please enter a word containing only letters in the word 'facebook': ")
	print book_counter(test_word)

def book_counter(input_word):
	facebook = []
	refill_count = 0
	inventory = []
	input_word = input_word.upper()
	for current_letter in input_word:		
		if current_letter in inventory:
			inventory.remove(current_letter)
		else:
			refill_count = refill_count + 1
			inventory.extend(["F","A","C","E","B","O","O","K"])
	return refill_count


if __name__ == '__main__':
	main()