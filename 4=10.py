import random
import time

def askPrompt(prompt) -> list|bool :
    try:
        input_number = int(input(f"{prompt} : "))
        return input_number
    except ValueError:
        return askPrompt(prompt)


list_number : list = []
answers : list = []
list_operator : list = ["*", "/", "+", "-"]
list_tries : list = []
number_try = 0
start_time = 0
result = 0
odd_number : list = [] # [3,5,7,9]

for i in range(3,10):
    if i % 2 != 0:
        odd_number.append(i)

number_number = askPrompt('How much number do you need')
while number_number < 3:
    print("Number need to be higher than 3")
    askPrompt('How much number do you need')

wanted_result = askPrompt('What result do you want')
for i in range(0,number_number):
    number = askPrompt(f"Number {i+1}")
    list_number.append(number)

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
            print(f"Try n°{number_try} => {equations_str}")
            if result == wanted_result:
                answers.append(equations_str)
        except Exception as e:
            pass
        start_time = time.time()

    current_time = time.time()
    if int(current_time-start_time) > 10: # If the previous equations was found more than 10sec ago the program stop
        break


if len(answers) == 0:
    print(f"You can't build an equation that is equal to {wanted_result} with these number => {','.join(str(n) for n in dict_number.values())}")
else:
    print(f"Here is the first correct equations found : {answers[0]}")
    print(f"There are {len(answers)} answers. Found in {number_try} combination")