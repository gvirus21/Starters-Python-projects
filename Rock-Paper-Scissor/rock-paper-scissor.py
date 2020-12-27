r=0
while r==0:
    import random
    from random import choice

    print("Welcome to Rock-Paper-Scissor !!")
    print("Type 0 for Rock,1 for Paper & 2 for Scissor!!\n Your turn :")

    x=int(input("Enter your choice :"))

    print("your choice :")

    if x==0:
        print("ROCK!")    
    elif x==1:
        print("PAPER!")
    elif x==2:
        print("SCISSOR!")
    else:
        print("invalid input!! \nplease try again !")
        quit()

    y=random.randint(0,2)

    print("computer's choice :")

    if y==0:
        print("ROCK!")    
    elif y==1:
        print("PAPER!")
    elif y==2:
        print("SCISSOR!")

    print("REASULT!!")

    if x==0 and y==2:
        print("You won!")
    elif y==0 and x==2:
        print("You lose!!")
    elif x>y:
        print("You lose!!")
    elif x==y:
        print("Draw!")
    else: print("You lose!!")


r=int(input("Try again? 0 for yes , 1 for No :"))


