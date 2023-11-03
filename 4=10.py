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

def gameSolver(list_number, wanted_result, stop_at_first):
    answers : list = []
    list_tries : list = []
    list_operator : list = ["*", "/", "+", "-"]
    result = 0
    start_time = 0
    number_try = 0

    odd_number : list = [] # [3,5,7,9]
    for i in range(3,10):
        if i % 2 != 0:
            odd_number.append(i)

    while True:
        equations : list = []
        random.shuffle(list_number)
        dict_number : dict = {}
        for i in range(0,len(list_number)):
            dict_number.update({f"number_{i+1}":list_number[i]})
        
        boolParenthese = bool(random.randint(0,1))
        for k,v in dict_number.items():
            random_number_operator = random.randint(0,len(list_operator)-1)
            operator = list_operator[random_number_operator]

            equations.append(v)
            if k != list(dict_number.keys())[-1]:
                equations.append(operator)

        if boolParenthese:
            maxIndexInsertParentheseOpen = 5
            indexInsertParentheseOpen = random.randint(0,maxIndexInsertParentheseOpen)
            if not isinstance(equations[indexInsertParentheseOpen],int):
                equations.insert(indexInsertParentheseOpen-1,"(")
            else:
                equations.insert(indexInsertParentheseOpen,"(")

        if "(" in equations:
            indexParentheseOpen = equations.index("(")
            random_odd_number = random.choice(odd_number)
            indexParentheseClose = indexParentheseOpen + random_odd_number
            while indexParentheseClose >= len(equations):
                index_odd_number = odd_number.index(random_odd_number)
                random_odd_number = random.choice(odd_number[:index_odd_number])
                indexParentheseClose = indexParentheseOpen + random_odd_number
            equations.insert(indexParentheseClose+1, ")")
        equations_str = "".join(str(e) for e in equations)

        if equations_str not in list_tries:
            list_tries.append(equations_str)
            try:
                result = eval(equations_str)
                number_try += 1
                if result == wanted_result:
                    answers.append(equations_str)
                    if stop_at_first == True:
                        break
            except Exception:
                pass
            start_time = time.time()

        current_time = time.time()
        if int(current_time-start_time) > 10: # If the previous equations was found more than 10sec ago the program stop
            break
    return answers, dict_number, number_try



def main():
    list_number : list = []
    answer_yes : list = ["oui", "yes"]
    stop_at_first : bool = False

    number_number = askPromptInt('How much number do you need')
    while number_number < 3:
        print("Number need to be higher than 3")
        askPromptInt('How much number do you need')

    wanted_result = askPromptInt('What result do you want')
    for i in range(0,number_number):
        number = askPromptInt(f"Number {i+1}")
        list_number.append(number)

    os.system("cls")

    programStartingTime = time.time()
    # Run the Solving program
    answers, dict_number, number_try = gameSolver(list_number, wanted_result, stop_at_first)

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

main()