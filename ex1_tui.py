import numpy as np
import ex1_gradient_based_method as gradient
import ex1_Newton_method as newton
import sys

# definition of global variables
yes = ['y', 'yes', 'Y', 'Yes']
no = ['n', 'no', 'N', 'No']

matrix_a = ''
vector_b = ''
scalar_c = ''
start_point = ''
batch_mode = True
batch_n = ''


def tui():
    print(chr(27) + "[2J")
    print('============================================================')
    print('=')

    #   reading vector B
    try:
        in_text = input('=   Please define vector B (i.e.: 1,2,3) : ')
        vector_b = format_input(in_text, ',')
        vector_len = len(vector_b)
        vector_b = np.asarray(vector_b).astype(np.float)

        #   reading matrix A
        vector_temp = []

        print('=   Please define symetric matrix with dimension {n}x{n}'.format(n=vector_len) + ': ')
        for x in range(0, vector_len):
            in_text = input('=   Please {n} row of marix A (i.e.: 1,2,3) : '.format(n=x))
            vector_temp.append(format_input(in_text, ','))

        matrix_a = np.asarray(vector_temp).astype(np.float)

        if not (gradient.isPositiveDefinite(matrix_a) and gradient.isSymmetric(matrix_a)):
            raise ValueError

        scalar_c = int(input('=   Please define scalar C (integer) : '))
        if not isinstance(scalar_c, int):
            raise ValueError

    except:
        error = 'Defined input variables are incorrect! Please define valid one!'
        print_error(error)

    print_variables(matrix_a, vector_b, scalar_c)

    try:
        print('=   Please define starting point')
        in_text = input('=   in example: "1" - integer or "1, 2" - range: ')
        in_text = format_input(in_text, ',')
        if not (len(in_text) == 2 or len(in_text) == 1):
            raise ValueError

    except ValueError:
        error = 'Defined input variables are incorrect! Please define valid one!'
        print_error(error)

    ans = input('=   Would you like run with batch mode (y | n): ')
    if ans in yes:
        batch_mode = True
        batch_n = int(input('=   Please specify N: '))
        if not batch_n <= 100:
            raise ValueError

    ans = int(input('=   Which method would you like run (gradient: 1, newton: 2) : '))
    print('=')
    print('============================================================')

    if batch_mode:
        if ans == 1:
            print('running batch mode gradient')
            gradient.batchMode(batch_n, matrix_a, vector_b)

        if ans == 2:
            print('running batch mode Newton')
            newton.batchMode(batch_n, matrix_a, vector_b)
    else:
        if ans == 1:
            print('running based gradient')
            gradient.gradientBasedMethod(matrix_a, vector_b)

        if ans == 2:
            print('running based Newton')
            newton.newtonBasedMethod(matrix_a, vector_b)


    print('============================================================')
    ans = input('=   Would you like input new variables (y | n):')
    if ans in yes:
        tui()
    else:
        sys.exit()

def format_input(text, delimiter):
    text = text.replace(' ', '')
    text = text.split(delimiter)
    return text


def print_error(error):
    print('=\n=   ' + error)
    ans = input('=   Would you like input new variables (y | n):')
    if ans in yes:
        tui()
    else:
        sys.exit()


def print_variables(matrix, vector, scalar):
    print('=')
    print('=   Defined variables:')
    print('=   Matrix:\n')
    print(matrix)
    print('\n=   Vector:\n')
    print(vector)
    print('\n=   Scalar: ' + str(scalar))


if __name__ == "__main__":
    tui()
