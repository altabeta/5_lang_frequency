import re
import collections
def get_filepath():
	a = input(str())
	return a
def word_freq(path):
	starterText = open(path, 'r').read()
	changedText = re.sub(r'[;:,\.\(\)\'\"\?\!\-\n]', ' ', starterText)
	changedText = changedText.lower()
	splittedWords = re.split(r' ', changedText)
	splittedWords = [x for x in splittedWords if x != '']
	commonWords = collections.Counter(splittedWords).most_common(10)
	return commonWords
a = get_filepath()
print(word_freq(a))
input('Press enter to continue...')
