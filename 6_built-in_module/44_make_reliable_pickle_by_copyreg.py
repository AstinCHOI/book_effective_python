
## In Design View
# pickle: unreliable among reliable programs (recommend to use it simply)
# json: reliable among unreliable programs

class GameState(object):
    def __init__(self):
        self.level = 0
        self.lives = 4
    
state = GameState()
state.level += 1
state.lives -= 1

import pickle
state_path = '/tmp/game_state.bin'
with open(state_path, 'wb') as f:
    pickle.dump(state, f)


with open(state_path, 'rb') as f:
    state_after = pickle.load(f)
print(state_after.__dict__)
# >>>
# {'lives': 3, 'level': 1}


class GameState(object):
    def __init__(self):
        self.level = 0
        self.lives = 4
        self.points = 0

state = GameState()
serialized = pickle.dumps(state)
state_after = pickle.loads(serialized)
print(state_after.__dict__)
# >>>
# {'points': 0, 'lives': 4, 'level': 0}


# This is side-effect
with open(state_path, 'rb') as f:
    state_after = pickle.load(f)
print(state_after.__dict__)
# >>>
# {'lives': 3, 'level': 1} # where is points?

assert isinstance(state_after, GameState)


# 1) Default attribute value
class GameState(object):
    def __init__(self, level=0, lives=4, points=0):
        self.level = level
        self.lives = lives
        self.points = points

def pickle_game_state(game_state):
    kwargs = game_state.__dict__
    return unpickle_game_state, (kwargs,)

def unpickle_game_state(kwargs):
    return GameState(**kwargs)

import sys
if sys.version_info[0] >= 3:
    import copyreg 
else:
    import copy_reg as copyreg
copyreg.pickle(GameState, pickle_game_state)

state = GameState()
state.points += 1000
serialized = pickle.dumps(state)
state_after = pickle.loads(serialized)
print(state_after.__dict__)
# >>>
# {'lives': 4, 'level': 0, 'points': 1000}

class GameState(object):
    def __init__(self, level=0, lives=4, points=0, magic=5):
        self.level = level
        self.lives = lives
        self.points = points
        self.magic = magic

# Okay, now
state_after = pickle.loads(serialized)
print(state_after.__dict__)
# >>>
# {'magic': 5, 'points': 1000, 'lives': 4, 'level': 0}


# 2) Class version management
# remove lives for some reason
class GameState(object):
    def __init__(self, level=0, points=0, magic=5):
        self.level = level
        self.points = points
        self.magic = magic

# pickle.loads(serialized)
# >>>
# TypeError: __init__() got an unexpected keyword argument 'lives'

def pickle_game_state(game_state):
    kwargs = game_state.__dict__
    kwargs['version'] = 2
    return unpickle_game_state, (kwargs,)

def unpickle_game_state(kwargs):
    version = kwargs.pop('version', 1)
    if version == 1:
        kwargs.pop('lives')
    return GameState(**kwargs)

copyreg.pickle(GameState, pickle_game_state)
state_after = pickle.loads(serialized)
print(state_after.__dict__)
# >>>
# {'points': 1000, 'magic': 5, 'level': 0}


# 3) Safe import path
copyreg.dispatch_table.clear()
state = GameState()
serialized = pickle.dumps(state)
del GameState
class BetterGameState(object):
    def __init__(self, level=0, points=0, magic=5):
        self.level = level
        self.points = points
        self.magic = magic

# pickle.loads(serialized)
# >>>
# AttributeError: Can't get attribute 'GameState' on <module '__main__' from '44_make_reliable_pickle_by_copyreg.py'>

print(serialized[:25])
# >>>
# b'\x80\x03c__main__\nGameState\nq\x00)'

copyreg.pickle(BetterGameState, pickle_game_state)

state = BetterGameState()
serialized = pickle.dumps(state)
print(serialized[:35])
# >>>
# b'\x80\x03c__main__\nunpickle_game_state\nq\x00}'