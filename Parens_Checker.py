# Algorithms & Data Structures: Implementing a Stack
# 12.21.15
# @totallygloria

from StackImplementation import Stack

def paren_checker(string):
    stack = Stack()

    for char in string:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.contains_items():
                stack.pop()
            else:
                return 'Unbalanced'

    if stack.contains_items():
        return 'Unbalanced'
    else:
        return 'Balanced'


def general_checker(string):
    stack = Stack()
    opens = '([{<'
    closes = ')]}>'

    for char in string:
        if char in opens:
            stack.push(char)
        elif char in closes:
            if not stack.contains_items():
                return "Stack prematurely empty. Unbalanced."
            else:
                prior = stack.pop()
                return match_checker(char, prior)  # returns Balanced or Unbalanced
    if stack.contains_items():
        return 'Unbalanced'
    else:
        return 'Balanced'
