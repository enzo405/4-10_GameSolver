
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