def genInputString(list):
    """
    Converts given lists of interger lists into a string where each element of a sublist is on a new line and sublists elements are separated by the empty line.
    Args:
        list (list of integer lists): List of list integers

    Returns:
        string: A string
    """
    inventory = '\n\n'.join(['\n'.join(map(str, sublist)) for sublist in list])
    return inventory
