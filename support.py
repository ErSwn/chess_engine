''' Functions and classes used for preprocessing boards on a chess game '''

import numpy as np

class List(list):
  ''' Special list with modified index slicing
      allowing to get slicings out of range
  '''
  def __init__(self, args = []):
    super().__init__(args)

  def __getitem__(self, item):
    if isinstance(item, slice):
        return super().__getitem__(slice( item.start, min(item.stop, self.__len__()) ))
    return super().__getitem__(item)
 

def get_black_view( board ):
  ''' rotates the board
      input: board in numpy shape
  '''
  return -np.rot90(np.array(board),  2)

def board_to_numpy( board ):
  return preprocess(board)

def to_categorical( board ):
  return tf.keras.utils.to_categorical(board, num_classes=13).reshape( (8, 8, 13, 1) )

pieces = {
    'r': _R,
    'n': _K,
    'b': _B,
    'q': _Q,
    'k': _Ki,
    'R': R,
    'N': K,
    'B': B,
    'Q': Q,
    'K': Ki,
    'p': _P,
    'P': P,
    '.': ec
}

def translate(board):
  B = [ r.split() for r in board.__str__().split('\n')]
  B = [[ pieces[p] for p in row ] for row in B]
  return B

def preprocess(board):
  return np.array(translate(board))


def tem_push(board, move):
  BOARD = board.copy()
  BOARD.push(move)
  return BOARD
