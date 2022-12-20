from sympy import symbols, diff

def derivative(equation):
    # Define the variable and the order of the derivative
    x = symbols('x')
    order = 1

    # Compute the derivative using the diff function
    derivative = diff(equation, x, order)

    return derivative


print(derivative('x/(3^x+10^x)'))



































