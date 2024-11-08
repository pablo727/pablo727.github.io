class Board:
    def __init__(self):
        """Initialize the board with empty spaces."""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]  # 3x3 grid with empty spaces
    
    def display(self):
        """Display the current state of the board."""
        print("\n" + "\n---+---+---\n".join([" | ".join(row) for row in self.board]) + "\n")
    
    def update(self, row, col, player):
        """Update the board with the player's move."""
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            return True
        return False

    def is_winner(self, player):
        """Check if the player has won."""
        # Check rows, columns, and diagonals for a winning line
        for row in self.board:
            if all([cell == player for cell in row]):
                return True
        for col in range(3):
            if all([self.board[row][col] == player for row in range(3)]):
                return True
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        if self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            return True
        return False

    def is_full(self):
        """Check if the board is full (no empty spaces)."""
        return all(cell != ' ' for row in self.board for cell in row)


class Game:
    def __init__(self):
        """Initialize the game with two players."""
        self.board = Board()  # Create a new board instance
        self.current_player = 'X'  # Player X starts the game
    
    def switch_player(self):
        """Switch the current player."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def play_turn(self):
        """Handle one turn of the game."""
        valid_move = False
        while not valid_move:
            try:
                row = int(input(f"Player {self.current_player}, enter row (0-2): "))
                col = int(input(f"Player {self.current_player}, enter column (0-2): "))
                valid_move = self.board.update(row, col, self.current_player)
                if not valid_move:
                    print("This spot is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter numbers between 0 and 2.")
        
        self.board.display()
    
    def is_game_over(self):
        """Check if the game is over."""
        if self.board.is_winner('X'):
            print("Player X wins!")
            return True
        if self.board.is_winner('O'):
            print("Player O wins!")
            return True
        if self.board.is_full():
            print("It's a draw!")
            return True
        return False

    def start_game(self):
        """Start the game and alternate turns between players."""
        self.board.display()
        while not self.is_game_over():
            self.play_turn()
            self.switch_player()
        print("Game over!")

# Start the game
if __name__ == "__main__":
    game = Game()  # Create a game instance
    game.start_game()  # Start the game loop
