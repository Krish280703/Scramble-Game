import random

scoresFile = open('Scores.txt')
Scores = []
for line in scoresFile:
    line = line.split()
    letter = line[0]
    score = int(line[1])
    Scores.append([letter,score])
scoresFile.close()


tilesFile = open('Tiles.txt')
Tiles = []
for line in tilesFile:
    line = line.strip()
    Tiles.append(line)
tilesFile.close()


dictionaryFile = open('Dictionary.txt')
Dictionary = []
for line in dictionaryFile:
    line = line.strip()
    Dictionary.append(line)
dictionaryFile.close()


def containsOnlyEnglishAlphabets(word):
    Alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',  'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']
    for letter in word:
        if letter.upper() not in Alphabets:
            return False
    return True

def getLetterScore(letter):
    letter.upper()
    for x in range(0,26):
        if Scores[x][0] == letter:
            return Scores[x][1]
        else:
            continue

def getWordScore(word):
    word.upper()
    WordScore = 0
    for letter in word:
        WordScore += getLetterScore(letter)
    return WordScore

def WordAndTile(word,myTiles):
    for letter in word:
        if letter not in myTiles:
            return False
        elif letter in myTiles:
            myTiles.remove(letter)
    return True


def isValid(word,myTiles,dictionary):
    word.upper()
    if (containsOnlyEnglishAlphabets(word) == True):
        if word in dictionary:
            if (WordAndTile(word,myTiles) == True):
                return True
    return False

myTiles = random.choices(Tiles, k=7)
print("Random Generated Tiles = ", myTiles)
print("The score for each tile will be printed below: ")
for letter in myTiles:
    print(letter , ":" , getLetterScore(letter))
word = input("Enter a valid word: ")
word.upper()
if (isValid(word,myTiles,Dictionary) == True):
    print("The score of the word is : ",getWordScore(word))
else:
    print("Invalid input")