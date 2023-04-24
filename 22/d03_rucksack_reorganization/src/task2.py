from utils import utils
from src.task1 import getPriority
from functools import reduce

def splitIntoGroups(input):
    inventories = input.strip().split("\n")
    groups = []
    while len(inventories)!=0:
        groups.append(inventories[:3])
        inventories[:3]=[]
    return groups

def identifyGroupBadge(group):
    badge = reduce(lambda s1,s2: s1&s2,map(set,group))
    return badge.pop()
 
def calculatePriorites(inventories):
    groups = splitIntoGroups(inventories)
    priorities = []
    while len(groups)!=0:
        badge = identifyGroupBadge(groups.pop())
        priorities.append(getPriority(badge))
    return sum(priorities)
    