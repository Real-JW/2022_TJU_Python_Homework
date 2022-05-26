import hashFunction
import sevenDigits
import snake
import thBigCharacter
import TJU
import keyWords
import simGame
import autoSearch
import grammarCheck

def menu():
    try:
        num = eval(input(" 1.Get the hash value \n 2.Draw the number with 7-digit \n 3.Draw snake \n 4.Draw Big \n 5.Draw TJU \n 6.Scan Keywords \n 7.Game Simultion with radar map \n 8.Auto search web \n 9.A simple grammer parser \n Please choose from the following functions:" ))
        if   num == 1:
            hashFunction.hashFunction()
        elif num == 2:
            sevenDigits.sevenDigits()
        elif num == 3:
            snake.snake()
        elif num == 4:
            thBigCharacter.theBigCharacter()
        elif num == 5:
            TJU.TJU()
        elif num == 6:
            keyWords.keyWords()
        elif num == 7:
            simGame.simGame()
        elif num == 8:
            autoSearch.autoSearch()
        elif num == 9:
            grammarCheck.grammarCheck()
        else:
            print('Error')
    except:
        print("Please input a number! ")
        menu()

if __name__ == '__main__':
    menu()
