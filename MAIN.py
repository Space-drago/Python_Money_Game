 #Money Game

#Imports
import os
from time import time, sleep
import random
import time
import sys

sys.setrecursionlimit(999999999)
moneyIncrementAmount = open('inc.dll')
moneyIncrementAmount = moneyIncrementAmount.read()
moneyIncrementAmount = int((moneyIncrementAmount))
money = open('_.dll')
money = money.read()
money = int(money)
moneyDEF = money 
moneyIncrementAmountDEF = moneyIncrementAmount
print("Simple Money Making Game.")
print("NOTE: This does not make real currency or crypto.")
time.sleep(5)
print("Type enter to make money.")
print("Type s to go to the store.")
print("Tyoe save to save the game.")
def clear_console():
    os.system('cls')
def main():
    global moneyIncrementAmount
    global money
    print("You have " + str(money) + " money")
    c = input("What would you like to do?")
    if c == 's':
        print("Store ")
        print("You have ", int(money), "Money")
        print("What can you buy?")
        print("1. Workers Money production + 1   COST: 100")
        print("2. 1TB RAM Computer Money Production + 10 COST: 999")
        print("3. Super Upgrade production + 100 COST: 9999")
        print("PLACEHOLDER")
        print("5. WIN. COST: 1,000,000")
        print("You have ", int(money), " Money")
        schoice = input("Choose an option: ")
        if schoice == "1":
            if money >= 100:
                money -= 100
                moneyIncrementAmount += 1
                main()
            else:
                print("Not enough money!")
                main()
        elif schoice == "2":
            if money >= 999:
                money -= 999
                moneyIncrementAmount += 10
                print("Sucess!")
                main()
            else:
                print("Not enough money!")
                main()
        elif schoice == "3":
            if money >= 9999:
                money -= 9999
                moneyIncrementAmount += 100
                print("Sucess!")
                main()
            else:
                print("Not enough money!")
                main()
        elif schoice == "4":
            if money >= 100000:
                money -= 100000
                print("Sucess")
                print("Badge Image Link")
                print("https://space-drago.github.io/badgeMONEYGAME.space-drago.github.io/")
                main()
            else:
                print("Not enough money.")
                main()
        elif schoice == "5":
            if money >= 1000000:
                money -= 1000000
                print("Sucess!")
                print("YOU WIN!!!")
                print("You can keep playing if you want but there is nothing else to buy!")
                input("Click enter to keep playing!")
                main()
            else:
                print("Not enough money!")
                main()



    elif c == 'save':
        input("Save the game. Press enter to continue.")
        print("This will save the game")
        time.sleep(2)
        moneynew = money
        print(moneynew)
        moneyIncrementAmountNew = moneyIncrementAmount
        print(moneyIncrementAmountNew)
        input()
        clear1 = open('_.dll', 'r+')
        clear2 = open('inc.dll', 'r+')
        # Read in the file
        with open('_.dll', 'r') as file :
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(str(moneyDEF), str(moneynew))

            # Write the file out again
        with open('_.dll', 'w') as file:
            file.write(filedata)

        with open('inc.dll', 'r') as file2 :
            filedata2 = file2.read()

        # Replace the target string
        filedata2 = filedata2.replace(str(moneyIncrementAmountDEF), str(moneyIncrementAmount))

            # Write the file out again
        with open('inc.dll', 'w') as file2:
            file2.write(filedata2)
        
    else:
        clear_console()

        money += moneyIncrementAmount
        main()
        
        


main()




