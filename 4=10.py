import random
import time
import os

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


def gameSolver(list_number, wanted_result, stop_at_first, list_operator):
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
            except Exception: # If the equations can't be eval
                pass # Pass the error
            start_time = time.time() # Get the current time

        current_time = time.time() # Get the current time
        if int(current_time-start_time) > 10: # If the previous equations was found more than 10sec ago the program stop
            print("The program stop because it didn't found any equations in 10sec")
            break # Stop the program
    return answers, dict_number, number_try # Return the answers, the dict of number and the number of try

def getUserConfig(test_mode):
    if not test_mode:
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
        list_number = [2,5,0,3]
        wanted_result = 10
        number_number = len(list_number)
        list_operator = ["+","-","*","/"]
    return list_number, wanted_result, number_number, list_operator


def main(test_mode):
    list_number : list = []
    answer_yes : list = ["oui", "yes"]
    stop_at_first : bool = True

    list_number, wanted_result, number_number, list_operator = getUserConfig(test_mode)
    
    os.system("cls")

    programStartingTime = time.time()
    # Run the Solving program
    answers, dict_number, number_try = gameSolver(list_number, wanted_result, stop_at_first, list_operator)

    os.system('cls')
    programEndingTime = time.time()

    if len(answers) == 0:
        print(f"You can't build an equation that is equal to {wanted_result} with these number => {','.join(str(n) for n in dict_number.values())}")
    else:
        wantAllResult = askPromptStr('Do you want to see all result ?')
        os.system("cls")
        if str.lower(wantAllResult) in answer_yes:
            for i in answers:
                print(i)
        else:
            print(f"Here is the first correct equations found : {answers[0]}")
        print(f"There are {len(answers)} answers. Found in {number_try} combination")
    print(f"Program executed in {programEndingTime-programStartingTime} sec")

def makeStats(test_mode, number_of_try=1000):
    stats = {
        "averageNumberOfTry": 0,
        "averageTime": 0
    }
    for i in range(0,number_of_try):
        list_number, wanted_result, number_number, list_operator = getUserConfig(test_mode)

        programStartingTime = time.time()
        answers, dict_number, number_try = gameSolver(list_number, wanted_result, True, list_operator)
        programEndingTime = time.time()
        
        stats["averageNumberOfTry"] += number_try
        stats["averageTime"] += programEndingTime-programStartingTime

    stats["averageNumberOfTry"] = stats["averageNumberOfTry"]/number_of_try
    stats["averageTime"] = stats["averageTime"]/number_of_try
    print(stats)


if __name__ == "__main__":
    TEST_MODE = True
    # main(TEST_MODE)
    makeStats(TEST_MODE)