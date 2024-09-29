def draw_board(spots):
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
             f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
             f"|{spots[7]}|{spots[8]}|{spots[9]}|")
    print(board)

def check_turn(turn):
    return 'O' if turn % 2 == 0 else 'X'

def check_for_win(spots):
    # Handle Horizontal Cases
    if (spots[1] == spots[2] == spots[3]) or \
       (spots[4] == spots[5] == spots[6]) or \
       (spots[7] == spots[8] == spots[9]):
        return True
    # Handle Vertical Cases
    elif (spots[1] == spots[4] == spots[7]) or \
         (spots[2] == spots[5] == spots[8]) or \
         (spots[3] == spots[6] == spots[9]):
        return True
    # Diagonal Cases
    elif (spots[1] == spots[5] == spots[9]) or \
         (spots[3] == spots[5] == spots[7]):
        return True
    
    return False

# Example usage
spots = [' ']*10  # Initialize spots (index 0 is unused)
turn = 0  # Example turn

draw_board(spots)  # Display the empty board
