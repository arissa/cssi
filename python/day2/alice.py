#! /usr/bin/python
#
# A program to analyze the text of Alice in Wonderland and do
# interesting things with the data.
import string
def GetUniqueWords(text):
	#text_without_punctuation = text.strip()

	words = text.lower().split()
	for word in words:
		word = word.strip(string.punctuation)
		word = word.strip(string.punctuation)
		word = word.strip(string.punctuation)

	unique_words = set(words)
	return unique_words


def main():
  # Open the file, read it into memory as a single string.
  with open('alice_in_wonderland.txt') as alice_file:
    alice_text = alice_file.read()

  print 'Unique words:', GetUniqueWords(alice_text)
  print len(GetUniqueWords(alice_text))

if __name__ == '__main__':
  main()