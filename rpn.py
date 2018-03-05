#!/usr/bin/env python3

import sys
import operator
import logging
import readline
from colored import fore, style
from fractions import Fraction
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
    answer = None
    if len(history) == 3:
        answer = history.pop()
        token = history.pop()
        arg = history.pop()
        output = fore.LIGHT_YELLOW + \
                 str(arg) + " " + str(token) + " = " + \
                 style.RESET

    elif len(history) == 4:
        answer = history.pop()
        token = history.pop()
        arg2 = history.pop()
        arg1 = history.pop()
        output = fore.LIGHT_YELLOW + \
                 str(arg1) + " " + str(token) + " " + str(arg2) + " = " + \
                 style.RESET

    if (answer is not None):
        if answer > 0:
            output += fore.GREEN + str(answer) + style.RESET
        elif answer < 0:
            output += fore.RED + str(answer) + style.RESET
        else:
            output += str(answer)

    if (output is None):
        output = "No history is present"
    return output

def fractionify(decimal):
    return str(Fraction(decimal))

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '^': operator.pow,
    '/': operator.truediv,
    '!': factorial,
    'history()': printHistory,
    'asFraction()': fractionify,
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
            if function == factorial or function == fractionify:
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
