# create inputs for the machine materials
# initialize machine resources
class Machine:
    # water, milk, coffee_beans, cups, money = 400, 540, 120, 9, 550

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550

    def remaining(self):

        if self.money >= 1:
            print(f"\nThe coffee machine has:\n"
                  f"{self.water} of water\n"
                  f"{self.milk} of milk\n"
                  f"{self.coffee_beans} of coffee beans\n"
                  f"{self.cups} of disposable cups\n"
                  f"${self.money} of money")
        else:
            print(f"\nThe coffee machine has:\n"
                  f"{self.water} of water\n"
                  f"{self.milk} of milk\n"
                  f"{self.coffee_beans} of coffee beans\n"
                  f"{self.cups} of disposable cups\n"
                  f"{self.money} of money")

        self.action_user()

    def action_user(self):
        print("\nWrite action (buy, fill, take, remaining, exit):")
        user_action = input()
        if user_action == "buy":
            self.buy()
        if user_action == "fill":
            self.fill()
        if user_action == "take":
            self.take()
        if user_action == "remaining":
            self.remaining()
        if user_action == "exit":
            self.exit_p()

    def buy(self):
        print("\nWhat do  you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        user_2 = input()
        if user_2 == "1":
            self.espresso()
        if user_2 == "2":
            self.latte()
        if user_2 == "3":
            self.cappuccino()
        if user_2 == "back":
            self.action_user()

    def espresso(self):
        # global water, milk, coffee_beans, cups, money
        self.es_water = 250
        if self.water >= self.es_water:
            print("I have enough resources, making you a coffee!")
            self.water -= 250
            self.coffee_beans -= 16
            self.money += 4
            self.cups -= 1
        else:
            print("sorry, not enough water!")
        self.action_user()

    def latte(self):
        # global water, milk, coffee_beans, cups, money
        self.l_water = 350
        if self.water >= self.l_water:
            print("I have enough resources, making you a coffee!")
            self.water -= 350
            self.milk -= 75
            self.coffee_beans -= 20
            self.money += 7
            self.cups -= 1
        else:
            print("sorry, not enough water!")
        self.action_user()

    def cappuccino(self):
        # global water, milk, coffee_beans, cups, money
        self.c_water = 200
        if self.water >= self.c_water:
            print("I have enough resources, making you a coffee!")
            self.water -= 200
            self.milk -= 100
            self.coffee_beans -= 12
            self.money += 6
            self.cups -= 1
        else:
            print("sorry, not enough water!")
        self.action_user()

    def fill(self):
        print("\nWrite how many ml of water do you want to add:")
        self.w = int(input())
        print("Write how many ml of milk do you want to add:")
        self.m = int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.b = int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.c = int(input())

        # global water, milk, coffee_beans, cups, money
        self.water += self.w
        self.milk += self.m
        self.coffee_beans += self.b
        self.cups += self.c
        self.action_user()

    def take(self):
        # global money
        print("\nI gave you $" + str(self.money))
        self.money -= self.money
        self.action_user()

    def exit_p(self):
        exit()


def main():
    cm = Machine()
    while True:
        cm.action_user()
        print()


if __name__ == "__main__":
    main()

# main()
