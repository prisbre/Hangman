#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import random
import string
import os.path

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

def isValid(userInput, charInput):
    '''
    userInput: string, containing user input per guess.
    charInput: list, containing letters typed so far, no duplicate.

    Return: boolean, True if userInput is valid.

    Guarantee userInput to meet the following constraints:
    * accept userInput.length = 1 only
    * accept alphabet only
    * ignore case status
    * return False if the letters have been tried
    '''
    if len(userInput) != 1:
        return False
    elif userInput in charInput:
        return False
    else:
        return userInput.isalpha()

def showCharGuessed(charGuessed, targetWord):
    '''
    charGuessed: list, containing letters have been guessed, no duplicate.
    targetWord: string, containing the secret word the user is guessing.

    Return: string, comprised of letters and underscores that represents
        what letters in secretWord have been guessed.
        eg. '_ _ _ a _'
    '''

    tagetLength = len(targetWord)
    showGuessed = ''

    # Initialize as '_ _ _ _ _'
    if len(charGuessed) == 0:
        for index in range(tagetLength):
            showGuessed += '_ '
    # Base on targetWord, append character properly
    else:
        for index in range(tagetLength):
            if targetWord[index] in charGuessed:
                showGuessed = showGuessed + targetWord[index] + ' '
            else:
                showGuessed = showGuessed + '_ '
    return showGuessed

def isWordGuessed(charGuessed, targetWord):
    '''
    charGuessed: list, containing letters have been guessed, no duplicate.
    targetWord: string, containing the secret word the user is guessing.

    Return: boolean, True if all the letters of targetWord are in charGuessed.
    '''
    # Transfer targetWord to a list with no duplicate
    targetList = []
    for element in targetWord:
        if element not in targetList:
            targetList.append(element)

    # Estimate whether targetWord is guessed in following conditions
    guessedLen = len(charGuessed)
    targetLen = len(targetList)
    if guessedLen == targetLen:
        count = 0
        for element in targetList:
            if element in charGuessed:
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

def hangman():
    '''
    Main function

    * At the start, computer randomly pick up a target word.
    * Then show how many letters the secretWord contains.
    * Ask user to input a letter per round.
    * Feedback immediately after each guess, and show guessed letters.
    * After each round, display remaining alphabets to choose.
    * Keep going till successfully guessed or run out of tries.
    '''

    # Initialize and display word length
    print 'Hi! Welcome to the game Hangman!'
    fileName = str(os.path.dirname(__file__)) + r"\words.txt"
    targetWord = getWords(fileName)
    print 'I am thinking of a word that is',str(len(targetWord)),'letters long.' \
        + ' Try to guess what it is. :P'
    tries = len(targetWord) + 3
    errors = 0
    charInput = []          # Record all letter typed by user
    charGuessed = []        # Record input letters that match target word
    userInput = ''

    guessed = False
    while not guessed:

        # Display limited tries and letter range
        print '------------------------------------------------------------ \n'
        print 'You have ' + str(tries - errors) + ' tries to guess what it is.'
        print 'Available letters to choose:\n' + \
            narrowRange(charInput) + '\n' +\
            'Guess word : ' + showCharGuessed(charGuessed, targetWord)

        # Ask for valid input s
        valid = False
        while not valid:
            userInput = raw_input('Please give me a letter here: ').lower()
            valid = isValid(userInput, charInput)
            if not valid:
                print 'Sorry, input is invalid. Try again.'
        if userInput not in charInput:
            charInput.append(userInput)

        # Check if letter guessed
        if userInput in targetWord:
            charGuessed.append(userInput)
            print 'Well done! You got this letter: '+ \
                showCharGuessed(charGuessed, targetWord)
        else:
            errors += 1
            print 'Oops! Not this one.'

        # Check if run out of tries
        if errors == tries:
            print 'Well, you ran out of tries. \nThe secret word is '+ targetWord
            break

        # Congratulation when success
        guessed = isWordGuessed(charGuessed, targetWord)
        if guessed:
            print 'Congratulations! You did it!'
            print 'The secret word is '+ targetWord

hangman()






