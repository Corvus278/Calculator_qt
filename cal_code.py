import cal_des2

import sys
from PyQt5 import QtWidgets
import math


class Calculator(QtWidgets.QMainWindow, cal_des2.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Button_1.clicked.connect(self.b1)
        self.Button_2.clicked.connect(self.b2)
        self.Button_3.clicked.connect(self.b3)
        self.Button_4.clicked.connect(self.b4)
        self.Button_5.clicked.connect(self.b5)
        self.Button_6.clicked.connect(self.b6)
        self.Button_7.clicked.connect(self.b7)
        self.Button_8.clicked.connect(self.b8)
        self.Button_9.clicked.connect(self.b9)
        self.Button_0.clicked.connect(self.b0)
        self.Button_C.clicked.connect(self.bC)

        self.Button_sum.clicked.connect(self.bsum)
        self.Button_sub.clicked.connect(self.bsub)
        self.Button_div.clicked.connect(self.bdiv)
        self.Button_mul.clicked.connect(self.bmul)
        self.Button_eq.clicked.connect(self.beq)
        self.Button_sqrt.clicked.connect(self.bsqrt)
        self.Button_qrt.clicked.connect(self.bqrt)
        self.Button_del.clicked.connect(self.bdel)
        self.Button_pm.clicked.connect(self.bpm)
        self.Button_row.clicked.connect(self.brow)
        self.Button_parenthesisLeft.clicked.connect(self.bparenthesisLeft)
        self.Button_parenthesisRight.clicked.connect(self.bparenthesisRight)

        self.flag = False  # Нужно ли очищать поле перед вводом, или нет
        self.sqrt_flag = False
        self.sqrt_value = ''

    def b1(self):
        return self.number('1')

    def b2(self):
        return self.number('2')

    def b3(self):
        return self.number('3')

    def b4(self):
        return self.number('4')

    def b5(self):
        return self.number('5')

    def b6(self):
        return self.number('6')

    def b7(self):
        return self.number('7')

    def b8(self):
        return self.number('8')

    def b9(self):
        return self.number('9')

    def b0(self):
        return self.number('0')

    def bC(self):
        self.label.setText('0')
        if len(self.sqrt_value) > 0:
            self.sqrt_value = ''

    def bsum(self):
        return self.chars('+')

    def bsub(self):
        return self.chars('-')

    def bdiv(self):
        return self.chars('/')

    def bmul(self):
        return self.chars('*')

    def bsqrt(self):
        self.sqrt_flag = True
        return self.chars('_/')

    def bqrt(self):
        return self.chars('^')

    def bdel(self):
        value = self.label.text()
        if self.flag:
            self.label.setText('0')
        else:
            if value[-1] == ' ':
                self.label.setText(value[:-3])
            else:
                self.label.setText(value[:-1])
        # Также нужно стирать значение из корня, если оно в данное время записывается
        if self.sqrt_flag:
            if len(self.sqrt_value) > 0:
                self.sqrt_value = self.sqrt_value[:-1]

    def bpm(self):
        return self.chars('+/-')

    def brow(self):
        return self.chars('.')

    def bparenthesisLeft(self):
        return self.number('(')

    def bparenthesisRight(self):
        return self.number(')')

    def beq(self):
        try:
            self.sqrt_flag = False  # На случай, если извлечение корня будет последним действием
            value_label = self.label.text()
            if value_label.find('_') != -1:
                if value_label[2:].find(' ') == -1:
                    value_label = str(math.sqrt(int(value_label[2:])))
                else:
                    sqrt_value_len = len(self.sqrt_value)
                    self.sqrt_value = str(math.sqrt(int(self.sqrt_value)))
                    border_l = value_label.find('_')+1
                    border_r = border_l + sqrt_value_len + 1
                    if value_label.find(' ', border_r) == -1:
                        value_label = value_label[:border_l-1] + self.sqrt_value
                    else:
                        value_label = value_label[:border_l-1] + self.sqrt_value + value_label[border_r:]

            if value_label.find('^') != -1:  # Возведение в степень
                value_label = value_label[:value_label.find('^')] + '**' + value_label[value_label.find('^')+1:]
            try:
                self.label.setText(str(eval(value_label)))
            except SyntaxError:
                self.flag = False   # Флаг опять опускается, т.к. число до конца не введено
                pass
            except ZeroDivisionError:
                self.label.setText('Деление на ноль невозможно!')
            self.flag = True  # При нажатии "равно" флаг поднимается, и перед вводом нового числа поле очищается
            self.sqrt_value = ''
        except:
            self.label.setText('Неверный ввод')
            self.flag = True

    def number(self, number):
        if self.flag:
            self.label.setText('')
            self.flag = False   # Флаг опускается обратно
        value_b = self.label.text()
        if number == '(':
            if value_b.rfind(' ') == -1:
                value_b = ''
                number = '('
            else:
                value_b = value_b[:value_b.rfind(' ')+1]
        if value_b == '0':
            self.label.setText(number)
        else:
            if self.sqrt_flag:
                self.sqrt_value += number
            self.label.setText(value_b + number)

    def chars(self, char):
        try:
            self.flag = False   # Опять опускаем флаг, что бы была возможность производить вычесления над результатом
            if char != '_/':
                self.sqrt_flag = False
            value_b = self.label.text()
            if char == '+/-':
                # Сперва находится последняя цифра, записывается в переменную (задом наперёд),
                # далее цифра переворачивается и меняет свой знак
                number = ''
                i = len(value_b)-1
                while i != -1 and 47 < ord(value_b[i]) < 58 or value_b[i] == '-' or value_b[i] == '+':
                    number += value_b[i]
                    i -= 1
                number = number[::-1]
                number = str(int(number) * (-1))
                # if int(number) < 0
                l = len(number)
                self.label.setText(value_b[:-l] + ' ' + number)
                if int(number) > 0:
                    value = self.label.text()
                    self.label.setText(value[:int(len(value))-(l+2)] + number)
            else:
                if char == '_/':   # У квадратного корня особое поведение
                    self.sqrt_flag = True
                    if value_b == '0':
                        self.label.setText(char)
                    elif 47 < ord(value_b[-1]) < 58:    # Ставим корень перед уже написаным числом
                        if value_b.rfind(' ') == -1:
                           self.label.setText(char + value_b)
                           # При извлечении берётся последний символ
                        else:
                            self.label.setText(value_b[:value_b.rfind(' ')+1] + char + value_b[value_b.rfind(' ')+1:])
                            self.sqrt_value = value_b[value_b.rfind(' ')+1:]
                    elif value_b[-2] in ['+', '-', '*', '/', '^']:
                        self.label.setText(value_b + f'{char}')
                elif 47 < ord(value_b[-1]) < 58 or value_b[-1] == '(' or value_b[-1] == ')':
                    if char == '.':    # Если будет введена точка, то пробел между ней и числом ставить не нужно
                        self.label.setText(value_b + f'{char}')
                    else:
                        self.label.setText(value_b + f' {char} ')
                else:
                    print(3)
                    self.label.setText(value_b[:-2] + f'{char} ')
        except:
            self.label.setText('0')


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Calculator()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
