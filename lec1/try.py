def inputNumber(sen):
    try:
        print(sen)
        num = int(input())
    except:
        num = 0
    return num

#num1 = inputNumber('input number 1 : ')
#num2 = inputNumber('input number 2 : ')
#print('sum is ' + str(num1 + num2))

#try:
    print('div is :' + str(num1/num2))
#except:
    #print('num2 must not be zero!!')

try:
    n = int(input('input first num :    '))
    n2 = int(input('input sec num :     '))
    print(n/n2)
except ValueError:
    print('input int number !')
except ZeroDivisionError:
    print('set num2 of none zero value!!')
else:
    print('will be printed if we do not have any error ')
finally:
    print('will be printed any way')


