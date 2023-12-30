import time
import os
from utils.calculatePossibility import calculate_possibilities
from utils.promptUtils import askPromptInt, askPromptStr, askForOperators
from program import runProgram


def main():
    # Initialize Default Variables
    WANTALLRESULT = False
    STOPATFIRST = False
    NUMBEROFTRY = 1000
    DEFAULT_LIST_NUMBER = [1,2,3,4]
    DEFAULT_RESULT = 10
    DEFAULT_OPERATOR = ["+","-","*"]

    # Ask User Prompt
    os.system("cls")
    TEST_MODE = askPromptStr("Do you want to use test mode ? (y/n) ").lower() == "y"
    ENABLESTATS = askPromptStr("Do you want to enable stats ? (y/n) ").lower() == "y"

    # Initialize Variables
    STATS = {
        "averageNumberOfTry": 0,
        "averageTime": 0
    }

    if not TEST_MODE:
        # Choose the number of number
        number_number = askPromptInt('How much number do you need')
        while number_number < 3:
            print("Number need to be higher than 3")
            askPromptInt('How much number do you need')

        # Choose what result you want
        wanted_result = askPromptInt('What result do you want')
        
        # Choose the number to test
        for i in range(0,number_number):
            number = askPromptInt(f"Number {i+1}")
            list_number.append(number)

        list_operator = askForOperators(number_number-1)
    else:
        list_operator = DEFAULT_OPERATOR
        list_number = DEFAULT_LIST_NUMBER
        wanted_result = DEFAULT_RESULT

    # Calculate the number of possibilities
    EQUATION_POSSIBILITY = calculate_possibilities(len(list_number), len(list_operator))
    print(f"There are {EQUATION_POSSIBILITY} possibilities")

    # Run the program
    runProgram(list_number, list_operator, wanted_result, STOPATFIRST, WANTALLRESULT, EQUATION_POSSIBILITY)

    # Run the program multiple time to get stats
    if ENABLESTATS:
        for i in range(0,NUMBEROFTRY):
            programStartingTime = time.time() # TODO le RunProgram est pas bon ici
            answers, dict_number, number_try = runProgram(list_number, list_operator, wanted_result, STOPATFIRST, EQUATION_POSSIBILITY)
            programEndingTime = time.time()
            
            STATS["averageNumberOfTry"] += number_try
            STATS["averageTime"] += programEndingTime-programStartingTime

        STATS["averageNumberOfTry"] = STATS["averageNumberOfTry"]/NUMBEROFTRY
        STATS["averageTime"] = STATS["averageTime"]/NUMBEROFTRY
        print(STATS)


if __name__ == "__main__":
    main()