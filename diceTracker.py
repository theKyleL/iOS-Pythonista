# Visual representation of dice rolls for games using 2 6-sided dice.
# (a.k.a. Settlers of Catan)
__author__ = ‘Kyle Latino’


# imports
import re
import sys

# variables
numberPattern = r”[0-9]+”
record = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}


# function definitions
def setupDictionary():
	global record
	# print(record)
	

def showVisual(count):
	stringOfChars = ‘’
	for i in range(count):
		stringOfChars += ‘X’
	return stringOfChars
	
	
def addValueToDict(val):
	record[int(val)] += 1
	
	
def printOutValues():
	# display histogram of dice roll values
	for num in record:
		print(‘{:2}’.format(num) + ‘: ‘ + ‘{:2}’.format(record[num]) + ‘ ‘ + showVisual(record[num]))
	print()


def getInput():
	# Parse input
	inputValue = input()
	# check for valid value
	parseValue(inputValue)
	

def parseValue(val):
	# check for exit value
	if val == “exit”:
		print(‘Shutdown’)
		sys.exit()
	# verify integer value within constraints
	validNumber = re.match(numberPattern, val)
	if validNumber:
		if int(val) > 1 and int(val) < 13:
			print(str(val), ‘ is a valid number’)
			addValueToDict(val)
		else:
			print(str(val), ‘ is an invalid number’)
	else:
		print(str(val), ‘ is an invalid number’)
	
	
if __name__ == ‘__main__’:
	# Init dictionary
	setupDictionary()
	while True:
		# get number from user
		getInput()
		# display current histogram
		printOutValues()