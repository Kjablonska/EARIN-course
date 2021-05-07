import numpy as np
import sys
from main import run_method

yes = ['y', 'yes', 'Y', 'Yes']
line = '============================================================'


def tui():
    print(chr(27) + "[2J")
    print(line)
    print('=   Authors: ')
    print('=   - Karolina Jablonska, 295814')
    print('=   - Wojciech Marosek, 295818')
    print(line)
    print('=   EARIN | Exercise 5 | Bayesian networks using the MCMC algorithm')
    print(line)

    try:
        name = input('=   Please input the name of .json file (alarm.json) : ')
        evidence = ''
        query = ''
        steps = ''

        if not name.endswith('.json'):
            raise ValueError

        option_enum = ['mcmc', 'markov_blanket']
        option = int(
            input('=   Please define the method by 0 ({}) or 1 ({})  : '.format(option_enum[0], option_enum[1])))

        if option == 0:
            evidence, query, steps = tui_mcmc()
        elif option == 1:
            evidence = input('=   Please input node (ie: burglary): ')
        else:
            raise ValueError

        print(line)
        run_method(name, evidence, query, steps, option_enum[option])

        ans = 'y'
        while ans in yes:
            print(line)
            ans = input('=   Would you like run {} method once again (y | n): '.format(option_enum[option]))
            if ans in yes:
                print(line)
                run_method(name, evidence, query, steps, option_enum[option])

        ans = input('=   Would you like input new variables (y | n): ')
        print(line)
        if ans in yes:
            tui()
        else:
            sys.exit()

    except ValueError:
        error = 'Defined input variables are incorrect! Please define valid one!'
        print_error(error)
    except AttributeError:
         error = 'Defined input variables are incorrect! Please define valid one!'
         print_error(error)


def tui_mcmc():
    try:
        evidence = {}
        in_text = input('=   Please input evidence with steps (ie: burglary:T): ')
        in_text = in_text.split(':')
        evidence[in_text[0]] = in_text[1]
        ans = 'y'
        while ans in yes:
            ans = input('=   Would you like add more evidence: ')
            if ans in yes:
                in_text = input('=   Please input evidence with value (ie: burglary:T): ')
                in_text = in_text.split(':')
                evidence[in_text[0]] = in_text[1]

        in_text = input('=   Please query (ie: John_calls, earthquake, alarm, Marry_calls): ')
        query = format_input(in_text, ',')

        print('=   Please define no of steps')
        steps = int(input('=   for example: "1000" - integer: '))

        return evidence, query, steps

    except ValueError:
        error = 'Defined input variables are incorrect! Please define valid one!'
        print_error(error)


"""
Converts string to the array. Responsible for fetching input data in correct format.
input: text - string, delimiter - char
output: array of delimited strings
"""
def format_input(text, delimiter):
    text = text.replace(' ', '')
    text = text.split(delimiter)
    return text


"""
Printing a error message and asking user next execution of program
input: error - String
output: n/a
"""
def print_error(error):
    yes = ['y', 'yes', 'Y', 'Yes']

    print('=\n=   ' + error)
    ans = input('=   Would you like input new variables (y | n):')
    if ans in yes:
        tui()
    else:
        sys.exit()


if __name__ == "__main__":
    tui()
