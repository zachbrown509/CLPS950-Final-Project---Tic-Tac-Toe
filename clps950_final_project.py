"""Tic Tac Toe Game"""

def single_player_game():
    import random

    board = [' ' for _ in range(10)]

    def print_board():
        print('   |   |   ')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |   ')
        print('-----------')
        print('   |   |   ')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |   ')
        print('-----------')
        print('   |   |   ')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |   ')

    print_board()

    def insert_letter(letter, pos):
        board[pos] = letter

    def space_is_free(pos):
        return board[pos] == ' '

    

    def is_board_full():
        return board.count(' ') == 1

    def is_winner(le):
        return ((board[1] == le and board[2] == le and board[3] == le) or
                (board[4] == le and board[5] == le and board[6] == le) or
                (board[7] == le and board[8] == le and board[9] == le) or
                (board[1] == le and board[4] == le and board[7] == le) or
                (board[2] == le and board[5] == le and board[8] == le) or
                (board[3] == le and board[6] == le and board[9] == le) or
                (board[1] == le and board[5] == le and board[9] == le) or
                (board[3] == le and board[5] == le and board[7] == le))

    def player_move():
        run = True
        while run:
            move = input("Please select a position to place 'X' (1-9): ")
            try:
                move = int(move)
                if 1 <= move <= 9:
                    if space_is_free(move):
                        insert_letter('X', move)
                        run = False
                    else:
                        print('Sorry, this space is occupied')
                else:
                    print('Please type a number between 1 and 9')
            except:
                print('Please type a number')

    def computer_move():
        possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
        move = 0

        for let in ['O', 'X']:
            for i in possible_moves:
                board_copy = board[:]
                board_copy[i] = let
                if is_winner(let):
                    move = i
                    return move

        corners_open = [i for i in possible_moves if i in [1, 3, 7, 9]]
        if corners_open:
            move = random.choice(corners_open)
            return move

        if 5 in possible_moves:
            move = 5
            return move

        edges_open = [i for i in possible_moves if i in [2, 4, 6, 8]]
        if edges_open:
            move = random.choice(edges_open)
            return move
        return move

    while not is_board_full():
        if not is_winner('O'):
            player_move()
            print_board()
        else:
            print("Sorry, you lose!")
            break
        
        if is_board_full():
            print("It's a tie!")
            break

        if not is_winner('X'):
            move = computer_move()
            if move != 0:
                insert_letter('O', move)
                print(f"Computer placed an 'O' in position {move}:")
                print_board()
        else:
            print("You win!")
            break

        if is_board_full():
            print("Tie game")
            break

    if input("Do you want to play again? (y/n): ").lower() == 'y':
        single_player_game()

def two_player_game():
    board = [' ' for _ in range(10)]

    def print_board():
        print('   |   |   ')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |   ')
        print('-----------')
        print('   |   |   ')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |   ')
        print('-----------')
        print('   |   |   ')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |   ')

    print_board()

    def insert_letter(letter, pos):
        board[pos] = letter

    def space_is_free(pos):
        return board[pos] == ' '
\

    def is_board_full():
        return board.count(' ') == 1

    def is_winner(le):
        return ((board[1] == le and board[2] == le and board[3] == le) or
                (board[4] == le and board[5] == le and board[6] == le) or
                (board[7] == le and board[8] == le and board[9] == le) or
                (board[1] == le and board[4] == le and board[7] == le) or
                (board[2] == le and board[5] == le and board[8] == le) or
                (board[3] == le and board[6] == le and board[9] == le) or
                (board[1] == le and board[5] == le and board[9] == le) or
                (board[3] == le and board[5] == le and board[7] == le))

    def player_move(player):
        run = True
        while run:
            move = input(f"Player {player}, please select a position to place '{player}' (1-9): ")
            try:
                move = int(move)
                if 1 <= move <= 9:
                    if space_is_free(move):
                        insert_letter(player, move)
                        run = False
                    else:
                        print('Sorry, this space is occupied')
                else:
                    print('Please type a number between 1 and 9')
            except:
                print('Please type a number')

    while not is_board_full():
        if not is_winner('O'):
            player_move('X')
            print_board()
        else:
            print("Player 'X' wins! Congratulations!")
            
            
        if is_board_full():
          print("It's a tie!")
          break

        if not is_winner('X'):
            player_move('O')
            print_board()
        else:
            print("Player 'O' wins! Congratulations!")
            break
          
        if is_board_full():
            print("It's a tie!")
            break

        

    if input("Do you want to play again? (y/n): ").lower() == 'y':
        two_player_game()

def main():
    print("Welcome to the Tic Tac Toe game!")
    mode = input("Enter 's' for single-player mode or 't' for two-player mode: ")
    if mode.lower() == 's':
        single_player_game()
    elif mode.lower() == 't':
        two_player_game()
    else:
        print("Invalid input. Please try again.")
        main()

if __name__ == "__main__":
    main()
