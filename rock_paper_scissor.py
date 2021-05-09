import random as rd 


def comp():
    comp_list = ["ROCK", "PAPER", "SCISSOR"]
    i = rd.randint(0, 2)
    return comp_list[i]

while True:
    start = input("Enter s to start: ")
    if start == 's':
        pass
    elif start != 's':
        break

    name = input("Enter your name: ")
    conclu = input("Enter rock, paper or scissor: ")
    player_choise = conclu.upper()

    computer = comp()
    print("Computer choose: ", computer)

    if computer == player_choise:
        print("Match is Draw")
        continue
    if (computer == "ROCK" and player_choise == "PAPER") or (computer == "PAPER" and player_choise == "SCISSOR") or (computer == "SCISSOR" and player_choise == "ROCK"):
        flag = 1
    if (computer == "ROCK" and player_choise == "SCISSOR") or (computer == "SCISSOR" and player_choise == "PAPER") or (computer == "PAPER" and player_choise == "ROCK"):
        flag = 0
    
    if flag == 1:
        print(name,"is WINNER")
    else:
        print("Computer is WINNER")
