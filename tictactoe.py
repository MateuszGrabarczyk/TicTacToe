import sys


def clear():
    print(1000 * "\n")


class Player:
    def __init__(self):
        self.name = input("Give me your name: ")
        while True:
            answer = input("Give me X or O: ").upper()
            if answer in ["X", "O"]:
                self.char = answer
                break
            else:
                print("Try again")
                continue
class Plansza:
    def __init__(self):
        self.board = {1 : " ", 2 : " ", 3 : " ",
                        4 : " ", 5 : " ", 6 : " ",
                        7 : " ", 8 : " ", 9 : " "}

    def printBoard(self):
        """It prints current state of the board"""
        print(self.board[1] + '|' + self.board[2] + '|' + self.board[3])
        print('-+-+-')
        print(self.board[4] + '|' + self.board[5] + '|' + self.board[6])
        print('-+-+-')
        print(self.board[7] + '|' + self.board[8] + '|' + self.board[9])


    def check_win_or_draw(self, char, name):
        """Checking if someone won the game. It can be a draw as well"""
        #horizontal win
        if ((self.board[1] == char and self.board[2] == char and self.board[3] == char) or
            (self.board[4] == char and self.board[5] == char and self.board[6] == char) or
            (self.board[7] == char and self.board[8] == char and self.board[9] == char)):
            print(name + " won the game!")
            sys.exit()

        #vertical win
        elif ((self.board[1] == char and self.board[4] == char and self.board[7] == char) or
            (self.board[2] == char and self.board[5] == char and self.board[8] == char) or
            (self.board[3] == char and self.board[6] == char and self.board[9] == char)):
            print(name + " won the game!")
            sys.exit()

        #diagonal win
        elif ((self.board[1] == char and self.board[5] == char and self.board[9] == char) or
              (self.board[3] == char and self.board[5] == char and self.board[7] == char)):
            print(name + " won the game!")
            sys.exit()


        #checking how many blanks are left
        blanks_left = 0
        for key, value in self.board.items():
            if value == " ":
                blanks_left += 1

        # checking if it is a draw
        if blanks_left == 0:
            print("It is a draw!")
            sys.exit()


    def fill_the_box(self, char, name):
        print("It is " + name + "'s move")
        while True:
            answer = int(input("Choose the empty box between 1 and 9 included: "))
            if answer in range(1, 10):
                if (self.board[answer] == " "):
                    self.board[answer] = char
                    print("--------------")
                    break
                else:
                    print("This box is not empty, try again")
            else:
                continue




#The game starts here
#initialize the game board
plansza = Plansza()
player1 = Player()
player2 = Player()

while True:
    plansza.printBoard()
    plansza.fill_the_box(player1.char, player1.name)
    plansza.check_win_or_draw(player1.char, player1.name)
    clear()

    plansza.printBoard()
    plansza.fill_the_box(player2.char, player2.name)
    plansza.check_win_or_draw(player2.char, player2.name)
    clear()