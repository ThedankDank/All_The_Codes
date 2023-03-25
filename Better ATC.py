print('Welcome!')
print('1. Simple Calculator\n'
      '2. Profit & Loss\n'
      '3. Password Checker\n'
      '4. Decision Calculator\n'
      '5. Bigger or Smaller?\n'
      '6. Case Study #1\n'
      '7. Grading System\n'
      '8. Bikes & Road Tax\n'
      '9. Leap Year? Or Not?\n'
      '10. Days of the Week\n'
      '11. Equilateral, Iscosceles and Scalene Triangles')
cod = int(input('Please choose a code: '))

while cod > 11 or cod < 0:
    cod = int(input('Please choose a code from 1-11: '))

if cod == 1:
    print('Please choose an operator.')
    print('1. Addition\n'
        '2. Subtraction\n'
        '3. Division\n'
        '4. Multiplication\n'
        '5. Modulus')
    ope = int(input('Operator: '))
    while ope > 5 or ope < 0:
        ope = int(input('Please enter an operator from 1-5: '))

    if ope == 1:
        x = float(input('Please enter a value: '))
        y = float(input('Please enter another value: '))
        print(f'The sum of {x} and {y} is {x + y}.')
    elif ope == 2:
        x = float(input('Please enter a value (larger): '))
        y = float(input('Please enter another value (smaller): '))
        print(f'The difference of {x} and {y} is {x - y}.')
    elif ope == 3:
        x = float(input('Please enter a value for the dividend: '))
        y = float(input('Please enter another value for the divisor: '))
        print(f'The quotient of {x} and {y} is {x / y}.')
    elif ope == 4:
        x = float(input('Please enter a value for the multiplicand: '))
        y = float(input('Please enter another value for the multiplier: '))
        print(f'The product of {x} and {y} is {x * y}.')
    else:
        x = float(input('Please enter a value for the dividend: '))
        y = float(input('Please enter another value for the divisor: '))
        print(f'The remainder of {x} and {y} is {x % y}.')

elif cod == 2:
    print('Choose an option:')
    print('1. Profit\n'
        '2. Loss\n'
        '3. Auto Decision')
    opt = int(input('Choose option: '))
    while opt > 3 or opt < 0:
        opt = int(input('Please choose an option between 1-3: '))

    if opt == 1:
        x = float(input('Please enter the selling price: '))
        y = float(input('Please enter the cost price: '))
        while x - y < 0:
            print('Error: The selling price must be higher than the cost price for there to be a positive output for the profit.')
            x = float(input('Please enter the selling price: '))
            y = float(input('Please enter the cost price: '))
            print(f'The profit gained is {x - y}.')
    elif opt == 2:
        x = float(input('Please enter the selling price: '))
        y = float(input('Please enter the cost price: '))
        while y - x < 0:
            print('Error: The cost price must be higher than the selling price for there to be a positive output for the loss.')
            x = float(input('Please enter the selling price: '))
            y = float(input('Please enter the cost price: '))
            print(f'The money lost is {y - x}.')
    else:
        x = float(input('Please enter the selling price: '))
        y = float(input('Please enter the cost price: '))
        if x - y < 0:
            print(f'The money lost is {y - x}.')
        else:
            print(f'The profit gained is {x - y}.')

elif cod == 3:
    pas = input('Enter your password: ')
    while pas.isdigit() or len(pas) < 7 or pas.isspace() or pas.isdecimal():
        pas = input('Enter your password: ')

    repas = input('Please re-enter you password: ')
    while repas != pas:
        print('Error: Your password does not match.')
        repas = input('Please re-enter you password: ')

    pin = input('Enter your PIN number: ')
    while pin.isalpha() or len(pin) < 7:
        print('Error: Your PIN number must comprise of digits and must be a length of 7 digits or above.')
        pin = input('Enter your PIN number: ')

    print('Your PIN number has been recorded.')

elif cod == 4:
    print('Please choose an option.')
    print('1. Even or Odd?\n'
          '2. Prime Numbers\n'
          '3. Square roots\n'
          '4. Whole Number or Decimal?')
    dec = int(input('Choose an option: '))
    while dec > 4 or dec < 0:
        dec = int(input('Please choose an option between 1-4: '))

    if dec == 1:
        x = int(input('Please enter a whole number: '))
        if x % 2 == 0:
            print(f'{x} is an even number.')
        else:
            print(f'{x} is an odd number.')
    elif dec == 2:
        x = int(input('Please enter a number: '))
        y = 0
        if x > 1:
            for i in range(1, x + 1):
                if x % i == 0:
                    y = y + 1
            if y == 2:
                print(f'{x} is a prime number.')
            else:
                print(f'{x} is a composite number.')
        else:
            print(f'{x} is either a unit number or a negative number.')
    elif dec == 3:
        x = int(input('Please enter a whole number: '))
        print(f'The square root of {x} is {x ** 2}')
    else:
        x = input('Please enter a number: ')
        if x.isdecimal():
            print(f'{x} is a decimal number.')
        else:
            print(f'{x} is a whole number.')

elif cod == 5:
    x = float(input('Please enter a number: '))
    y = float(input('Please enter a number: '))
    z = float(input('Please enter a number: '))
    while x == y or x == z or y == z:
        print('Error: All numbers must not be equal.')
        x = float(input('Please enter a number: '))
        y = float(input('Please enter a number: '))
        z = float(input('Please enter a number: '))

    S = min(x, y, z)
    L = max(x, y, z)
    print(f'The highest number between {x}, {y} and {z} is {L}.')
    print(f'The lowest number between {x}, {y} and {z} is {S}.')

elif cod == 6:
    x = float(input('Please enter a number: '))
    y = float(input('Please enter a number: '))
    z = float(input('Please enter a number: '))
    while x == y or x == z or y == z:
        print('Error: All numbers must not be equal.')
        x = float(input('Please enter a number: '))
        y = float(input('Please enter a number: '))
        z = float(input('Please enter a number: '))

    S = min(x, y, z)
    print(f'The product of the two largest numbers is {(x * y * z) / S}')

elif cod == 7:
    G = float(input('Please enter your marks: '))
    while G > 100 or G < 0:
        print('Error: Your marks cannot be lesser than 0 or greater than 100.')
        G = float(input('Please enter your marks: '))

    if G in range(80, 101):
        print('You got an A!')
    elif G in range(70, 80):
        print('You got a B!')
    elif G in range(60, 70):
        print('You got a C.')
    elif G in range(50, 60):
        print('You got a D.')
    else:
        print('You got an E.')

elif cod == 8:
    tax = float(input('Please enter the cost of your bike: '))
    while tax < 0:
        print('Error: The value given must be positive!')
        tax = float(input('Please enter the cost of your bike: '))

    if tax > 100000:
        print(f'The total amount to be paid for your bike (including taxes) is {(tax * 0.15) + tax}.')
    elif tax in range(50000, 100001):
        print(f'The total amount to be paid for your bike (including taxes) is {(tax * 0.1) + tax}.')
    else:
        print(f'The total amount to be paid for your bike (including taxes) is {(tax * 0.05) + tax}.')

elif cod == 9:
    yer = int(input('Please enter a year: '))
    while yer < 0:
        print('Error: The year cannot be in negative digits.')
        yer = int(input('Please enter a year: '))

    if yer % 4 == 0:
        print(f'Year {yer} is a leap year.')
    else:
        print(f'Year {yer} is not a leap year.')

elif cod == 10:
    day = int(input('Please enter a number from 1-7: '))
    while day > 7 or day < 0:
        print('Error: The number must be between 1-7.')
        day = int(input('Please enter a number from 1-7: '))

    if day == 1:
        print('It is Sunday.')
    elif day == 2:
        print('It is Monday.')
    elif day == 3:
        print('It is Tuesday.')
    elif day == 4:
        print('It is Wednesday.')
    elif day == 5:
        print('It is Thursday.')
    elif day == 6:
        print('It is Friday.')
    else:
        print('It is Saturday.')

else:
    x = float(input('Please enter a length for side 1: '))
    y = float(input('Please enter a length for side 2: '))
    z = float(input('Please enter a length for side 3: '))
    if x == y == z:
        print('It is an equilateral triangle.')
    elif x == y or x == z or y == z:
        print('It is an iscosceles triangle.')
    else:
        print('It is a scalene triangle.')
