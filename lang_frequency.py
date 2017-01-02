import re
import collections
def get_data(path):
	starter_text = open(path, 'r').read()
	return starter_text
def word_freq(starter_text):
	changed_text = re.sub(r'[;:,\.\(\)\'\"\?\!\-\n]', ' ', starter_text) # swapping punctuation marks with spaces;
	changed_text = changed_text.lower()
	splitted_words = re.split(r' ', changed_text)
	splitted_words = [x for x in splitted_words if x != ''] # creating word list, deleting excess spaces; 
	common_words = collections.Counter(splitted_words).most_common(10) 
	return common_words
a = input(str())
text = get_data(a)
print(word_freq(text))
input('Press enter to continue...')
