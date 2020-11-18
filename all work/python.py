#a+b
print(sum(map(int, input().split())))
############################################

перевод числа в другую систему счисления python
перевод числа в другую систему счисления python
перевод числа в другую систему счисления python



num = int(input())
base = int(input("Base (2-9): "))
if not(2 <= base <= 9):
    quit()

newNum = ''

while num > 0:
    newNum = str(num % base) + newNum
    num //= base

print(newNum)

C комментариями:

# Ввод числа и преобразование к целому
num = int(input())
# Ввод системы счисления
base = int(input("Base (2-9): "))

# Проверка корректности ввода системы счисления.
# Если основание не принадлежит указанному диапазону,
# то происходит выход из программы
if not(2 <= base <= 9):
    quit()

# Переменная для хранения строкового представления
# числа в заданной системе счисления
newNum = ''

# Пока исходное число больше 0,
while num > 0:
    # находится остаток от его деления на основание,
    # остаток преобразовывается к строковому типу и
    # добавляется в начало строкового представления нового числа
    newNum = str(num % base) + newNum
    # Само десятичное число делится нацело
    # на основание заданной системы счисления
    num //= base

# Вывод строкового представления числа
# в системе счисления с основанием base
print(newNum)

########################################
hepeBoD B tpouzhuyu cucTeMy

a, b = map(int, input().split())
def q(res):
    new = ''
    while res:
        new = str(res % 3) + new
        res //= 3
    return new
print(int(q(a)))
############################################
def convert_base(num, to_base=10, from_base=3):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]
    ##############################################
a = int(input())
print(bin(a))
