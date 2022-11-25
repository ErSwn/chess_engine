''' Functions and classes used for preprocessing boards on a chess game '''

import numpy as np
import tensorflow as tf
from copy import deepcopy
import numpy as np
from tqdm import tqdm

def unison_shuffled_copies(a, b):
    assert len(a) == len(b)
    p = np.random.permutation(len(a))
    return a[p], b[p]

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
  return tf.keras.utils.to_categorical(board, num_classes=13)

_Ki = -6
Ki = 6
_P = -1
P=  1
_K = -2
K = 2
_R = -3
R = 3
_Q = -4
Q = 4
_B = -5
B = 5

ec = 0



def translate(board):
  _Ki = -6
  Ki = 6
  _P = -1
  P=  1
  _K = -2
  K = 2
  _R = -3
  R = 3
  _Q = -4
  Q = 4
  _B = -5
  B = 5

  ec = 0
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
  B = [ r.split() for r in board.__str__().split('\n')]
  B = [[ pieces[p] for p in row ] for row in B]
  return B

def preprocess(board):
  return np.array(translate(board))


def tem_push(board, move):
  BOARD = board.copy()
  BOARD.push(move)
  return BOARD
  
class __Board:
  def __init__(self, board = None ):
    self.position = board
    
    if board is None:
      self.position = np.array([[_R,_K,_B,_Q,_Ki,_B,_K,_R],
                        [_P,_P,_P,_P,_P,_P,_P,_P ],
                        [ec,ec,ec,ec,ec,ec,ec,ec],
                        [ec,ec,ec,ec,ec,ec,ec,ec],
                        [ec,ec,ec,ec,ec,ec,ec,ec],
                        [ec,ec,ec,ec,ec,ec,ec,ec],
                        [P,P,P,P,P,P,P,P],
                        [R,K,B,Ki,Q,B,K,R]])
      
    self.position = tf.keras.utils.to_categorical(self.position, num_classes=13)
    self.position = self.position.reshape( (8, 8, 13, 1) )

  def get_moves(self, color):
    pass
    

def load_from_memory( f ):
  s = []
  data = np.load(f, allow_pickle=True)

  for i in data:
    data =data[i]

  for val in tqdm(data):
    *hist, y = val
    s.append( [hist, val] )
  return s
