#!/usr/bin/env python3

import sys
import operator
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
logger.addHandler(ch)

def factorial(base):
    if base < 0:
        raise ArithmeticError
    if base == 0:
        return 1
    return base * factorial(base-1)

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '!': factorial,
}

def calculate(arg):
    stack = list()
    for token in arg.split():
        try:
            value = float(token)
            stack.append(value)
        except ValueError:
            function = operators[token]
            result = 0
            if function == factorial:
                arg = stack.pop()
                result = function(arg)
            else:
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = function(arg1, arg2) 
            stack.append(result)
        logger.debug(stack)

    if len(stack) != 1:
        raise TypeError
    return stack.pop()

def main():
    while True:
        print(calculate(input('rpn calc> ')))

if __name__ == '__main__':
    main()
