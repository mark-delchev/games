import random
games = int(input("How many games would you like to play?"))
choices = ["rock", "paper", "scissors"]
player_wins = 0
computer_wins = 0


for game in range(games):
    player_input = input().lower()
    computer_select = random.randint(0, len(choices) - 1)
    computer_input = choices[computer_select]
    print(f"Player: {player_input}")
    print(f"Computer: {computer_input}")
    if player_input == computer_input:
        print("Tie!")
    elif player_input == "rock":
        if computer_input == "paper":
            print("Computer wins!")
            computer_wins += 1
        else:
            print("Player wins!")
            player_wins +=1
    elif player_input == "paper":
        if computer_input == "rock":
            print("Player wins!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1
    elif player_input == "scissors":
        if computer_input == "rock":
            print("Computer wins!")
            computer_wins += 1
        else:
            print("Player wins!")
            player_wins += 1
print(f"Final score: Computer- {computer_wins} Player- {player_wins}")
