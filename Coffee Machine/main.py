machine_balance = 0

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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



def check_machine_resources(coffee):
    if MENU[coffee]["ingredients"]["water"]<=resources["water"] and MENU[coffee]["ingredients"]["milk"]<=resources["milk"] and MENU[coffee]["ingredients"]["coffee"]<=resources["coffee"]    :
        return True
    else:
        return False
def check_user_funds_serve(money, coffee):
    global machine_balance
    if money>=MENU[coffee]["cost"]:
        machine_balance+=MENU[coffee]["cost"]
        money-=MENU[coffee]["cost"]
        resources["water"]-=MENU[coffee]["ingredients"]["water"]
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
        resources["coffee"]-=MENU[coffee]["ingredients"]["coffee"]
        if money!=0.0:
            return f"Here is your {coffee} and change of {money} "
        else:
            return f"Here is your {coffee} "
    else:
        return f"You didn't have enough funds for {coffee}, your amount of {money} has been refunded  "

def generate_report():
    print(f"Water: {resources["water"]}ml")
    print(f"Water: {resources["milk"]}ml")
    print(f"Water: {resources["coffee"]}g")
    print(f"Money: ${machine_balance}")


user_choice="on"
while user_choice!="off":

    user_choice = input("What would you like? (espresso/latte/cappuccino):" ).lower()

    print(user_choice)

    if user_choice=="espresso" or user_choice=="latte" or user_choice=="cappuccino":
        if check_machine_resources(user_choice):
            quarter = float(input("insert quarters")) * 0.25
            dimes = float(input("insert dimes")) * 0.10
            nickles = float(input("insert nickles")) * 0.05
            pennies = float(input("insert pennies")) * 0.01
            user_money = quarter + dimes + nickles + pennies
            print(check_user_funds_serve(user_money,user_choice))
        else:
            print("Not enough resources in machine")
    elif user_choice=="report":
        generate_report()









