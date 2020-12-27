MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,    
}

quantity_available=True
while quantity_available==True:
    report=input("Want to see report? y or n :").lower()

    if report=="y":
        print(resources)
    order=input("What do you like to order? 1.Espresso, 2.latte, 3.cappuccino :").lower()

    if order=="off":
        """ Secret code to turn off the machine """
        quit()

    #checking resources
    def checkingResources(quantity_available=quantity_available):
        order_ingredients=MENU[order]["ingredients"]

        for i in MENU:
            if order==i:
                for quantity in resources:
                    if quantity not in order_ingredients:

                        """ if ingredient of resource is not required for 
                        selected coffee to make,we are adding that ingredient 
                        in coffee with amount of '0'"""

                        not_present_item=quantity
                        order_ingredients[not_present_item]=0

            return order_ingredients
    order_ingredients=checkingResources(quantity_available)
    
    for quantity in resources:
        """ new resources updating """
        resources[quantity]=resources[quantity]-order_ingredients[quantity]
        if resources[quantity]<=0:
            print("Sorry! insufficient items")
            quantity_available=False
            quit()
    print(f"new resources :{resources}")


    def coinCollecting():
        for i in MENU:
            if i==order:
                cost=MENU[order]["cost"]
                print(f"please pay ${cost}")

        print("Pay amount in coins ..")
        pennys=float(input("pennys: "))
        nickels=float(input("nickels: "))
        dimes=float(input("dimes: "))
        quarters=float(input("quarters: "))

        total=pennys*0.01+nickels*0.05+dimes*0.1+quarters*0.25

        cost=MENU[order]["cost"]
        return total,cost


    total,cost=coinCollecting()
    def transaction(total=total,cost=cost):
        if total>=cost:
            print("Transaction Successfull")
            if total>cost:
                change=total-cost
                print(f"Heres your change ${change}")
            
            print(f"Enjoy your {order}")
        else:
            print("Sorry not enough money! \nTransaction Failed")
    transaction(total,cost)


    
    


        
