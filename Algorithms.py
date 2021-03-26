import TicTacToe

###########
# MINIMAX #
###########

player, opponent = 'X', 'O'

def log(s):
    filename = 'minimaxLog.txt'
    with open(filename,'a') as f:
        f.writelines(str(s) + '\n')

def minimax(board, depth, isMax):
    game = TicTacToe.TicTacToe()
    game.board = board
    if isMax: game.current_player = player
    else: game.current_player = opponent
    winner = game.gameDone()
    if winner == player: # winner is max
        #log('game')
        #print('max')
        return 1
    elif winner == 'tie': # tie
        #log('game')
        #print('tie')
        return 0
    elif winner == opponent: # winner is min
        #log('game')
        #print('min')
        return -1
    if isMax: # max move
        best = -10
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = player
                    best = max(best,minimax(board,depth+1,not isMax))
                    board[i][j] = '-'
        return best
    else: # min move
        best = 10
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = opponent
                    best = min(best,minimax(board,depth+1,not isMax))
                    board[i][j] = '-'
        return best
        
def findBestMove(game):
    board = game.board
    bestVal = -10
    bestMove = 0
    moveCount = 0
    for i in range(3):
        for j in range(3):
            moveCount += 1
            if board[i][j] == '-':
                board[i][j] = player
                moveVal = minimax(board, 0, False)
                board[i][j] = '-'
                print(moveVal)
                if moveVal > bestVal:
                    bestMove = moveCount
                    bestVal = moveVal
    return bestMove


    