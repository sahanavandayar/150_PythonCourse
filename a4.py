# NOTE: Until you fill in the TTTBoard class mypy is going
# to give you multiple errors talking about unimplemented
# class attributes, don't worry about this as you're working


class TTTBoard:
    """A tic tac toe board

    Attributes:
        board - a list of '*'s, 'X's & 'O's. 'X's represent moves by player 'X',
        'O's represent moves by player 'O' and '*'s are spots no one has yet
        played on
    """

    def __init__(self):
        self.board = ["*","*","*","*","*","*","*","*","*"]
        #attributes in class, case if winner happens
##        self.winner = False
##        #when game ends
##        self.over = False

                                                                                                                                
    def __str__(self):
        return (self.board[0] + " " + self.board[1] + " " + self.board[2] + "\n"
               + self.board[3] + " " + self.board[4] + " " + self.board[5] + "\n"
               + self.board[6] + " " + self.board[7] + " " + self.board[8])

    def make_move(self,player,pos):
       #Places a move for player in the position pos

        if pos >= 0 and pos <= 8:
            if self.board[pos] == '*':
                self.board[pos] = player
                return True
            else:
                return False
        else:
            return False

        #pos is an integer
    def has_won(self,player):
        if ((self.board[0] == player and self.board[1] == player and self.board[2] == player) or #top row
            (self.board[3] == player and self.board[4] == player and self.board[5] == player) or #middle row
            (self.board[6] == player and self.board[7] == player and self.board[8] == player) or #last row
            (self.board[0] == player and self.board[3] == player and self.board[6] == player) or #left column
            (self.board[1] == player and self.board[4] == player and self.board[7] == player) or #middle column
            (self.board[2] == player and self.board[5] == player and self.board[8] == player) or #right column
            (self.board[0] == player and self.board[4] == player and self.board[8] == player) or #neg diagonal
            (self.board[2] == player and self.board[4] == player and self.board[6] == player)):   #pos diagnol 
            return True
        else:
            return False
        
        #returns True if player has won the game,and False if not
    def game_over(self):
        if (self.has_won("X") == True) or (self.has_won("O") == True):
            return True
        for index in self.board:
            if index == "*":
                return False 
        else:
            return True
        #returns True if someone has won or if the board is full, False otherwise
    def clear(self):
        self.board = ["*","*","*","*","*","*","*","*","*"]
        #clears board to reset the game


def play_tic_tac_toe() -> None:
    """Uses your class to play TicTacToe"""

    def is_int(maybe_int: str):
        """Returns True if val is int, False otherwise

        Args:
            maybe_int - string to check if it's an int

        Returns:
            True if maybe_int is an int, False otherwise
        """
        try:
            int(maybe_int)
            return True
        except ValueError:
            return False

    brd = TTTBoard()
    players = ["X", "O"]
    turn = 0

    while not brd.game_over():
        print(brd)
        move: str = input(f"Player {players[turn]} what is your move? ")

        if not is_int(move):
            raise ValueError(
                f"Given invalid position {move}, "
                "position must be integer between 0 and 8 inclusive"
            )

        if brd.make_move(players[turn], int(move)):
            turn = not turn

    print(f"\nGame over!\n\n{brd}")
    if brd.has_won(players[0]):
        print(f"{players[0]} wins!")
    elif brd.has_won(players[1]):
        print(f"{players[1]} wins!")
    else:
        print(f"Board full, that's game!")


##if __name__ == "__main__":
##    # here are some tests. These are not at all exhaustive tests. You will
##    # DEFINITELY need to write some more tests to make sure that your TTTBoard class
##    # is behaving properly.
##    brd = TTTBoard()
##    brd.make_move("X", 8)
##    brd.make_move("O", 7)
##
##    assert brd.game_over() == False
##
##    brd.make_move("X", 5)
##    brd.make_move("O", 6)
##    brd.make_move("X", 2)
##
##    assert brd.has_won("X") == True
##    assert brd.has_won("O") == False
##    assert brd.game_over() == True
##
##    brd.clear()
##
##    assert brd.game_over() == False
##
##    brd.make_move("O", 3)
##    brd.make_move("O", 4)
##    brd.make_move("O", 5)
##
##    assert brd.has_won("X") == False
##    assert brd.has_won("O") == True
##    assert brd.game_over() == True
##
###board is full
##    brd.clear()
##    assert brd.make_move("X",1)
##    assert brd.make_move("O",0)
##    assert brd.make_move("X",3)
##    assert brd.make_move("O",2)
##    assert brd.make_move("X",5)
##    assert brd.make_move("O",4)
##    assert brd.make_move("X",6)
##    assert brd.make_move("O",7)
##    assert brd.make_move("X",8)
##    
###assert to check the tie works
##    assert brd.has_won("X") == False
##    assert brd.has_won("O") == False
##    assert brd.game_over() == True
##
###out of bounds int
##    brd.clear()
##    assert brd.make_move("X",-9) == False
##    assert brd.make_move("X",9) == False
##    
###out of bounds string
##    #brd.clear()
##    #assert brd.make_move("X",avocado) == False
##
##    #talked w Prof Compton, no need for this _____________________________________________________________________________________________________________________
##
###overwrite move
##    assert brd.make_move("X",1)== True
##    assert brd.make_move("O",1) == False
##
##
##    
##
##    print("All tests passed!")
##
##    # uncomment to play!
##    play_tic_tac_toe()
