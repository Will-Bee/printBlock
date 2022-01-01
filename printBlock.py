import os, sys


def printBlock(var):
    """
    Args:
        var ([int]): [True for BLOCKING print, else: UNBLOCKING print]
    """
    if var == True:
        sys.stdout = open(os.devnull, 'w')

    else:
        sys.stdout = sys.__stdout__



### examples

print("okay")
printBlock(True)
print("This is not printing")

print("this is no printing too")
printBlock(False)
print("This will print")
