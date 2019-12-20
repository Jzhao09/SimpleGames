import random


class TicTacToeGame:
    myBoard = []
    gameRunning = True
    available_moves = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    """
    This method creates the board holding the information on the value of the
    9 spaces of the board, from left to right, top to bottom.
    """
    @classmethod
    def create_board(cls):
        # is this even necessary haha...
        board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        # print(len(board))
        cls.myBoard = board

    """
    This method prints out the current 
    """
    @classmethod
    def display_board(cls):
        # Display Top border
        print("-------")
        # Display Top Row
        print("|" + cls.myBoard[0] + "|" + cls.myBoard[1]
              + "|" + cls.myBoard[2] + "|")
        # Display Top Middle border
        print("-------")
        # Display Middle Row
        print("|" + cls.myBoard[3] + "|" + cls.myBoard[4]
              + "|" + cls.myBoard[5] + "|")
        # Display Bottom Middle border
        print("-------")
        # Display Bottom Row
        print("|" + cls.myBoard[6] + "|" + cls.myBoard[7]
              + "|" + cls.myBoard[8] + "|")
        # Display Bottom
        print("-------")

    """
    This static method makes sure the input is a number 
    """
    @staticmethod
    def validate_user_input(number_input):
        # Check if input is a number
        try:
            number_input = int(number_input)
            # Make sure the number is between 1-9
            if number_input > 9 or number_input < 1:
                raise ValueError
            return number_input
        except ValueError:
            print("Invalid input! Enter a number between 1-9 inclusive")
            return False

    @classmethod
    def do_player_turn(cls):
        print("Pick a space to go: ")
        player_input = cls.validate_user_input(input())
        if not player_input:
            print("Invalid input")
        else:
            player_input -= 1
            if cls.myBoard[player_input] != '_':
                print("Invalid input")
            else:
                # Put an X in the square
                cls.myBoard[player_input] = 'X'
                # Remove the option from the list of available options
                cls.available_moves.remove(player_input)
                print("Removing: " + str(player_input) +
                      ", available moves remaining: " +
                      str(len(cls.available_moves)))
                # Show updated board
                cls.display_board()

    @classmethod
    def do_computer_turn(cls):
        # Print list of available moves
        print(cls.available_moves)
        # Pick a random number 0 - available_moves size and get the move
        random_number = random.randint(0, len(cls.available_moves)-1)
        print("random_number: " + str(random_number))
        random_number = cls.available_moves[random_number]
        print("space selected: " + str(random_number))
        # Put a O in that space
        cls.myBoard[random_number] = 'O'
        # Show updated board
        cls.display_board()
        # Remove that move from the list
        cls.available_moves.remove(random_number)

    @classmethod
    def check_moves_remaining(cls):
        if len(cls.available_moves) <= 0:
            return False
        else:
            return True

    @classmethod
    def run_game(cls):
        human_turn = True
        # Test code
        while cls.gameRunning:
            if human_turn:
                cls.do_player_turn()
            else:
                cls.do_computer_turn()
            human_turn = not human_turn
            cls.gameRunning = cls.check_moves_remaining()

    def __init__(self):
        self.create_board()
        self.display_board()
        self.run_game()


# Driver code
myGame = TicTacToeGame()