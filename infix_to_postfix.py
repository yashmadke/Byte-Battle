def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    else:
        return 0

def infix_to_postfix(infix):
    postfix = []
    stack = []

    for char in infix:
        if char.isalnum():  # Operand
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # Discard '('
        else:  # Operator
            while stack and precedence(stack[-1]) >= precedence(char):
                postfix.append(stack.pop())
            stack.append(char)

    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)


infix_expression = "(a+b)*c+(d*e+f)"
postfix_expression = infix_to_postfix(infix_expression)
print("Infix expression:", infix_expression)
print("Postfix expression:", postfix_expression)