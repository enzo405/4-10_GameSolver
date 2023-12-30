import random
import time


def runProgram(list_number:list, list_operator:list, wanted_result:int, stop_at_first:bool, WANTALLRESULT:bool, EQUATION_POSSIBILITY:int):
    # Initialize variables
    dict_number = {}
    number_try = 0
    answers = []
    programStartingTime = time.time()

    # Build all the existing equation
    equations = buildAllEq(list_number, list_operator, EQUATION_POSSIBILITY)

    # Check if the equation is equal to the wanted result
    for equation in equations:
        if eval(equation) == wanted_result:
            answers.append(equation)
            if stop_at_first:
                break

    programEndingTime = time.time()
    if len(answers) == 0:
        print(f"You can't build an equation that is equal to {wanted_result} with these number => {','.join(str(n) for n in dict_number.values())}")
    else:
        print(f"There are {len(answers)} answers. Found in {number_try} combination")
    print(f"Program executed in {programEndingTime-programStartingTime} sec")


def getAllNumbers(numbers:list) -> list:
    """
    Returns all list filled of nested list that correspond to the order of the number in the equations 
    Doesn't contains duplicates of the nested list
    """
    result : list = []

    def backtrack(nums, path, result):
        if not nums:
            result.append(path)
            return
        for i in range(len(nums)):
            new_path = path + [nums[i]]
            new_nums = nums[:i] + nums[i+1:]
            backtrack(new_nums, new_path, result)

    backtrack(numbers, [], result)
    return result


def buildEq(numbers:list, operators:list, nbrParenthese:int) -> list:
    # TODO
    print(numbers, operators, nbrParenthese)
    return []

def buildAllEq(numbers, operators):
    equations = []
    num_eq = 0
    all_numbers = getAllNumbers(numbers)
    all_operators = getAllNumbers(operators)
    max_nbrParenthese = len(numbers)//2

    for numbers in all_numbers:
        for operators in all_operators:
            for nbrParenthese in range(0,max_nbrParenthese+1):
                equation = buildEq(numbers, operators, nbrParenthese)
                equations.append(equation)
                num_eq += 1
    return equations