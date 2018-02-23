#!/usr/bin/env python3

def calculate(arg):
    stack = list()
    for token in arg.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            if token == '+':
                arg1 = stack.pop()
                arg2 = stack.pop()
                result = arg1 + arg2
                stack.append(result)
            elif token == '-':
                arg1 = stack.pop()
                arg2 = stack.pop()
                result = arg2 - arg1
                stack.append(result)
            else:
                print('%s is not an operator.' % token)
        print(stack)
    return stack.pop()

def main():
    while True:
        print(calculate(input('rpn calc> ')))

if __name__ == '__main__':
    main()
