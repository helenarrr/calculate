import methods as m
import input_chars as ic
import log as l

def button_click():
    print('Введите 0, чтобы продолжить работу')
    print('Введите 1, чтобы закончить работу')
    flag = int(input())
    while flag == 0:
        primer = m.parse()
        result = m.calculate(primer)
        ic.view_data(result)
        l.logger(primer, result)
        print('Введите 0, чтобы продолжить работу: ')
        print('Введите 1, чтобы закончить работу: ')
        flag = int(input())
    print('Программа завершилась')

