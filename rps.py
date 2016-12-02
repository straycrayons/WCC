import random
# Parameters: a String `move`
# Returns: Boolean for whether move is valid
#
# Valid moves include 'rock', 'paper', or 'scissors'`
#
def check_move(move):

    if move == 'rock' or move == 'paper' or move == 'scissors':
        return True
    else:
        return False

def get_player_move():

    # Prompt the user to enter their move
    move = raw_input('Pick your move: rock, paper, or scissors? ')

    # This will happen on a loop until the user enters a valid move
    while check_move(move) == False:
        print('Invalid move; pick again.')
        # Run this function again, so they're asked to enter a new move
        move = get_player_move()

    return move

# Test this function
print 'You picked: ' + get_player_move()

def get_computer_move():
    moves = ['rock', 'paper', 'scissors'];
    return random.choice(moves)

def judge(moveA, moveB):
    if moveA == 'rock' and moveB == 'paper':
        return False
    if moveA == 'rock' and moveB == 'scissors':
        return True
    if moveA == 'paper' and moveB == 'rock':
        return True
    if moveA == 'paper' and moveB == 'scissors':
        return False
    if moveA == 'scissors' and moveB == 'rock':
        return False
    if moveA == 'scissors' and moveB == 'paper':
        return True

def play():

    print('Welcome to Welcome to Rock, Paper, Scissors!')

    player = get_player_move()
    check_move(get_player_move)
    computer = get_computer_move()
    print('The computer picked: ' + computer)

    if player == computer:
        print('Tie')
    elif(judge(player, computer)):
        print('You won!')
    else:
        print('The computer won!')

    play_again = raw_input('Play again? Type `y` or `n`: ')

    if(play_again == 'y'):
        play()
    else:
        print('Thanks for playing!')

play()
