def user_input():
    while True:
        timer = input("How long will each turn in the game be? Enter a number from 1 to 9 (seconds) to decide.\n")
        if timer.isdigit() and 1 <= int(timer) <= 9:
            return int(timer)
        print("Invalid input. Please enter a number between 1 and 9.")

def print_board(position):
    # position[1] = data from key 1 of position dictionary
    board = (f"\n |{position[1]}|{position[2]}|{position[3]}|\n"
    f" |{position[4]}|{position[5]}|{position[6]}|\n"
    f" |{position[7]}|{position[8]}|{position[9]}|\n")

    print(board)

def check_turn(turn):
  if turn % 2 == 0: 
    return '0'
  else: 
    return 'X'

def check_for_win(position):
  # Handle Horizontal Cases
  if   (position[1] == position[2] == position[3]) \
    or (position[4] == position[5] == position[6]) \
    or (position[7] == position[8] == position[9]):
    return True
  # Handle Vertical Cases
  elif (position[1] == position[4] == position[7]) \
    or (position[2] == position[5] == position[8]) \
    or (position[3] == position[6] == position[9]):
    return True
  # Diagonal Cases
  elif (position[1] == position[5] == position[9]) \
    or (position[3] == position[5] == position[7]):
    return True
    
  else: return False