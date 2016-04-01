# Hangman game

import random
import string
import os.path

fileName = str(os.path.dirname(__file__)) + r"\words.txt"

def getWords(fileName):
    """
    Input: a file only containing words in one line.
    Return: string, a lowercase words pick up at random.

    Depending on the size of the word list, this function may
      take a while to finish.
    """
    print "Loading word list from file..."
    fileHandle = open(fileName, 'r')
    line = fileHandle.readline()
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return random.choice(wordlist).lower()

targetWord = getWords(fileName)

def isValid(userInput):
    '''
    Input: string, containing user input.
    Return: boolean, True if userInput is valid.

    Guarantee userInput to meet the following constraints:
    * userInput.length = 1
    * only alphabet accept
    * ignore case
    '''
    if len(userInput) == 0 or len(userInput) > 1:
        return False
    else:
        return userInput.isalpha()

def showCharGuessed(charGuessed, targetWord, allGuessed):
    '''
    charGuessed: list, containing letters have been guessed, no duplicate.
    targetWord: string, containing the secret word the user is guessing.
    allGuessed: boolean, True if targetWord is guessed.
    Return: string, comprised of letters and underscores that represents
        what letters in secretWord have been guessed.
        eg. '_ _ _ a _'
    '''
    tagetLength = len(targetWord)
    showGuessed = ''

    # Initialize as '_ _ _ _ _'
    if len(charGuessed) == 0:
        for i in range(tagetLength):
            showGuessed += '_ '
    # Base on targetWord, append character properly
    elif not allGuessed:
        for i in range(tagetLength):
            if targetWord[i] in charGuessed:
                showGuessed = showGuessed + targetWord[i] + ' '
            else:
                showGuessed = showGuessed + '_ '
    # Show answer when all letters guessed
    else:
        showGuessed = targetWord
    return showGuessed

def isWordGuessed(charGuessed, targetWord):
    '''
    charGuessed: list, containing letters have been guessed, no duplicate.
    targetWord: string, containing the secret word the user is guessing.
    Return: boolean, True if all the letters of targetWord are in charGuessed.
    '''
    # Transfer targetWord to a list with no duplicate
    targetList = []
    for e in targetWord:
        if e not in targetList:
            targetList.append(e)

    # Comparison, add some defensive feature
    guessedLen = len(charGuessed)
    targetLen = len(targetList)
    if guessedLen == targetLen:
        count = 0
        for e in targetList:
            if e in charGuessed:
                count += 1
        if count == targetLen:
            return True
        else:
            return False
    else:
        return False

def narrowRange(charInput):
    '''
    charInput: list, containing letters typed so far, no duplicate.
    Return: string, containing filtered Alphabet for choosing.
    '''
    # Delete input letters from Alphabet to narrow range
    availableLetters = 'A B C D E F G H I J K L M ' + \
        'N O P Q R S T U V W X Y Z '
    for element in charInput :
        element = element.upper()
        if element in availableLetters:
            oldElement = element + ' '
            availableLetters = availableLetters.replace(oldElement, '')
    return availableLetters





'''
def hangman():
'''

