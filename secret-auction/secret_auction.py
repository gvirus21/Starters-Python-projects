import os
def clear():
    os.system('cls')
bid_again=True
highest_bid=0
Winner=""

while(bid_again==True):
    clear()
    Name=input("Enter your name :")
    Bid=int(input("Enter your bid :"))
    if highest_bid<Bid:
        highest_bid=Bid
        Winner=Name
    newBid=input("New bid? :")   
    if newBid=="yes" or newBid=="1":
        bid_again=True
    elif newBid=="no" or newBid=="0":
        bid_again=False
    else:
        print("invalid input")
        quit()
print(f"{Winner} won the bid with ${highest_bid}")

