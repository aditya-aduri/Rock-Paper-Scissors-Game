# Rock paper scissors

import random
player_decision = raw_input("please enter a choice(Rock, Paper or Scissor) : ")
possible_choice = ["Rock", "Paper", "Scissors"]
comp_choice = random.choice(possible_choice)
print("\n you chose is "  +  format(player_decision) + " computer choice is "   +   format(comp_choice)   +   "\n")


if player_decision == comp_choice:
    print ("both players selected" + format(player_decision) + "its a tie!")
elif player_decision == "Rock":
    if comp_choice == "Scissor":
        print ("Rock smashes Scissors, you win!")
    else:
        print ("paper covers rock, you Win!!")
elif player_decision == "paper":
    if comp_choice == "rock":
        print ("paper covers rock, you win!")
    else:
        print ("Scissors will cut paper, you lose!")
elif player_decision == "Scissor":
    if comp_choice == "paper":
        print ("scissor will cut paper, you win!")
    else:
        print ("rock will smash scissor,you win!!!!!!!!!")
