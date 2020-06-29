from collections import deque


def result(cc):
    #print(cc)
    res = deque()
    for i in cc:
        if i.isdigit():
            res.append(int(i))
        else:
            if i == "+":
                a = res.pop()
                b = res.pop()
                c = a + b
                res.append(c)
            elif i == "-":
                b = res.pop()
                a = res.pop()
                c = a - b
                res.append(c)
            elif i == "*":
                a = res.pop()
                b = res.pop()
                c = a * b
                res.append(c)
            elif i == "/":
                b = res.pop()
                a = res.pop()
                #print(b, a)
                c = a / b
                res.append(c)
            #print(res)
    return int(res[0])


def plus_minus(num):
    if '*' not in num[0] and '+' not in num[0] \
            and '-' not in num[0] and '/' not in num[0]:
        count = deque()
        opr = deque()
        try_err = 0
        for i in num:
            if '(' in i:
                try_err = 1
            elif ')' in i:
                try_err -= 1
        if try_err == 0:
            for i in range(len(num)):
                if len(num[i]) > 1 and num[i].startswith('-') and num[i][-1].isdigit():
                    count.append('-' + num[i][1:])
                    # print(count)
                elif len(num[i]) > 1 and num[i].startswith('+') and num[i][-1].isdigit():
                    count.append(num[i][1:])
                    # print(count)
                elif num[i].isdigit() and i == 0:
                    count.append(num[0])
                elif num[i].isdigit():
                    count.append(num[i])
                    # print(num[i])
                elif num[i].isalpha():
                    try:
                        nn = str(dct_var[num[i]])
                        count.append(nn)
                    except ValueError:
                        print('Invalid assignment')
                    except KeyError:
                        print(f'Unknown variable {num[i]} 66')
                elif not num[i].isdigit():
                    operand = num[i]
                    #print(operand)
                    if operand.startswith('+') or operand.startswith('-') \
                            or operand.startswith('*') or operand.startswith('/') :
                        if operand.startswith('+'):
                            operand = '+'
                        elif operand.startswith('-'):
                            operand = minus_or_plus(operand)
                        elif operand.startswith('*'):
                            if len(operand) == 1:
                                operand = '*'
                            else:
                                err = 'Invalid expression'
                                return err
                        elif operand.startswith('/'):
                            if len(operand) == 1:
                                operand = '/'
                            else:
                                err = 'Invalid expression'
                                return err
                    if len(opr) == 0:
                        opr.append(operand)
                    elif operand.startswith('(') or operand.endswith(')'):
                        if operand.startswith('('):
                            for yy in operand:
                                #print(yy)
                                if yy == '(':
                                    opr.append(yy)
                                else:
                                    count.append(yy)
                                #print(opr, 444)
                        elif operand.endswith(')'):
                            #print(')00')
                            count.append(operand[:-1])
                            lf = len(opr)
                            while lf != 0:
                                if opr[-1] == '(':
                                    opr.pop()
                                    break
                                else:
                                    #print(opr, 11)
                                    op = opr.pop()
                                    count.append(op)
                                    #print(opr)
                                lf -= 1
                    elif dct_opr[operand] > dct_opr[opr[-1]]:
                        opr.append(operand)
                    elif dct_opr[operand] <= dct_opr[opr[-1]]:
                        op = opr[-1]
                        if op == '(':
                            opr.append(operand)
                            #print(op)
                            #print('add4')
                        else:
                            op = opr.pop()
                            #print(op)
                            count.append(op)
                            opr.append(operand)
            if len(opr) >= 1:
                #print(opr)
                while len(opr) != 0:
                    d = opr.pop()
                    count.append(d)
                #print('last')
            #print(count)
            #print(opr)
            return result(count)
        else:
            err = 'Invalid expression'
            return err
    else:
        if num[0].startswith('-'):
            lst = []
            for i in num[0]:
                lst.append(i.isdigit())
            if all(lst[1:]):
                return num[0]
        else:
            num = list(num[0])
            try_err = 0
            for i in num:
                if '(' in i:
                    try_err = 1
                elif ')' in i:
                    try_err -= 1
            if try_err == 0:
                count = deque()
                opr = deque()
                for i in range(len(num)):
                    if len(num[i]) > 1 and num[i].startswith('-') and num[i][-1].isdigit():
                        count.append('-' + num[i][1:])
                        #print(count)
                        # print(count)
                    elif len(num[i]) > 1 and num[i].startswith('+') and num[i][-1].isdigit():
                        count.append(num[i][1:])
                        # print(count)
                    elif num[i].isdigit() and i == 0:
                        count.append(num[0])
                    elif num[i].isdigit():
                        count.append(num[i])
                        # print(num[i])
                    elif num[i].isalpha():
                        try:
                            nn = str(dct_var[num[i]])
                            count.append(nn)
                        except ValueError:
                            print('Invalid assignment')
                        except KeyError:
                            print(f'Unknown variable {num[i]}')
                    elif not num[i].isdigit():
                        operand = num[i]
                        # print(operand)
                        if len(operand) > 1 and operand.startswith('+') or operand.startswith('-'):
                            if operand.startswith('+'):
                                operand = '+'
                            else:
                                operand = minus_or_plus(operand)
                        if len(opr) == 0:
                            opr.append(operand)
                        elif operand.startswith('(') or operand.endswith(')'):
                            if operand.startswith('('):
                                opr.append(operand[0])
                                count.append(operand[1:])
                            elif operand.endswith(')'):
                                # print(')00')
                                count.append(operand[:-1])
                                lf = len(opr)
                                while lf != 0:
                                    if opr[-1] == '(':
                                        opr.pop()
                                    else:
                                        op = opr.pop()
                                        count.append(op)
                                    lf -= 1
                        elif dct_opr[operand] >= dct_opr[opr[-1]]:
                            opr.append(operand)
                        elif dct_opr[operand] < dct_opr[opr[-1]]:
                            op = opr.pop()
                            if op == '(':
                                opr.append(operand)
                            # print(op)
                            # print('add4')
                            else:
                                count.append(op)
                                opr.append(operand)
                if len(opr) >= 1:
                    # print(opr)
                    while len(opr) != 0:
                        d = opr.pop()
                        count.append(d)
                    # print('last')
                # print(count)
                # print(opr)
                return result(count)
            else:
                err = 'Invalid expression'
                return err


def minus_or_plus(mop):
    l_mop = len(mop)
    if l_mop % 2 != 0:
        a = '-'
        return a
    return '+'


def define_var(str_var):
    global dct_var
    ind = str_var.find('=')
    key = str_var[:ind].strip()
    value = str_var[ind + 1:].strip()
    if key == '':
        print('Unknown variable')
    else:
        if key.isalpha():
            if value.isalpha():
                try:
                    dct_var[key] = dct_var[value]
                except KeyError:
                    print('Unknown variable')
            else:
                try:
                    dct_var[key] = int(value)
                except ValueError:
                    print('Invalid assignment')
        else:
            print('Invalid identifier')
    # print(dct_var)


def operation(opr):
    global stop
    if numbers == '/exit':
        print('Bye!')
        stop = False
    elif numbers == '/help':
        print('The program calculates the sum of numbers')
        print('The program calculates the sum or subtractions of numbers')
    else:
        print('Unknown command')


def print_or_operator(var):
    global dct_var
    ind = var.find('=')
    key = var[:ind].strip()
    value = var[ind + 1:].strip()
    # print(key)
    # print(value)
    if '+' in var or '-' in var:
        var = var.split(' ')
        for_opr = []
        # print(var)
        for item in var:
            if item.isalpha():
                if item in dct_var:
                    # print(item)
                    for_opr.append(item.replace(item, str(dct_var[item])))
                else:
                    print(f'Unknown variable {item}')
            else:
                for_opr.append(item)
        print(plus_minus(for_opr), sep='')
    else:
        if value in dct_var:
            print(dct_var[value])
        else:
            print('Unknown variable')


dct_opr = {'+': '1', '-': '1', '*': '2', '/': '2', '(': '60'}
dct_var = {}
stop = True
while stop:
    numbers = input()
    if numbers == '':
        pass
    elif numbers.startswith('/'):
        operation(numbers)
    elif numbers[0].isalpha() or numbers[1].isalpha() and numbers[0] == ' ':
        if "=" in numbers:
            define_var(numbers)
        elif len(numbers) >= 1:
            print_or_operator(numbers)
        else:
            print('Invalid identifier')
    elif numbers.startswith('+') or numbers.startswith('-') or not numbers.startswith('/'):
        try:
            numbers = numbers.split()
            print(plus_minus(numbers), sep='')
        except TypeError:
            print('Invalid expression')
    else:
        print('Invalid identifier')


'''        try:
            numbers = numbers.split()
            print(plus_minus(numbers))
        except TypeError:
            print('Invalid expression 3')'''
'''def plus_minus(num):
    # print(num)
    count = ''
    for i in range(len(num)):
        if len(num[i]) > 1 and num[i].startswith('-') and num[i][-1].isdigit():
            count = 0
            count -= int(num[i][1:])
            # print(count)
        elif len(num[i]) > 1 and num[i].startswith('+') and num[i][-1].isdigit():
            count = 0
            count += int(num[i][1:])
            # print(count)
        elif num[i].isdigit() and i == 0:
            count = 0
            count = int(num[0])
        elif num[i].isdigit():
            if num[i - 1].startswith('+'):
                count += int(num[i])
            if num[i - 1].startswith('-'):
                if minus_or_plus(num[i - 1]) == '-':
                    count -= int(num[i])
                    # print(num[i])
                    # print(1)
                else:
                    count += int(num[i])
    if count + 0 == count:
        return count
'''
