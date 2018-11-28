#Pseudo Code
# Use the itertools to made a two dimensional matrix of card number and suit
# Shuffle then print the card
#Import Modules
import random
import itertools

#Use product to create thwo dimensional matrix of 1-13 each with a suit [1, Clubs] to [13, Diamonds]
deck = list(itertools.product(range(1,14),['Clubs','Spades','Hearts','Diamonds']))

#Randomly shuffle this 2x2 matrix
random.shuffle(deck)

#Print out what you got, special cases for face cards
print("The card you drew was:")
if(deck[0][0] == 11):
	print("Jack of " + str(deck[0][1]))
elif(deck[0][0] == 12):
	print("Queen of " + str(deck[0][1]))
elif(deck[0][0] == 13):
	print("King of " +  str(deck[0][1]))
else:
	print(str(deck[0][0]) + " of " + str(deck[0][1]))

