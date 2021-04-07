#!/usr/bin/env python3

class CoffeeMachine:

    def __init__(self, money, water, milk, coffee_beans, cups):
        self.money = money
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups

    def __str__(self):
        return f"""The coffee machine has:\n{self.water} of water\n{self.milk} of milk\n{self.coffee_beans} of coffee beans\n{self.cups} of disposable cups\n{self.money} of money"""

    def remaining(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee_beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"${self.money} of money")
        print()

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        coffee = input()
        if coffee == '1':
            available = [int(self.water/250), int(self.coffee_beans/16)]
            if min(available) >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.coffee_beans -= 16
                self.cups -= 1
                self.money += 4
            else:
                if int(self.water/250) < 1:
                    print("Sorry, not enough water!")
                elif int(self.coffee_beans/16) < 1:
                    print("Sorry, not enough coffee beans!")
        elif coffee == '2':
            available = [int(self.water/350), int(self.milk/75), int(self.coffee_beans/20)]
            if min(available) >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.cups -= 1
                self.money += 7
            elif int(self.water/350) < 1:
                print("Sorry, not enough water!")
            elif int(self.milk/75) < 1:
                print("Sorry, not enough milk!")
            elif int(self.coffee_beans/20) < 1:
                print("Sorry, not enough coffee beans!")
        elif coffee == '3':
            available = [int(self.water/200), int(self.milk/100), int(self.coffee_beans/12)]
            if min(available) >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.cups -= 1
                self.money += 6
            else:
                if int(self.water/200) < 1:
                    print("Sorry, not enough water!")
                elif int(self.milk/100) < 1:
                    print("Sorry, not enough milk!")
                elif int(self.coffee_beans/12) < 1:
                    print("Sorry, not enough coffee beans!")
        elif coffee == 'back':
            print()

    def fill(self):
        print("Write how many ml of water do you want to add:")
        self.water += int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.coffee_beans += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.cups += int(input())

    def take(self):
        print(f"I gave you ${self.money}")
        self.money -= self.money

    def get_action(self, to_do):
        if to_do == 'buy':
            print()
            self.buy()
        elif to_do == 'fill':
            print()
            self.fill()
        elif to_do == 'take':
            print()
            self.take()
        elif to_do == 'remaining':
            print()
            self.remaining()


coffee_machine = CoffeeMachine(550, 400, 540, 120, 9)
action = ""

while action != 'exit':
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    coffee_machine.get_action(action)
