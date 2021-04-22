import Algorithms
import GFGMinimax

class TicTacToe:
    def __init__(self):
        self.current_player = 'X'
        self.board = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)
    def __str__(self):
        s = '\n'
        for i in range(3):
            for j in range(3):
                s += self.board[i][j] + ' '
            s += '\n'
        return s
    # move spots have these numbers:
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # returns true is can move, false if move invalid
    def move(self, spot):
        if spot < 1:
            return False
        elif spot < 4:
            if self.board[0][spot-1] == '-':
                self.board[0][spot-1] = self.current_player
                return True
            else:
                return False
        elif spot < 7:
            if self.board[1][spot-4] == '-':
                self.board[1][spot-4] = self.current_player
                return True
            else:
                return False
        elif spot < 10:
            if self.board[2][spot-7] == '-':
                self.board[2][spot-7] = self.current_player
                return True
            else:
                return False
        else:
            return False
    # make move by coordinate
    def exactMove(self, move):
        print(move)
        try:
            self.board[move[0]][move[1]] = self.current_player
            return True
        except:
            print('cannot move')
            return False
    # checks if game board full
    def boardFull(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j]=='-':
                    return False
        return True
    # checks if game is done, returns winner if done, else returns ''
    def gameDone(self):
        diagonal1, diagonal2 = '',''
        for i in range(3):
            if self.board[i][0] + self.board[i][1] + self.board[i][2] == self.current_player*3: # row check
                return self.current_player
            elif self.board[0][i] + self.board[1][i] + self.board[2][i] == self.current_player*3: # col check
                return self.current_player
            diagonal1 += self.board[i][i] # downward diagonal
            diagonal2 += self.board[2-i][i] # upward diagonal
        if diagonal1 == self.current_player*3 or diagonal2 == self.current_player*3:
            return self.current_player
        if self.boardFull():
            return 'tie'
        else:
            return ''

# runs game, returns winner
# supports quiet mode
def runGame(gamers=['human','human'], mode=''):
    validGamers = ['human','minimax','GFGminimax']
    if (not gamers[0] in validGamers) or (not gamers[1] in validGamers):
        return 'invalid game'
    winner = ''
    game = TicTacToe()
    players = ['X','O']
    while game.gameDone() == '':
        for i in players:
            game.current_player = i
            if mode!= 'quiet':
                print(game)
                print(game.current_player)
            valid = False
            if gamers[players.index(i)]=='human':
                while not valid:
                    play = input('Enter move number: ')
                    try:
                        play = int(play)
                    except:
                        continue
                    valid = game.move(play)
            elif gamers[players.index(i)]=='GFGminimax':
                print('minimax is choosing...')
                move = GFGMinimax.findBestMove(game.board)
                print(game.exactMove(move))
            elif gamers[players.index(i)]=='minimax':
                print('minimax is choosing...')
                move = Algorithms.findBestMove(game)
                print(game.move(move))
            if game.gameDone()!='':
                if mode!= 'quiet':
                    winner = game.gameDone()
                    print('Winner is', winner)
                    print(game)
                break
    return winner

if __name__ == '__main__':
    x = input('enter robot')
    runGame([x,'human'])
