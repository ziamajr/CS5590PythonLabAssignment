# David Ziama
# Class ID 3
# Create a Tic Tac Toegame


board = [0,1,2,3,4,5,6,7,8]

def printboard():
    print("----------")
    print(board[6],"|",board[7],"|",board[8])
    print("----------")
    print(board[3],"|",board[4],"|",board[5])
    print("----------")
    print(board[0],"|",board[1],"|",board[2])
    print("----------")

choices = []

for x in range (0, 9) :
    choices.append(str(x + 1))

playerOneTurn = True
winner = False


while not winner :
    printboard()

    if playerOneTurn :
        print("Player 1:")
    else :
        print("Player 2:")

    try:
        choice = int(input(">>"))
    except:
        print("That field has already been taken.")
        continue



