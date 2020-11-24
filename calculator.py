#python

print("\033[1;32;40m CALCULATOR PROGRAM MADE BY ANONYMINHACK5 \n")
print("\033[1;33;40m THIS TOOL WILL HELP IN SOLVING BASIC MATHEMATICAL OPERATIONS FOR EDUCATIONAL PURPOSES\n")

print("\033[1;36;40m :::::::::::::: CALCULATOR IS NOW WORKING.:::::::::::::\n")
color = ['Follow me on github: https://github.com/TermuxHackz', 'Follow me on facebook: https://facebook.com/anonyminhack5', 'Follow me on twitter: https://twitter.com/anonyminHack5', 'Name: AnonyminHack5', 'Position: Admin of Termux Android Hackers', 'WELCOME']
with open('abc.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('abc.txt')
print(content.read())

def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print("\033[1;31;40m You have not typed a valid operator, please run the program again\n.")

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
      print("\033[2;37;40m THANKS FOR USING THIS CALCULATOR SEE YOU LATER, FOLLOW ME ON TWITTER: @AnonyminHack5\n")
    else:
        again()

calculate()
