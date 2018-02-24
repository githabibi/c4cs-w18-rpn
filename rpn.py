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

def printHistory(history):
    if len(history) == 3:
        answer = history.pop()
        token = history.pop()
        arg = history.pop()
        return str(arg) + " " + str(token) + \
                " = " + str(answer)
    elif len(history) == 4:
        answer = history.pop()
        token = history.pop()
        arg2 = history.pop()
        arg1 = history.pop()
        return str(arg1) + " " + str(token) + " " + str(arg2) \
                + " = " + str(answer)
    else:
        raise TypeError

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '!': factorial,
    'history()': printHistory,
}

def calculate(arg):
    stack = list()
    history = list()
    for token in arg.split():
        try:
            value = float(token)
            stack.append(value)
        except ValueError:
            function = operators[token]
            result = 0
            if function == factorial:
                arg = stack.pop()
                history.append(arg)
                history.append(token)
                result = function(arg)
            elif function == printHistory:
                return printHistory(history)
            else:
                arg2 = stack.pop()
                arg1 = stack.pop()
                history.append(arg1)
                history.append(arg2)
                history.append(token)
                result = function(arg1, arg2) 
            history.append(result)
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
