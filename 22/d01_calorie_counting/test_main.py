import tkit
import main

def test_mostCaloriesCarried():
    testCases = [] 
    testCases.append((24000, [[1000,2000,300],[4000],[5000,6000],[7000,8000,9000],[10000]]))
    testCases.append((24, [[1,2,3],[4],[5,6],[7,8,9],[10]]))
    testCases.append((0, []))
    
    for tc in testCases:
        expected, testCase = tc[0], tkit.genInputString(tc[1])
        assert main.mostCaloriesCarried(testCase) == expected


def test_getSumTopThreeCarriedCalories():
    testCases = [] 
    testCases.append((45000, [[1000,2000,300],[4000],[5000,6000],[7000,8000,9000],[10000]]))
    testCases.append((45, [[1,2,3],[4],[5,6],[7,8,9],[10]]))
    testCases.append((0, []))
    
    for tc in testCases:
        expected, testCase = tc[0], tkit.genInputString(tc[1])
        assert main.sumTopThreeCarriedCalories(testCase) == expected