## UTILS
def calculate_possibilities(nbrC:int, nbrO:int):
    """
    Author: Spirygo
    Co-Author: github/enzo405
    with nbrC equal to the number of number
    with nbrO equal to the number of operator
    """
    result = 0

    def factorial(n):
        if n == 1:
            return 1
        else:
            return n * factorial(n-1)

    for i in range(1, nbrC):
        calc = (nbrC**(nbrC-i) * nbrO**(nbrC-i) * nbrC**i * nbrO**(i-1)) 
        result += calc * factorial(nbrC //2) 
    return result