from utils import utils
import re


def parseCrateStacks(input):
    """Parses input of the given form to list of lists of letters, list with index 0 is empty.
    Args:
            input (string): Example:"[D]         [D]\n[G] [F] [S] [L] [Q]\n1   2   3   4" 

    Returns:
            list of lists: A list of lists. Listst under '0' intended to be empty to simplify indexing. of integers Example []
    """
    numStacks = int(max(re.findall(r"\d", input))
                    )  # the last line of the input
    crateStacks = [[]
                   for _ in range(numStacks+1)]  # +1 to simplify referencing

    oneLineInput = input.replace('\n', ' ')
    parsedInput = re.finditer(r"\[([A-Z])\]", oneLineInput)
    getId = toStackId(numStacks)

    crateTags = list(
        map(lambda match: (getId(match.start()), match.group(1)), parsedInput))
    for (stackId, crateTag) in crateTags:
        crateStacks[stackId].insert(0, crateTag)

    return crateStacks


def toStackId(numStacks):
    """ Decorates 'intMapper' to take into account the number of stacks and allow position of matched '[' as input

    Args:
            numStacks (int): Number of crate stacks

    Example:

            Let numStacks = 3

            space: "_"
            +0				   +0
            in	0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 
                    [ A ] _ [ B ] _ [ C ] _ [ D ] _ [ E ]
            out	  0       1       2       1       2

            0->0, 4->1, 9->2, 13->1, 17->2
            id = (num)*4 + 1 -> stackId = (id-1)//4, stackId [1..]

    Returns:
            function(posMatch): A function, that maps given match position of "[" in the string to a stack id(>0).
    """
    return lambda id: intMapper(id+1) % numStacks + 1  # id= idOf('[')


def intMapper(num):
    """ Maps num -> toNum according to a fomula below.

    Args:
            num (int): An integer to map.

    Example:

            space: "_"
            +0				   +10
            in 	0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 
                    [ A ] _ [ B ] _ [ C ] _ [ D ] _ [ E ]
            out	  0       1       2       3       4

            1->0, 5->1, 9->2, 13->3, 17->4

                    num = (toNum)*4 + 1 -> toNum = (num-1)//4

    Returns:
            int: Mapped integer according to the formula (num-1)//4
    """
    return (num-1)//4


def parseMoves(input):
    """Parses any substring of the form 'move (\d+) from (\d+) to (\d+)' to a tripple of the form (<amount>,<from>,<to>) and packs them in a list.

    Args:
            input (string): A string. 

    Returns:
            list of integer tuppels: A list of integer tripples of the form (<amount>,<from>,<to>)
    """
    PATTERN = 'move (\d+) from (\d+) to (\d+)'
    matched = re.compile(PATTERN).findall(input)

    moves = []
    for move in matched:
        (amount_, from_, to_) = move
        moves.append((int(amount_), int(from_), int(to_)))

    return moves


def processMove(move, crateStacks):
    (amount_, from_, to_) = move
    pickedCrates = crateStacks[from_][-amount_:]
    pickedCrates.reverse()
    crateStacks[from_][-amount_:] = []
    crateStacks[to_] += pickedCrates


def getCratesOnTopAfterRearrangement(input, moveCrates=processMove):
    (iptCrates, iptMoves) = input.split("\n\n")
    crateStacks = parseCrateStacks(iptCrates)
    moves = parseMoves(iptMoves)
    for move in moves:
        moveCrates(move, crateStacks)
    cratesOnTop = list(map(peekTop, crateStacks[:]))
    return ''.join(cratesOnTop)


def peekTop(stack):
    if len(stack) == 0:
        return ''
    else:
        return stack[-1]
