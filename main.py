import string


def mainfunct(expression:str) -> str:
    expression= expression.replace(" ", "")
    if (expression[0].isdigit()== False and expression[0] != '('):
        raise Exception("Error")
    twoinarow = False
    for char in expression:
        if ( char.isdigit() == False and char != '('):
            if(twoinarow == True):
                raise Exception("Error")
            twoinarow = True
        else:
            twoinarow= False
    return solve_brackets(expression)
            
        
        

def solve(expression: str) -> str:
    expression = expression.replace(" ", "")
    expression = solve_mult_div(expression) 
    result = 0
    current_number = ''  
    current_operator = '+' 

    for char in expression:
        if char.isdigit():
            current_number += char  
        else:
            
            if current_operator == '+':
                result += int(current_number)
            elif current_operator == '-':
                result -= int(current_number)
            current_number = '' 
            current_operator = char 

   
    if current_operator == '+':
        result += int(current_number)
    elif current_operator == '-':
        result -= int(current_number)

    return str(result)

def solve_mult_div(expression: str) -> str:
    i = 0
    while i < len(expression):
        if expression[i] == '*':
            left_index = i - 1
            while left_index >= 0 and expression[left_index].isdigit():
                left_index -= 1
            right_index = i + 1
            while right_index < len(expression) and expression[right_index].isdigit():
                right_index += 1
            result = int(expression[left_index + 1:i]) * int(expression[i + 1:right_index])
            expression = expression[:left_index + 1] + str(result) + expression[right_index:]
            i = 0
        elif expression[i] == '/':
            left_index = i - 1
            while left_index >= 0 and expression[left_index].isdigit():
                left_index -= 1
            right_index = i + 1
            while right_index < len(expression) and expression[right_index].isdigit():
                right_index += 1
            result = int(expression[left_index + 1:i]) // int(expression[i + 1:right_index])
            expression = expression[:left_index + 1] + str(result) + expression[right_index:]
            i = 0
        i += 1
    return expression

def solve_brackets(expression: str) -> str:
    innermostleft = 0
    i = 0
    while i < len(expression):
        if expression[i] == '(':
            innermostleft = i
        if expression[i] == ')':
            expression = expression[:innermostleft] + solve(expression[innermostleft + 1: i]) + expression[i+1:]
            i = 0
            innermostleft = 0
        i=i+1

    return str(solve(expression))
    
N = int(input("Enter the number of expressions: "))
expressions = [input() for x in range(N)]

for expression in expressions:
    try:
        print(mainfunct(expression))
    except Exception as e:
        print("Error:", e)
        