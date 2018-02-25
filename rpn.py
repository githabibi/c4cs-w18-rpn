#!/usr/bin/env python3

import sys
import operator
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
logger.addHandler(ch)

history = list()

def factorial(base):
    if base < 0:
        raise ArithmeticError
    if base == 0:
        return 1
    return base * factorial(base-1)

def printHistory():
    global history
    output = None
    if len(history) == 3:
        answer = history.pop()
        token = history.pop()
        arg = history.pop()
        output = str(arg) + " " + str(token) + \
                 " = " + str(answer)
    elif len(history) == 4:
        answer = history.pop()
        token = history.pop()
        arg2 = history.pop()
        arg1 = history.pop()
        output = str(arg1) + " " + str(token) + \
                 " " + str(arg2) + " = " + str(answer)

    if (len(history) > 0):
        raise TypeError
    if (output is None):
        output = "No history is present"
    return output


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '!': factorial,
    'history()': printHistory,
}

def calculate(arg):
    global history
    stack = list()
    for token in arg.split():
        try:
            value = float(token)
            stack.append(value)
        except ValueError:
            function = operators[token]
            result = 0
            if function == factorial:
                history = list()
                arg = stack.pop()
                history.append(arg)
                history.append(token)
                result = function(arg)
            elif function == printHistory:
                return printHistory()
            else:
                history = list()
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
