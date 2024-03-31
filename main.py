from helpers import user_input, print_board, check_turn, check_for_win
from pytimedinput import timedInput
import os

# dictionary = key: data
position = {1 : '1', 2 : '2', 3 : '3',
            4 : '4', 5 : '5', 6 : '6',
            7 : '7', 8 : '8', 9 : '9'}

playing, complete = True, False
turn = 0
prev_turn = -1

instructions = """
• • •
At the start of the game, your tic-tac-toe board will look like this:

 |1|2|3|
 |4|5|6|
 |7|8|9|

To select a position on the board, enter a spot from 1 to 9. Starting with player one, you will take turns entering your marks in unmarked positions.
The first player to get 3 of their marks in a row is the winner.
If no one wins, the game is a draw.
• • •
"""

print("Welcome to a game of tic-tac-timeout!")
player_one = input("Enter player one's name: ")
player_two = input("Enter player two's name: ")
if player_one == player_two:
    print("Player one has already selected that name. Please pick another.")
    player_two = input("Enter player two's name: ")

print(f"• {player_one}'s sign is X")
print(f"• {player_two}'s sign is 0")

# The user inputs how long they want each turn to be.
timer = user_input()

print("Enter ? to view the instructions, otherwise enter any key to begin the game.")
intro = input()
if intro == "?":
  print(instructions)
  begin = input("Enter any key to begin the game. ")
print("Now let's play!")


while playing:
    print_board(position)

    # Notify the player when they have made an invalid entry.
    if prev_turn == turn:
        print("Invalid input. Please pick an unmarked position.")
    # State whose turn it is.
    if check_turn(turn) == '0': 
        print(f"{player_one}, it is your turn.")
    else: 
        print(f"{player_two}, it is your turn.")
    print("Enter your position or select q to quit.")
    prev_turn = turn

    # timedOut = bool confirming whether the function timed out or not. 
    action, timedOut = timedInput(prompt="", timeout=timer)

    if(timedOut):
        print("YOUR TIME IS UP! YOUR TURN IS OVER!")
        turn += 1
        continue

    if action == "q": playing = False
    # Error handling: check if the input is a number (1-9).
    elif str.isdigit(action) and int(action) in position:
        # Error handling: ensure that the position is unmarked.
        if not position[int(action)] in {"X", "0"}:
            # We have valid input! Update the board.
            turn += 1
            position[int(action)] = check_turn(turn)

    # Check if their is a winner.
    if check_for_win(position): playing, complete = False, True
    # Check if the board is full (without a winner).
    draw = all((mark == 'X' or mark == '0') for mark in position.values())
    if (draw): playing = False

# Print the results.
print_board(position)
if complete:
    if check_turn(turn) == 'X': 
        print(f"Congratulations {player_one}, you have won.")
    else: 
        print(f"Congratulations {player_two}, you have won.")
else:
    print("Both players have tied. Nobody has won.")

print(f"Thanks for playing, {player_one} and {player_two}!")