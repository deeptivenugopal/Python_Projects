import random
print("Rolling a dice.....")

while True:
    print("Do you want roll the dice?")
    answer = input("> ").lower().strip()
    if answer == "yes":
        num = random.randint(1,6)
        if num == 1:
            print("------------\n"
                  "|          |\n"
                  "|    O     |\n"
                  "|          |\n"
                  "------------")
        elif num == 2:
            print("------------\n"
                  "|          |\n"
                  "| O     O  |\n"
                  "|          |\n"
                  "------------")
        elif num == 3:
            print("-------------\n"
                  "| O     O   |\n"
                  "|           |\n"
                  "|    O      |\n"
                  "------------")
        elif num == 4:
            print("-------------\n"
                  "| O     O   |\n"
                  "|           |\n"
                  "| O     O   |\n"
                  "------------")
        elif num == 5:
            print("-------------\n"
                  "| O     O   |\n"
                  "|    O      |\n"
                  "| O     O   |\n"
                  "------------")
        elif num == 6:
            print("------------\n"
                  "| O  O  O  |\n"
                  "|          |\n"
                  "| O  O  O  |\n"
                  "------------")
    else:
        break
    
