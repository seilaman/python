import random

NewGame = input("Do you want to play? (Y/N)")
retry=0
wordlist=["PIKACHU", "SEILA", "KEYBOARD","WORK","WALK","PROJECT","FIND","SUBLIME"]
Wordtofind=wordlist[random.randrange(0, len(wordlist))]
#Wordtofind= "PIKACHU"
letters=[]
WordSplit = list(Wordtofind)
global Lettersfoundsofar
Lettersfoundsofar = list(len(Wordtofind) * "_")

if (NewGame == "Y" or NewGame == "y"):
	print ("\n" + "*"*15 + "\n* Let's play! *\n" +"*"*15 + "\n")
	while retry < 10:
		Input = input("\n\nGive me a letter: ").capitalize()
		print("------------\n\n")
		if Input != "" and len(Input) == 1:
			Letterfound = Wordtofind.find(Input)
			if Letterfound != -1:
				print("Letter Found!")
				Lettersfoundsofar[Letterfound]=Input
				if (Lettersfoundsofar == WordSplit):
					print("Well done mate!\n")
					exit()
			else:
				print("Try again!\n\n")
				retry += 1
			print("Word to find : " + "".join(Lettersfoundsofar))
			print("Retries = " + str(retry) + "/10\n\n")
			letters.append(Input)
			print("Letters in the mail: " + ", ".join(letters))
		if retry == 10:
			print("You lost! Get lost!")
else:
	print("Bye!")
	exit()
