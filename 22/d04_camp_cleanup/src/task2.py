import re

def numberOverlappingPairs(scheudule):
    return sum(list(map(areOverlapping,scheudule.strip().split("\n"))))

def areOverlapping(pairAssignment):
    """Verifies weather any of the two given assignemnts is fully contained by another. An assignemnt is a string of two integer numbers.

    Args:
        pairAssignment (string): Is a string of the form "num1-num2, num3-num4".

    Returns:
        boolean: True, if any of the assignemnt fully contains another. 
    """
    (s1,e1,s2,e2) = list(map(int,re.findall(r'\d+',pairAssignment)))
    overlap = None
    if e1 < s2:
        overlap = False
    elif s1 > e2:
        overlap = False
    else:
        overlap = True
    return overlap