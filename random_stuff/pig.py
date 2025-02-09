import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    player = input("Enter the number of players (2 - 4): ")
    if player.isdigit():
        player = int(player)
        if 2 <= player <= 4:
            break
        else:
            print("Must have 2 - 4 players.")
    else:
        print("please put in a number!")

max_score = 50
player_scores = [0 for _ in range(player)]

while max(player_scores) < max_score:

    for player_id in range(player):
        print("\nPlayer number", player_id + 1, "turn has just started!\n")
        print("Your total score is:", player_scores[player_id], "\n")
        current_scores = 0

        while True:
            should_roll = input("Would you like to roll (y)?")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn over!")
                current_scores = 0
                break
            else:
                current_scores += value
                print("You rolled a:", value)

            print("Your score is:", current_scores)
        
        player_scores[player_id] += current_scores
        print("Your total scores is:", player_scores[player_id])

max_score = max(player_scores)
winning_player = player_scores.index(max_score)
print("Player number", winning_player + 1, "is the winner with a score of:", max_score)
