import random
from PyDictionary import PyDictionary


dictionary=PyDictionary()
#get random word

file = open("/usr/share/dict/words","r")
words = file.read().split("\n")


def get_word():
	valid_word = False
	while(not valid_word):
		index = random.randint(0,235887)
		word = words[index]


		if(word[0].islower() and len(word)>2):
			valid_word = True
			return word
	

#get definition of word

def define_word():

	valid_word = False
	while(not valid_word):
		word = get_word()
		if(dictionary.meaning(word, disable_errors=True)):
			print(word.upper()+"\n")
			defs = dictionary.meaning(word)
			for key,value in defs.items():
				print(str(key)+": "+str(value).strip("[]\'\"").replace("\'",""))

			syns = dictionary.synonym(word)
			if syns:
				s = ""
				for syn in syns:
					s+= syn+", "
				print("\nSynonyms: "+s[:-2]+"\n")
			ants = dictionary.antonym(word)
			
			if ants:
				a = ""
				for ant in ants:
					a+= ant+", "

				print("Antonyms: "+a[:-2])
			valid_word = True

define_word()
