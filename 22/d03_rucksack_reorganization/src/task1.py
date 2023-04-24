def findErrorsInRucksack(rucksack):
    """Find errors in the given rucksack

    Args:
        rucksack (string): String of characters ^[a-zA-Z] of even length

    Returns:
        list of letters: Returns letters are both in the first and the second half of the input string
    """
    length = len(rucksack)
    compar1 = rucksack[:length//2]
    compar2 = rucksack[length//2:]
    return list(set(compar1) & set(compar2))

def sumPriorities(errors):
    """Orders priorites to letters and sums them up.

    Args:
        errors (list of characters): A list of characters

    Returns:
        int: sum of errors
    """
    return sum(list(map(getPriority,errors)))

def getPriority(letter):
    prior = -1
    if letter.isupper():
        prior = ord(letter)-ord("A")+27
    else:
        prior = ord(letter)-ord("a")+1
    return prior

def getSumOfAllErrorPriorities(input):
    rucksacks = input.strip().split("\n")
    errorsPerRucksack = map(findErrorsInRucksack,rucksacks)
    return sum(map(sumPriorities, errorsPerRucksack))