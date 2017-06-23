#David Ziama
#ClassID # 3
#June 23, 2017

#1.Draw a Game board.
# This one is 3x3 (like in tic tac toe).
# Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).
# Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.
# Hint: use functions.

def print_horiz_line():
    print(" --- " * board_size)

def print_vert_line():
    print(" |  " * (board_size + 1))

if __name__ == "__main__":
    board_size = int(input("What is the size of the game board you want to draw? "))

    for index in range(board_size):
        print_horiz_line()
        print_vert_line()
print_horiz_line()