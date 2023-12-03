from __future__ import print_function
import random


class TicTacToe:

    def __init__(self):  #Declaring the board array
        self.board = []



    def create_board(self):   #Creating the board
        for i in range(3):  #Creating rows
            row = []
            for j in range(3): #Creating columns
                row.append('-')  #Each borad Cell is initiated to display "_"
            self.board.append(row)  #Add another row

    def get_random_first_player(self): #Deciding who starts the game
        return random.randint(0, 1) #like a coin toss either 0 (0) or 1 (X)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player): #Deciding who wins according to board status
        win = None

        n = len(self.board)


        for i in range(n):    # checking rows
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:

                return win

        for i in range(n):          # checking columns
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        win = True            # checking diagonals form left to right
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True # checking diagonals form right to left
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):  #Checks if the board is full and game ended
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):  #if current playes was "0" swap to "X" else     swap to "0"
        return 'X' if player == 'O' else 'O'


    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ") #Prints each column (item) in a certain row
            print() #Prints next row line

    def start(self):
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O' #The payer who starts the game
        while True:
            print("Player " + str(player) + " turn")

            self.show_board()

            # taking user input
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            # fixing the spot
            self.fix_spot(row - 1, col - 1, player)

            # checking whether current player has won or not
            if self.is_player_win(player):
                print("Player " + str(player) + " wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.swap_player_turn(player)

        # showing the final view of board

        print() #new line to seperate
        self.show_board()


# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
