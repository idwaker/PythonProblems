# Algorithms & Data Structures: Implementing a Stack
# 12.21.15
# @totallygloria


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        return self.items

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def contains_items(self):
        return len(self.items) > 0

    def size(self):
        return len(self.items)


def rev_string(input_string):
    stack = Stack()
    new_string = str()

    for char in input_string:
        stack.push(char)

    while stack.contains_items():
        new_string += stack.pop()
    return new_string


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


def match_checker(char, prior):
    matches = [('(', ')'), ('[', ']'), ('{', '}'), ('<', '>')]
    for opening, closing in matches:
        if char == closing and prior == opening:
            return "Balanced."
    return "Unbalanced."


def int_to_bin(value):
    stack = Stack()
    num = int(value)
    binary_num = ''

    while num > 0:
        stack.push(num % 2)
        num //= 2
    while stack.contains_items():
        binary_num += str(stack.pop())
    return binary_num


'''
if int_to_bin(233) == '11101001':
    print "233 equals", int_to_bin(233)
else:
    print "Doesn't work."
'''


def base_converter():
    stack = Stack()
    digits = '0123456789ABCDEF'
    num = int(raw_input('Enter a number to convert: '))
    base = int(raw_input('Enter a base to convert to: '))
    new_num = ''

    while num > 0:
        stack.push(num % base)
        num //= base

    while stack.contains_items():
        new_num += str(digits[stack.pop()])
    return new_num


base_converter()
