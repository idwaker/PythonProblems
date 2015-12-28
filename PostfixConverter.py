# Algorithms & Data Structures: Implementing a Stack
# 12.28.15
# @totallygloria

from StackClass import Stack


def postfix_converter(infixstring):
    op_stack = Stack()
    output_list = []
    infix_list = infixstring.split(' ')
    operators = '*/+-'

    for char in infix_list:
        if char == '(':
            op_stack.push(char)
        elif char == ')':
            prior_op = op_stack.pop()
            while prior_op != '(':
                output_list.append(prior_op)
                prior_op = op_stack.pop()
        elif char in operators:
            if op_stack.contains_items() and op_stack.peek() in '*/':
                output_list.append(op_stack.pop())
                op_stack.push(char)
            else:
                op_stack.push(char)
        else:
            output_list.append(char)

    while op_stack.contains_items():
        output_list.append(op_stack.pop())

    return output_list


print postfix_converter('( A + B ) * ( C + D )')
print postfix_converter('A * B + C * D')
