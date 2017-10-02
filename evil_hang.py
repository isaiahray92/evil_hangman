'''
Hangman.py
'''

import sys
import random
from collections import defaultdict

class Hangman:
    '''
    Initializes the words list
    '''
    def __init__(self):
        file = open('words.txt','r')
        self.words = []
        self.wordguess = []
        for line in file:
            self.words.append(line.rstrip())

    '''
    Outputs the current status of the guesses
    '''
    def printword(self):
        for c in self.wordguess:
            print c,
        print

    def playgame(self):
        # generate random word
        word = self.words[random.randint(0,len(self.words)-1)]
        self.wordguess = ['_'] * len(word)
        #Making a subset of all of the words that have the same length as the given word
        subset = [words for words in self.words if len(words) == len(word)]

        #Putting the given word into the subset list
        subset.append(word)
        guesses = 0
        remaing = 10
        user_guess = []
        #letters = list(word)
        
        print self.wordguess
        print ('The length of the word is %s' %len(word))
        while guesses < 10:
            
            #Making a dictionary where the values are lists
            subdict = defaultdict(list)

            print ('You have %s remaining guess' %remaing)
            ch = raw_input('Enter a guess:').lower()
            if ch in user_guess:
                print 'Already Guessed'
            elif ch.isalpha() and len(ch) == 1:
                user_guess.append(ch)
                print ('You have already guessed %s' %user_guess)
                guesses += 1
                remaing -= 1
            else:
                if len(ch) > 1:
                    print 'please enter a letter not a string'
                else:
                    print "please enter a letter in the alphabet"
            
            #Going through the subset of words to find if the letter guessed is in any of the words
            for sub in subset:
                letters = list(sub)
                result_list = map(lambda x: True if x==ch in letters else False,letters)
                #If the word does not contain the letter guessed put in the key value 0 and append
                #to the list
                if True not in result_list:
                    subdict[0].append(sub)
                

                else:
                    #If the word contains the letter guessed we will need to find the positions
                    #positions will find the positions of the guessed letter
                    positions = [i for i, x in enumerate(result_list) if x]
                    #If there is only one letter in the word, we will get the position in the string
                    #and have the dictionary key equivalent to this value.
                    if len(positions) == 1:
                        subdict[positions[0] + 1].append(sub)
                    else:
                        #If the word has the letter in more than one position we will multiply both 
                        #positions by 3 and add them together to get the key.
                        keys = 0
                        i = 0
                        for pos in positions:
                            keys = positions[i] *3 + keys
                            i += 1
                        subdict[keys].append(sub)

                   

            #Once we have our dictionary we will find the largest list and make this our new subset 
            #of words
            largest = [keys for keys in subdict.keys() if len(subdict.get(keys))== max([len(n) for n in subdict.values()] )]
            

            if len(largest) > 0:
                subset = subdict.get(largest[0])
            
            if subset[0] > 0:
                word = subset[0]

            #Once we have a new word we will print the letters containing that words and start
            #the process over again
            letters = list(word)
            result_list = map(lambda x: True if x == ch in letters else False,letters)
            
            
            if True not in result_list:
                print '%s is not in the word' %ch
            else:
                positions = [i for i, x in enumerate(result_list) if x]
                for pos in positions:
                    self.wordguess[pos] = ch
            print self.wordguess
            if '_' not in self.wordguess:
                print 'You win!!'
                break

        if '_' in self.wordguess:
            print 'You lose! The word was: %s ' %word
            answer = raw_input('Do you want to play again? y or n ').lower()
            if answer == 'y':
                game = Hangman()
                game.playgame()





if __name__ == "__main__":

    game = Hangman()

    game.playgame()
