from collections import deque



#------------------------------------ MCT vs Human ------------------------------------
#Decribe Variable
#These variables for board game gui
BLOCK_SIZE = 50
PADDING_SIZE = 5
BOARD_WIDTH = BLOCK_SIZE * 8
BOARD_HEIGHT = BLOCK_SIZE * 8 + 20
FRAME_PER_SECOND = 40
WINDOWWIDTH = BLOCK_SIZE * 10
WINDOWHEIGHT = BLOCK_SIZE * 10
XMARGIN = int(((8 * BLOCK_SIZE)) / 2)
YMARGIN = int(((8 * BLOCK_SIZE)) / 2)
retract_moves = deque(maxlen=5)

#These variables for players
MCTS_NUM = 2
MAX_THINK_TIME = 5
debug = False
player = 1
victory = 0
whiteTiles = 2
blackTiles = 2
useAI = True
changed = True
AIReadyToMove = False

#These variables for board
board = [[0 for x in range(8)] for x in range(8)]
board[3][3] = 1
board[3][4] = 2
board[4][3] = 2
board[4][4] = 1
