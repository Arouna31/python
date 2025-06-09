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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {"quarter": 0.25, "dime": 0.10, "nickle": 0.05, "pennie": 0.01}


def check_resource_for_menu(menu):
    check_table = {"is_okay": True, "ingredients_not_okay": []}

    for resource in MENU[menu]["ingredients"]:
        required_amount = MENU[menu]["ingredients"][resource]
        available_amount = resources.get(
            resource, 0
        )  # get() avoid error when key not present

        if available_amount < required_amount:
            check_table["is_okay"] = False
            check_table["ingredients_not_okay"].append(resource)

    return check_table


def handle_payment():
    total = 0
    print("Please insert coins.")
    for coin in coins:
        amount = int(input(f"How many {coin}s ? : "))
        total += amount * coins[coin]

    return total


def main():
    machine_state = "on"

    while machine_state == "on":
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")

        if user_choice == "off":
            machine_state = "off"
        if user_choice == "report":
            print(
                f"\nWater : {resources['water']}ml \nMilk : {resources['milk']}ml \nCoffee: {resources['coffee']}g\n"
            )

        for menu in MENU:
            if menu == user_choice:
                resources_sufficient = check_resource_for_menu(menu)

                if resources_sufficient["is_okay"]:
                    user_payment = handle_payment()

                    if user_payment < MENU[menu]["cost"]:
                        print("Sorry that's not enough money. Money refunded.")
                    else:
                        if user_payment > MENU[menu]["cost"]:
                            print(
                                f"Here is ${round(user_payment - MENU[menu]['cost'], 2)} dollars in change."
                            )

                        for resource in MENU[menu]["ingredients"]:
                            resources[resource] = (
                                resources.get(resource, 0)
                                - MENU[menu]["ingredients"][resource]
                            )

                        print(f"Here is your {menu} ☕ Enjoy !")

                else:
                    print(
                        f"Sorry there is not enough {resources_sufficient['ingredients_not_okay'][0]}."
                    )


main()
