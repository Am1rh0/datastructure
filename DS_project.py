def infix_to_postfix(expression):
    operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []

    for char in expression:
        if char.isalpha() or char.isdigit():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and operators.get(char, 0) <= operators.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return ''.join(output)

# infix_expression = "(a+b)*(c-d)/e"
# postfix_expression = infix_to_postfix(infix_expression)
# print("Postfix Expression:", postfix_expression)



def infix_to_prefix(expression):
    operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []

    for char in reversed(expression):
        if char.isalpha() or char.isdigit():
            output.append(char)
        elif char == ')':
            stack.append(char)
        elif char == '(':
            while stack and stack[-1] != ')':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and operators.get(char, 0) <= operators.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return ''.join(reversed(output))

# infix_expression = "(a+b)*(c-d)/e"
# prefix_expression = infix_to_prefix(infix_expression)
# print("Prefix Expression:", prefix_expression)



def prefix_to_infix(expression):
    stack = []

    for char in reversed(expression):
        if char.isalnum():
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            result = '(' + operand1 + char + operand2 + ')'
            stack.append(result)

    infix = stack.pop()

    return infix

# prefix_expression = "+*AB-CDE"
# infix_expression = prefix_to_infix(prefix_expression)
# print(infix_expression)



def prefix_to_postfix(expression):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])

    for char in expression[::-1]:
        if char in operators:
            operand1 = stack.pop()
            operand2 = stack.pop()
            postfix = operand1 + operand2 + char
            stack.append(postfix)
        else:
            stack.append(char)

    return stack.pop()

# prefix_expression = "+*AB-CDE"
# postfix_expression = prefix_to_postfix(prefix_expression)
# print(postfix_expression)



def postfix_to_infix(expression):
    stack = []

    for char in expression:
        if char.isalnum():
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            infix = '(' + operand1 + char + operand2 + ')'
            stack.append(infix)

    return stack.pop()

# postfix_expression = "ab+"
# infix_expression = postfix_to_infix(postfix_expression)
# print(infix_expression)



def postfix_to_prefix(expression):
    stack = []

    for char in expression:
        if char.isalnum():
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            prefix = char + operand1 + operand2
            stack.append(prefix)

    return stack.pop()

# postfix_expression = "ab+"
# prefix_expression = postfix_to_prefix(postfix_expression)
# print(prefix_expression)



def evaluate_postfix_expression(expression):
    operand_stack = []

    for c in expression:
        if c.isdigit():
            operand_stack.append(int(c))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()

            if c == '+':
                operand_stack.append(operand1 + operand2)
            elif c == '-':
                operand_stack.append(operand1 - operand2)
            elif c == '*':
                operand_stack.append(operand1 * operand2)
            elif c == '/':
                operand_stack.append(operand1 / operand2)
            elif c == '^':
                operand_stack.append(operand1 ** operand2)
            else:
                print("Invalid operator:", c)
                return 0

    return operand_stack.pop()

# postfix_expression = "7245*+"
# result = evaluate_postfix_expression(postfix_expression)
# print("your expression evaluate result is:", result)



def evaluate_prefix_expression(expression):
    operand_stack = []

    for c in reversed(expression):
        if c.isdigit():
            operand_stack.append(int(c))
        else:
            operand1 = operand_stack.pop()
            operand2 = operand_stack.pop()

            if c == '+':
                operand_stack.append(operand1 + operand2)
            elif c == '-':
                operand_stack.append(operand1 - operand2)
            elif c == '*':
                operand_stack.append(operand1 * operand2)
            elif c == '/':
                operand_stack.append(operand1 / operand2)
            elif c == '^':
                operand_stack.append(operand1 ** operand2)
            else:
                print("Invalid operator:", c)
                return 0

    return operand_stack.pop()

# prefix_expression = "+*132"
# result = evaluate_prefix_expression(prefix_expression)
# print("your expression evaluate result is:", result)



def detect_notation(expression):
    operators = set(['+', '-', '*', '/','^'])
    stack = []

    for char in expression:
        if char in operators:
            stack.append(char)
        elif char.isalnum():
            stack.append(char)

    operand_count = sum([1 for char in stack if char.isalnum()])
    operator_count = sum([1 for char in stack if char in operators])

    if operator_count == operand_count - 1:
        return "Postfix Notation"
    elif operator_count == operand_count - 1:
        return "Prefix Notation"
    else:
        return "Infix Notation"

# expression = "+ 3 4"
# notation_type = detect_notation(expression)
# print(f"The expression '{expression}' is in {notation_type}.")



def expression_validation(expression):
    if expression[0] in "+-*/^":
        return 'prefix'
    elif expression[-1] in "+-*/^":
        return 'postfix'
    else:
        return 'infix'
    
# expression = "a+b"
# valiation_expression = expression_validation(expression)
# print(valiation_expression)

    