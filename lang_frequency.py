import re
import collections
def get_data(path):
	starterText = open(path, 'r').read()
	return starterText
def word_freq(starterText):
	changedText = re.sub(r'[;:,\.\(\)\'\"\?\!\-\n]', ' ', starterText) # здесь избавляемся от знаков препинания, переносов и приводим текст к удобоваримому виду;
	changedText = changedText.lower()
	splittedWords = re.split(r' ', changedText)
	splittedWords = [x for x in splittedWords if x != ''] # создаем список всех слов текста, попутно избавляемся от лишних пробелов; 
	commonWords = collections.Counter(splittedWords).most_common(10) 
	return commonWords
a = input(str())
text = get_data(a)
print(word_freq(text))
input('Press enter to continue...')
