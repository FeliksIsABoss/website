#imports go here
import random
import time

#variables go here
cookies = 0
coins = 100
ponziShares = 0
ponziPrice = 263
ckamShares = 0
ckamPrice = 742
pyramidShares = 0
pyramidPrice = 8287
stringLower = "LIST"
stringLower2 = "GAME"
stringLower4 = "SLOT"
i = 1000000000
gamePlayer = 5
gameGuesser = random.randint(1, 10)
list = "List"
guesses = 3
CoinGuess = random.randint(15, 50)

#search engine actually begins
while(i > 1) :
   search = input("Welcome to Zeece's search engine, please type List to continue: ")

   if search == list or search == "list": #checks for search
       print("Games, Amogus, Slots, Gamble, Stock")
   if search == "Stock" or search == "Stock":
    print("Welcome to the Scam Market, where you lose money every single time you trade.")
    time.sleep(2)
    print("To get started, type trade {STOCK}, so for example 'trade ponzi'.")
    print("Alternatively, you can type 'stats' to see your portfolio.")
    while(True):
       bru = input(" ")
       if bru == "trade ponzi":
           print("Do you want to buy or sell Ponzi? Type b to buy or s to sell.")
           buyorsellp = input(" ")
           if buyorsellp == "b":
               print("How much stock do you want to buy?")
               buyp = input(" ")
               if input:
                   buyAmountp = float(buyp)
                   costp = buyAmountp * ponziPrice
                   print("This will cost you " + str(costp) + ". Are you sure?")
                   buyconfirmp = input(" ")
                   if buyconfirmp == "y":
                       if coins - costp >= 0:
                           ponziShares =+ buyAmountp
                           coins = coins - costp
                           print("You bought %s ponzi stock!" % buyAmountp)
                       elif coins - costp < 0:
                           print("Not enough money!")
                      
       if bru == "trade ckam":
           print("Do you want to buy or sell Ckam? Type b to buy or s to sell.")
           buyorsellc = input(" ")
           if buyorsellc == "b":
               print("How much stock do you want to buy?")
               buyc = input(" ")
               if input:
                   buyAmountc = float(buyc)
                   costc = buyAmountc * ckamPrice
                   print("This will cost you " + str(costc) + ". Are you sure?")
                   buyconfirmc = input(" ")
                   if buyconfirmc == "y":
                       if coins - costc >= 0:
                           ckamShares =+ buyAmountc
                           coins = coins - costc
                           print("You bought %s Ckam stock!" % buyAmountc)
                       elif coins - costc < 0:
                           print("Not enough money!")
                      
       if bru == "trade pyramid":
           print("Do you want to buy or sell pyramid? Type b to buy or s to sell.")
           buyorsellpy = input(" ")
           if buyorsellpy == "b":
               print("How much stock do you want to buy?")
               buypy = input(" ")
               if input:
                   buyAmountpy = float(buypy)
                   costpy = buyAmountpy * ckamPrice
                   print("This will cost you " + str(costpy) + ". Are you sure?")
                   buyconfirmpy = input(" ")
                   if buyconfirmpy == "y":
                       if coins - costpy >= 0:
                           ckamShares =+ buyAmountpy
                           coins = coins - costpy
