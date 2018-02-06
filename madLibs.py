#! \usr\bin\env python3

import re

with open('madLibs.txt') as madLibFile:
	madLibContents=madLibFile.read()
madLibsWords=list(madLibContents.split())

adjectiveRegex=re.compile(r'ADJECTIVE*')
nounRegex=re.compile(r'NOUN*')
adverbRegex=re.compile(r'ADVERB*')
verbRegex=re.compile(r'VERB*')

for i in range(len(madLibsWords)):
	if adjectiveRegex.match(madLibsWords[i]):
		print('Enter and adjective',end=': ')
		sub= input()
	elif nounRegex.match(madLibsWords[i]):
		print('Enter and noun',end=': ')
		sub=input()
	elif adverbRegex.match(madLibsWords[i]):
		print('Enter an adverb',end=': ')
		sub=input()
	elif verbRegex.match(madLibsWords[i]):
		print('Enter and verb',end=': ')
		sub=input()
	else:
		continue
	madLibsWords.remove(madLibsWords[i])
	madLibsWords.insert(i,sub)
joinWordsList=' '
newString=joinWordsList.join(madLibsWords)
with open('madlibNew.txt','w') as newMadLibFile:
	newMadLibFile.write(newString)
print(newString)
