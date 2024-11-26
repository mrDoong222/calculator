def int_check(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input) 
        else:
            return 'use a number. try again'
def calc():
    a = int_check('enter number: ')
    o = input('enter operator (+, -, /, x): ')
    b = int_check('enter number: ')
    if o == '+':
        print(a+b)
    elif o == '-':
        print(a-b)
    elif o == '/':
        print(float(a/b))
    elif o == 'x':
        print(a*b)
    else: 
        print('invalid input used')
        calc()
    print('NEW EQUATION:')
    calc()
calc()
