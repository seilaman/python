import random

NewGame = input("Do you want to play? (Y/N)")
retry=0
wordlist=["PIKACHU", "SEILA", "KEYBOARD","WORK","WALK","PROJECT","FIND","SUBLIME"]
Wordtofind=wordlist[random.randrange(0, len(wordlist))]
letters=[]
WordSplit = list(Wordtofind)
global Lettersfoundsofar
Lettersfoundsofar =  ["_" for i in Wordtofind ]

def findall(needle, haystack):
	result=[]
	for i, char in enumerate(haystack):
		if char == needle:
			result.append(i)
	return result

if (NewGame == "Y" or NewGame == "y"):
	print ("\n" + "*"*15 + "\n* Let's play! *\n" +"*"*15 + "\n")
	while retry < 10:
		Input = input("\n\nGive me a letter: ").capitalize()
		print("------------\n\n")
		if len(Input) == 1:
			b = findall(Input,Wordtofind)
			if len(b)>0:
				print("Letter Found!")
				for j in b:
					Lettersfoundsofar[j]=Input
				if (Lettersfoundsofar == WordSplit):
					print("All letters have been found! Well done mate!\n")
					exit()
			else:
				print("Try again!\n\n")
				retry += 1
			print("Word to find : " + "".join(Lettersfoundsofar))
			#"".join(letters).count(Input)
			print("Retries = " + str(retry) + "/10\n\n")
			letters.append(Input)
			print("Letters in the mail: " + ", ".join(letters))
		if retry == 10:
			print("You lost! Get lost!")
else:
	print("Byeeeeeeee!")
	exit()
