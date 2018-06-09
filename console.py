__doc__ = "A module to log information"
__all__ = ["E", "L", "P", "R", "S", "log"]


E = 'ERROR'
L = 'LOADING'
P = 'PROCESSING'
R = 'RUNNING'
S = 'SUCCESS'

def log(main, msg):
    print('[{}]: {}'.format(main, msg))

