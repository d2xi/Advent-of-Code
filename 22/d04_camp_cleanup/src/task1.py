import re

def numberFullyContained(sсheudule):
    return sum(list(map(isFullyContained,sсheudule.strip().split("\n"))))

def isFullyContained(pairAssignment):
    """Verifies weather any of the two given assignemnts is fully contained by another. An assignemnt is a string of two integer numbers.

    Args:
        pairAssignment (string): Is a string of the form "num1-num2, num3-num4".

    Returns:
        boolean: True, if any of the assignemnt fully contains another. 
    """
    (s1,e1,s2,e2) = list(map(int,re.findall(r'\d+',pairAssignment)))
    isContained = None
    if s1 <= s2 and e1>=e2:
        isContained = True
    elif s1>=s2 and e1<=e2:
        isContained = True
    else:
        isContained = False
    return isContained