import numpy as np

import sys

from ex1_common_methods import batch_mode_method, is_symmetric, is_positive_definite, newton_based_method, gradient_based_method, J_function

yes = ['y', 'yes', 'Y', 'Yes']
line = '============================================================'
def tui():

    print(chr(27) + "[2J")
    print(line)

    try:

        in_text = input('=   Please input vector B (i.e.: 1,2,3) : ')
        vector_b = format_input(in_text, ',')
        vector_len = len(vector_b)
        vector_b = np.asarray(vector_b).astype(np.float)

        vector_temp = []

        print('=   Please input symmetric matrix with dimension {n}x{n}'.format(n=vector_len) + ': ')
        for x in range(0, vector_len):
            in_text = input('=   Please input {n}th row of matrix A (i.e.: 1,2,3) : '.format(n=x))
            vector_temp.append(format_input(in_text, ','))

        matrix_a = np.asarray(vector_temp).astype(np.float)

        if not (is_symmetric(matrix_a) and is_positive_definite(matrix_a)):
            raise ValueError

        scalar_c = int(input('=   Please input scalar C (integer) : '))
        if not isinstance(scalar_c, int):
            raise ValueError

        print_variables(matrix_a, vector_b, scalar_c)

        print(line)
        print('=   Please define starting point')
        start_point = input('=   in example: "1" - integer or "1, 2" - range: ')
        start_point = format_input(start_point, ',')

        if len(start_point) == 1:
            start_point.append(start_point[0])

        if not (len(start_point) == 2):
            raise ValueError

        run_method(matrix_a, vector_b, scalar_c, start_point)
        print(line)

        ans = 'y'
        while ans in yes:
            ans = input('=   Would you like run another method (y | n):')
            if ans in yes:
                run_method(matrix_a, vector_b, scalar_c, start_point)
                print(line)

    except ValueError:
        error = 'Defined input variables are incorrect! Please define valid one!'
        print_error(error)
    except np.linalg.LinAlgError:
        error = 'Defined matrix is not a positive-definite! Please input valid one!'
        print_error(error)

    ans = input('=   Would you like input new variables (y | n):')
    if ans in yes:
        tui()
    else:
        sys.exit()


def run_method(_matrix_a, _vector_b, _scalar_c, _start_point):
    batch_mode = False

    ans = input('=   Would you like run with batch mode (y | n): ')
    if ans in yes:
        batch_mode = True
        batch_n = int(input('=   Please specify N: '))
        if not batch_n <= 100:
            raise ValueError

    ans = int(input('=   Which method would you like run (gradient: 1, newton: 2) : '))

    if batch_mode:
        if ans == 1:
            print('=   Batch mode simple gradient method executed')
            print(line)
            sol = batch_mode_method('gradient', int(batch_n), _matrix_a, _vector_b, _scalar_c, _start_point)

        if ans == 2:
            print('=   Batch mode Newtons method executed')
            print(line)
            sol = batch_mode_method('newton', int(batch_n), _matrix_a, _vector_b, _scalar_c, _start_point)

        print("=   Obtained solutions for each program execution")
        print(np.array(sol))

    else:
        if ans == 1:
            print('=   Based mode gradient method executed')
            print(line)
            sol = gradient_based_method(_matrix_a, _vector_b, _scalar_c, _start_point)

        if ans == 2:
            print('=   Based mode newton method executed')
            print(line)
            sol = newton_based_method(_matrix_a, _vector_b, _scalar_c, _start_point)

        print('Result = ', sol)
        print('J(x) = ', J_function(_matrix_a, _vector_b, _scalar_c, sol))


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


"""
Printing a input variable for the task
input: matrix, vector, scalar
output: n/a
"""


def print_variables(matrix, vector, scalar):
    print(line)
    print('=   Defined variables:')
    print('=   Matrix:\n')
    print(matrix)
    print('\n=   Vector:\n')
    print(vector)
    print('\n=   Scalar: ' + str(scalar))


if __name__ == "__main__":
    tui()
