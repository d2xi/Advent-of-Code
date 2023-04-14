import functools

def mostCaloriesCarried(inventory):
    """
    The function calculates from the given string  representing the food inventories of all elves, which elve carries the most callories in the group. 
    Args:
        inventory (string): An empty string or a string consisting of several lines, where each line is an integer or an empty line(an inventory separator). Each block of intergers is a inventory of an elve.

    Returns:
        string: The biggest carried callorie count in the group.
    """
    listOfStrings = inventory.split("\n\n")
    if listOfStrings == ['']:
        return 0
    listOfIntlists = [list(map(int, substring.split('\n'))) for substring in listOfStrings]
    totalCaloriesPerElve = map(sum,listOfIntlists)
    return max(totalCaloriesPerElve)

def sumTopThreeCarriedCalories(inventory):
    listOfStrings = inventory.split("\n\n")
    if listOfStrings == ['']:
        return 0
    listOfIntlists = [list(map(int, substring.split('\n'))) for substring in listOfStrings]
    totalCaloriesPerElve = list(map(sum,listOfIntlists))
    topThree = sorted(totalCaloriesPerElve)[-3:]
    return sum(topThree)

if __name__=='__main__':
    input = None
    try:
        with open('input.txt', 'r') as file:
            input = file.read().strip()
    except FileNotFoundError:
        print("File not found. Please provide a valid file name.")
    except Exception as e:
        print("Error occurred while reading the file:", e)
    else:
        print("Task1", mostCaloriesCarried(input))
        print("Taks2", sumTopThreeCarriedCalories(input))