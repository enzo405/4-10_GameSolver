import random

def askPrompt() -> list|bool :
    try:
        number_1 = int(input("Write the 1st number : "))
        number_2 = int(input("Write the 2nd number : "))
        number_3 = int(input("Write the 3rd number : "))
        number_4 = int(input("Write the 4th number : "))
        return [number_1, number_2, number_3, number_4]
    except:
        return False

list_number = askPrompt()
while list_number == False:
    list_number = askPrompt()

answers : list = []
list_operator : list = ["*", "/", "+", "-"] 
list_tries : list = []
number_try = 0
gap_tries = 0
result = 0
odd_number : list = [] # [3,5,7,9]
for i in range(3,10):
    if i % 2 != 0:
        odd_number.append(i)


while True:
    equations : list = []
    random.shuffle(list_number)
    dict_number : dict = {
        "number_1": list_number[0],
        "number_2": list_number[1],
        "number_3": list_number[2],
        "number_4": list_number[3]
    }

    for k,v in dict_number.items():
        random_number_parenthese = random.randint(0,1)
        random_number_operator = random.randint(0,len(list_number)-1)
        operator = list_operator[random_number_operator]

        equations.append(v)
        if k != list(dict_number.keys())[-1]:
            equations.append(operator)

    if random_number_parenthese == 1:
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
            print(f"Try n°{number_try} => {equations_str}")
            if result == 10:
                answers.append(equations_str)
        except Exception as e:
            pass
    else:
       gap_tries += 1
    
    if gap_tries >= 100000:
        break


if len(answers) == 0:
    print(f"You can't build an equation that is equal to 10 with these number => {','.join(str(n) for n in dict_number.values())}")
else:
    for answer in answers:
        print(f"The correct equations is : {answer}")
    print(f"There are {len(answers)} answers. Found in {number_try} combination")