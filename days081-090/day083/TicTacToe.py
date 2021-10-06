class TicTacToe:
    def __init__(self):
        self.activeGame = True
        self.board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.piece = 'X'
        self.win = False
        self.winning_condition = None
        self.start()

    def draw_board(self):
        print()
        board = self.board
        """Prints the game board and current set game pieces"""
        print('   |   |')
        print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
        print('   |   |')

    def change_active_piece(self):
        """Change the active game piece (ie. O or X) after a successful move has been made."""
        if self.piece == 'X':
            self.piece = 'O'
        else:
            self.piece = 'X'

    def get_move(self):
        """Place the player's input move onto the game board if move is available."""
        while True:
            move = int(input(f'Player {self.piece}, please enter the space (1-9) to make your move: ')) - 1
            if self.board[move] != "O" and self.board[move] != "X":
                self.board[move] = self.piece
                break
            else:
                print('There is already a piece there! Please try again...')

    def check_for_win(self):
        """Check to see if any of the win conditions are satisfied."""

        # Check Rows:
        start_i = 0
        end_i = 2
        for i in range(3):
            if all(self.piece == ele for ele in self.board[start_i:end_i + 1]):
                self.winning_condition = f'{self.piece} Winning Condition: Row {i + 1}'
                self.win = True
                break
            else:
                start_i += 3
                end_i += 3

        # Check Columns:
        start_i = 0
        end_i = 6
        for i in range(3):
            if all(self.piece == ele for ele in self.board[start_i:end_i + 1:3]):
                self.winning_condition = f'{self.piece} Winning Condition: Column {i + 1}'
                self.win = True
                break
            else:
                start_i += 1
                end_i += 1

        # Check the Two Diagonals:
        if all(self.piece == ele for ele in self.board[2:7:2]):
            self.winning_condition = f'{self.piece} Winning Condition: Top left to bottom right diagonal.'
            self.win = True
        elif all(self.piece == ele for ele in self.board[0:9:4]):
            self.winning_condition = f'{self.piece} Winning Condition: Top right to bottom left diagonal.'
            self.win = True

    def start(self):
        print('WELCOME TO TIC-TAC-TOE!')
        while self.activeGame:
            self.draw_board()
            self.get_move()
            self.check_for_win()
            if self.win:
                self.draw_board()
                print(f'Player {self.piece} Wins. Congratulations!')
                print(self.winning_condition)
                break
            else:
                self.change_active_piece()
        print('--- Game over ---')


if __name__ == "__main__":
    game = TicTacToe()