import random
import time
import os
from math import factorial

def askPromptInt(prompt) -> int:
    try:
        input_number = int(input(f"{prompt} : "))
        return input_number
    except ValueError:
        return askPromptInt(prompt)

def askPromptStr(prompt) -> str:
    input_number = input(f"{prompt} ")
    return input_number

def askForOperators(numberOfAsking) -> list:
    numberAsked = 1
    list_operator : list = []
    while numberAsked <= numberOfAsking:
        operator = askPromptStr(f"N°{numberAsked} What operator do you want to use (+,-,*,/) ? ")
        while operator not in ["+","-","*","/"]:
            operator = askPromptStr(f"N°{numberAsked} What operator do you want to use (+,-,*,/) ? ")
        list_operator.append(operator)
        numberAsked += 1
    return list_operator


def gameSolver(list_number, list_operator, wanted_result, stop_at_first , equationPossibility):
    answers : list = []
    list_tries : list = []
    result = 0
    start_time = 0
    number_try = 0

    odd_number : list = [] # List of odd number
    for i in range(3,10): # Loop through the range 3 to 10
        if i % 2 != 0: # If the number is odd
            odd_number.append(i) # Add the number to the list

    while True:
        equations : list = []
        temp_list_operator = list_operator.copy() # Copy the list of operator
        random.shuffle(list_number) # Shuffle the list of number
        random.shuffle(temp_list_operator) # Shuffle the list of operator
        dict_number : dict = {}
        for i in range(0,len(list_number)): # Loop through the list
            dict_number.update({f"number_{i+1}":list_number[i]})

        boolParenthese = bool(random.randint(0,1)) # 0 = False, 1 = True
        for k,v in dict_number.items(): # Loop through the dict
            equations.append(v) # Add the number to the equations
            if k != list(dict_number.keys())[-1]: # If the number is not the last number of the list
                operator = temp_list_operator[0] # Get the first operator of the list
                equations.append(operator) # Add the operator to the equations
                temp_list_operator.remove(operator) # Remove the operator from the list

        if boolParenthese: # If boolParenthese is True
            maxIndexInsertParentheseOpen = 5 # Max index where the program can insert a parenthese
            indexInsertParentheseOpen = random.randint(0,maxIndexInsertParentheseOpen) # Get a random index where the program can insert a parenthese
            if not isinstance(equations[indexInsertParentheseOpen],int): # If the index is not a number
                equations.insert(indexInsertParentheseOpen-1,"(") # Insert the parenthese before the index
            else:
                equations.insert(indexInsertParentheseOpen,"(") # Insert the parenthese before the index

        if "(" in equations: # If there is a parenthese in the equations
            indexParentheseOpen = equations.index("(") # Get the index of the first parenthese
            random_odd_number = random.choice(odd_number) # Get a random odd number
            indexParentheseClose = indexParentheseOpen + random_odd_number # Get the index of the close parenthese
            while indexParentheseClose >= len(equations): # If the index of the close parenthese is higher than the length of the equations
                index_odd_number = odd_number.index(random_odd_number) # Get the index of the random odd number
                random_odd_number = random.choice(odd_number[:index_odd_number]) # Get a random odd number before the previous random odd number
                indexParentheseClose = indexParentheseOpen + random_odd_number # Get the index of the close parenthese
            equations.insert(indexParentheseClose+1, ")") # Insert the close parenthese after the index
        equations_str = "".join(str(e) for e in equations) # Convert the list to a string
        if equations_str not in list_tries: # If the equations is not in the list of tries
            list_tries.append(equations_str) # Add the equations to the list of tries
            try: # Try to eval the equations
                result = eval(equations_str) # Eval the equations
                number_try += 1 # Add 1 to the number of try
                if result == wanted_result: # If the result is equal to the wanted result
                    answers.append(equations_str) # Add the equations to the list of answers
                    if stop_at_first == True: # If stop_at_first is True
                        break # Stop the program
            except Exception as e: # If the equations can't be eval
                print(e)
            start_time = time.time() # Get the current time

        current_time = time.time() # Get the current time
        if len(answers) > 1:
            if len(answers) == equationPossibility:
                break
            else:
                print(len(answers))
        elif current_time-start_time >= 10:
            print("The program stop because it didn't found any equations in 10sec")
            break # Stop the program
    return answers, dict_number, number_try # Return the answers, the dict of number and the number of try

def runProgram(list_number:list, list_operator:list, wanted_result:int, stop_at_first:bool, WANTALLRESULT:bool, EQUATION_POSSIBILITY:int):
    programStartingTime = time.time()
    answers, dict_number, number_try = gameSolver(list_number, list_operator, wanted_result, stop_at_first, EQUATION_POSSIBILITY)
    programEndingTime = time.time()
    if len(answers) == 0:
        print(f"You can't build an equation that is equal to {wanted_result} with these number => {','.join(str(n) for n in dict_number.values())}")
    else:
        if not stop_at_first and WANTALLRESULT:
            for i in answers:
                print(i)
        else:
            print(f"Here is the first correct equations found : {answers[0]}")
        print(f"There are {len(answers)} answers. Found in {number_try} combination")
    print(f"Program executed in {programEndingTime-programStartingTime} sec")


def calculate_possibilities(list_number:list, list_operator:list):
    num_arrangements = factorial(len(list_number)) # Calculate the number of ways to arrange numbers
    num_operator_positions = factorial(len(list_number) - 1) // factorial(len(list_number) - 1 - len(list_operator)) # Calculate the number of ways to choose positions for operators
    num_operator_arrangements = factorial(len(list_operator)) # Calculate the number of ways to arrange operators
    total_possibilities = num_arrangements * num_operator_positions * num_operator_arrangements # Calculate the total number of possibilities
    print(f"Total number of possibilities: {total_possibilities}")
    return total_possibilities



def main():
    os.system("cls")
    TEST_MODE = askPromptStr("Do you want to use test mode ? (y/n) ").lower() == "y"
    ENABLESTATS = askPromptStr("Do you want to enable stats ? (y/n) ").lower() == "y"
    WANTALLRESULT = False
    STOPATFIRST = False
    NUMBEROFTRY = 1000
    STATS = {
        "averageNumberOfTry": 0,
        "averageTime": 0
    }
    DEFAULT_LIST_NUMBER = [1,2,3,4]
    DEAFAULT_RESULT = 10
    DEFAULT_OPERATOR = ["+","-","*"]

    if not TEST_MODE:
        number_number = askPromptInt('How much number do you need')
        while number_number < 3:
            print("Number need to be higher than 3")
            askPromptInt('How much number do you need')

        wanted_result = askPromptInt('What result do you want')
        for i in range(0,number_number):
            number = askPromptInt(f"Number {i+1}")
            list_number.append(number)

        list_operator = askForOperators(number_number-1)
    else:
        list_operator = DEFAULT_OPERATOR
        list_number = DEFAULT_LIST_NUMBER
        wanted_result = DEAFAULT_RESULT

    EQUATION_POSSIBILITY = calculate_possibilities(list_number, list_operator)
    runProgram(list_number, list_operator, wanted_result, STOPATFIRST, WANTALLRESULT, EQUATION_POSSIBILITY)

    if ENABLESTATS:
        for i in range(0,NUMBEROFTRY):
            programStartingTime = time.time()
            answers, dict_number, number_try = gameSolver(list_number, list_operator, wanted_result, STOPATFIRST, EQUATION_POSSIBILITY)
            programEndingTime = time.time()
            
            STATS["averageNumberOfTry"] += number_try
            STATS["averageTime"] += programEndingTime-programStartingTime

        STATS["averageNumberOfTry"] = STATS["averageNumberOfTry"]/NUMBEROFTRY
        STATS["averageTime"] = STATS["averageTime"]/NUMBEROFTRY
        print(STATS)


if __name__ == "__main__":
    main()