#!/usr/bin/env python

import operator

def main():
  print word_count()

def word_count():
  word_totals = {
	
}

  book_contents = f.read()
  book_contents = book_contents.replace('\n', ' ')
  book_contents = book_contents.replace(',', '')
  book_contents = book_contents.replace('.', '')
  book_contents = book_contents.replace('"', '')

  book_split = book_contents.split(' ')
  for word in book_split:
  	if word not in word_totals:
  		word_totals[word] = 1
	word_totals[word] += 1
  word_totals = sorted(word_totals.items(), key=operator.itemgetter(1))
  return word_totals



f = open('rob-book.txt','r')

if __name__ == '__main__':
  main()