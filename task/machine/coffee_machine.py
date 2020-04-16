# create inputs for the machine materials
# initialize machine resources
water, milk, coffee_beans, cups, money = 400, 540, 120, 9, 550


def remaining():
    global water, milk, coffee_beans, cups, money
    # water += 0
    # milk += 0
    # coffee_beans += 0
    # cups += 0
    # money += 0
    # if money >= 1:
    print(f"\nThe coffee machine has:\n"
          f"{water} of water\n"
          f"{milk} of milk\n"
          f"{coffee_beans} of coffee beans\n"
          f"{cups} of disposable cups\n"
          f"${money} of money")

    action_user()


def action_user():
    print("\nWrite action (buy, fill, take, remaining, exit):")
    user_action = input()
    if user_action == "buy":
        buy()
    if user_action == "fill":
        fill()
    if user_action == "take":
        take()
    if user_action == "remaining":
        remaining()
    if user_action == "exit":
        exit_p()


def buy():
    print("\nWhat do  you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    user_2 = input()
    if user_2 == "1":
        espresso()
    if user_2 == "2":
        latte()
    if user_2 == "3":
        cappuccino()
    if user_2 == "back":
        action_user()


def espresso():
    global water, milk, coffee_beans, cups, money
    es_water = 250
    if water >= es_water:
        print("I have enough resources, making you a coffee!")
        water -= 250
        coffee_beans -= 16
        money += 4
        cups -= 1
    else:
        print("sorry, not enough water!")
    action_user()


def latte():
    global water, milk, coffee_beans, cups, money
    l_water = 350
    if water >= l_water:
        print("I have enough resources, making you a coffee!")
        water -= 350
        milk -= 75
        coffee_beans -= 20
        money += 7
        cups -= 1
    else:
        print("sorry, not enough water!")
    action_user()


def cappuccino():
    global water, milk, coffee_beans, cups, money
    c_water = 200
    if water >= c_water:
        print("I have enough resources, making you a coffee!")
        water -= 200
        milk -= 100
        coffee_beans -= 12
        money += 6
        cups -= 1
    else:
        print("sorry, not enough water!")
    action_user()


def fill():
    print("\nWrite how many ml of water do you want to add:")
    w = int(input())
    print("Write how many ml of milk do you want to add:")
    m = int(input())
    print("Write how many grams of coffee beans do you want to add:")
    b = int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    c = int(input())

    global water, milk, coffee_beans, cups, money
    water += w
    milk += m
    coffee_beans += b
    cups += c
    action_user()


def take():
    global money
    print("\nI gave you $" + str(money))
    money -= money
    action_user()


def exit_p():
    exit()


def main():
    action_user()
    # remaining()


main()
