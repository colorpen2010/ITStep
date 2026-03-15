num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
action = input('Enter operation(+, -, *, /): ')

match action:
    case '+': print(f'{num1} + {num2} = {num1 + num2}')
    case '-': print(f'{num1} - {num2} = {num1 - num2}')
    case '*': print(f'{num1} * {num2} = {num1 * num2}')
    case '/': print(f'{num1} / {num2} = {num1 / num2}')

try:
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    action = input('Enter operation(+, -, *, /): ')

    match action:
        case '+': print(f'{num1} + {num2} = {num1 + num2}')
        case '-': print(f'{num1} - {num2} = {num1 - num2}')
        case '*': print(f'{num1} * {num2} = {num1 * num2}')
        case '/': print(f'{num1} / {num2} = {num1 / num2}')
except:
    print('Incorrect number!')

try:
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    action = input('Enter operation(+, -, *, /): ')

    match action:
        case '+': print(f'{num1} + {num2} = {num1 + num2}')
        case '-': print(f'{num1} - {num2} = {num1 - num2}')
        case '*': print(f'{num1} * {num2} = {num1 * num2}')
        case '/': print(f'{num1} / {num2} = {num1 / num2}')
except ValueError:
    print('Incorrect number!')
except ZeroDivisionError:
    print("Can't divide by zero!")

while True:
    try:
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        action = input('Enter operation(+, -, *, /): ')

        match action:
            case '+': print(f'{num1} + {num2} = {num1 + num2}')
            case '-': print(f'{num1} - {num2} = {num1 - num2}')
            case '*': print(f'{num1} * {num2} = {num1 * num2}')
            case '/': print(f'{num1} / {num2} = {num1 / num2}')
    except ValueError:
        print('Incorrect number!')
    except ZeroDivisionError:
        print("Can't divide by zero!")
    finally:
        reapeat = input('Do you want to repeat? Y/N ')
        if reapeat.lower() == 'n':
            break