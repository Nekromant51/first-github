def def1(number):
    summ = 0
    while number != 0:
        summ = summ + number % 10
        number = number // 10
    print("Сумма цифр числа равна: ", summ)

def def2(number):
    count = 0
    while(number > 0):
        count = count + 1
        number = number // 10
    print("Количество цифр в числе:", count)

def def3(number):
    count = 0
    if number == 0:
        print("Количество цифр: 1")
    else:
        while number != 0:
            count += 1
            number //= 10
    print("Количество цифр: ", count)


number = int(input('Введите число: '))
def1(number)
def2(number)
def3(number)
