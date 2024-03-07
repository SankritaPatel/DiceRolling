import random

def print_dice(number):
    if number == 1:
        print("---------")
        print("|       |")
        print("|   O   |")
        print("|       |")
        print("---------")
    elif number == 2:
        print("---------")
        print("| O     |")
        print("|       |")
        print("|     O |")
        print("---------")
    elif number == 3:
        print("---------")
        print("| O     |")
        print("|   O   |")
        print("|     O |")
        print("---------")
    elif number == 4:
        print("---------")
        print("| O   O |")
        print("|       |")
        print("| O   O |")
        print("---------")
    elif number == 5:
        print("---------")
        print("| O   O |")
        print("|   O   |")
        print("| O   O |")
        print("---------")
    else:
        print("---------")
        print("| O   O |")
        print("| O   O |")
        print("| O   O |")
        print("---------")

def roll_dice():
    """Simulate rolling a six-sided die."""
    return random.randint(1, 6)

def main():
    print("Welcome to the dice simulator!")

    while True:
        input("Press Enter to roll the dice...")
        number = roll_dice()
        print("You rolled:", number)
        print_dice(number)

        choice = input("Roll again? (y/n): ")
        if choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()
