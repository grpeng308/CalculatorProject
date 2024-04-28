from PyQt6.QtWidgets import *
from gui import *
import math

WIDTH_MODE = 450
WIDTH_NO_MODE = 255
HEIGHT = 300


def is_float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedWidth(WIDTH_NO_MODE)
        self.preview.setText("")
        self.main_text.setText("0")
        self.var1 = 1
        self.__negative = False
        self.label1.hide()
        self.label2.hide()
        self.lineEdit1.hide()
        self.lineEdit2.hide()
        self.submit.hide()

        self.circle.setGeometry(260, 20, 100, 20)
        self.square.setGeometry(360, 20, 100, 20)
        self.rectangle.setGeometry(260, 50, 100, 20)
        self.triangle.setGeometry(360, 50, 100, 20)

        self.label1.setGeometry(260, 90, 30, 20)
        self.lineEdit1.setGeometry(260, 115, 168, 22)
        self.label2.setGeometry(260, 145, 51, 20)
        self.lineEdit2.setGeometry(260, 170, 168, 22)

        self.submit.setGeometry(367, 205, 61, 30)

        self.preview.setGeometry(126, 15, 111, 20)
        self.main_text.setGeometry(20, 50, 218, 31)

        self.__mode = False
        self.mode.clicked.connect(lambda: self.mode_status())

        self.clear.clicked.connect(lambda: self.clear_button())
        self.delete_2.clicked.connect(lambda: self.delete_button())
        self.negative.clicked.connect(lambda: self.negative_button())

        self.divide.clicked.connect(lambda: self.function_button('/'))
        self.multiply.clicked.connect(lambda: self.function_button('*'))
        self.subtract.clicked.connect(lambda: self.function_button('-'))
        self.add.clicked.connect(lambda: self.function_button('+'))

        self.equal.clicked.connect(lambda: self.equal_button())

        self.zero.clicked.connect(lambda: self.click_button('0'))
        self.one.clicked.connect(lambda: self.click_button('1'))
        self.two.clicked.connect(lambda: self.click_button('2'))
        self.three.clicked.connect(lambda: self.click_button('3'))
        self.four.clicked.connect(lambda: self.click_button('4'))
        self.five.clicked.connect(lambda: self.click_button('5'))
        self.six.clicked.connect(lambda: self.click_button('6'))
        self.seven.clicked.connect(lambda: self.click_button('7'))
        self.eight.clicked.connect(lambda: self.click_button('8'))
        self.nine.clicked.connect(lambda: self.click_button('9'))

        self.decimal.clicked.connect(lambda: self.decimal_button())

        self.circle.clicked.connect(lambda: self.circle_clicked())
        self.rectangle.clicked.connect(lambda: self.rectangle_clicked())
        self.square.clicked.connect(lambda: self.square_clicked())
        self.triangle.clicked.connect(lambda: self.triangle_clicked())

        self.submit.clicked.connect(lambda: self.submit_clicked())

    def submit_clicked(self):
        if self.circle.isChecked():
            print("True")
            radius = self.lineEdit1.text()
            if is_float(radius):
                if float(radius) > 999 or float(radius) < 0:
                    self.lineEdit1.setText(f"")
                    self.main_text.setText("Error")
                else:
                    area = math.pi * float(radius) ** 2
                    self.main_text.setText(f"Area = {area:.5f}")
            else:
                self.lineEdit1.setText(f"")
                self.main_text.setText("Error")

        elif self.square.isChecked():
            side = self.lineEdit1.text()
            if is_float(side):
                if float(side) > 999 or float(side) < 0:
                    self.lineEdit1.setText(f"")
                    self.main_text.setText("Error")
                else:
                    if is_int(side):
                        area = int(side) ** 2
                        self.main_text.setText(f"Area = {area}")
                    else:
                        area = float(side) ** 2
                        self.main_text.setText(f"Area = {area:.5f}")

            else:
                self.lineEdit1.setText(f"")
                self.main_text.setText("Error")

        elif self.rectangle.isChecked():
            length = self.lineEdit1.text()
            width = self.lineEdit2.text()
            if is_float(length) and is_float(width):
                if float(length) > 999 or float(width) > 999 or float(length) < 0 or float(width) < 0:
                    self.lineEdit1.setText(f"")
                    self.lineEdit2.setText(f"")
                    self.main_text.setText("Error")
                else:
                    if is_int(length) and is_int(width):
                        area = int(length) * int(width)
                        self.main_text.setText(f"Area = {area}")
                    else:
                        area = float(length) * float(width)
                        self.main_text.setText(f"Area = {area:.5f}")

            else:
                self.lineEdit1.setText(f"")
                self.lineEdit2.setText(f"")
                self.main_text.setText("Error")

        elif self.triangle.isChecked():
            base = self.lineEdit1.text()
            height = self.lineEdit2.text()
            if is_float(base) and is_float(height):
                if float(base) > 999 or float(height) > 999 or float(base) < 0 or float(height) < 0:
                    self.lineEdit1.setText(f"")
                    self.lineEdit2.setText(f"")
                    self.main_text.setText("Error")
                else:
                    if is_int(base) and is_int(height):
                        area = 0.5 * int(base) * int(height)
                        self.main_text.setText(f"Area = {area}")
                    else:
                        area = 0.5 * float(base) * float(height)
                        self.main_text.setText(f"Area = {area:.5f}")

            else:
                self.lineEdit1.setText(f"")
                self.lineEdit2.setText(f"")
                self.main_text.setText("Error")

    def circle_clicked(self):
        self.label1.show()
        self.lineEdit1.show()
        self.submit.show()
        self.label2.hide()
        self.lineEdit2.hide()

        self.submit.setGeometry(370, 145, 61, 20)
        self.label1.setGeometry(260, 90, 100, 26)
        self.label1.setText("Radius")
        self.lineEdit1.setPlaceholderText("Enter radius value here")

    def square_clicked(self):
        self.label1.show()
        self.lineEdit1.show()
        self.submit.show()
        self.label2.hide()
        self.lineEdit2.hide()

        self.submit.setGeometry(370, 145, 61, 20)
        self.label1.setGeometry(260, 90, 100, 26)
        self.label1.setText("Side")
        self.lineEdit1.setPlaceholderText("Enter side value here")

    def rectangle_clicked(self):
        self.label1.show()
        self.lineEdit1.show()
        self.label2.show()
        self.lineEdit2.show()
        self.submit.show()
        self.label1.setGeometry(260, 90, 100, 26)

        self.label1.setText("Length")
        self.label2.setText("Width")
        self.lineEdit1.setPlaceholderText("Enter length value here")
        self.lineEdit2.setPlaceholderText("Enter width value here")

    def triangle_clicked(self):
        self.label1.show()
        self.lineEdit1.show()
        self.label2.show()
        self.lineEdit2.show()
        self.submit.show()
        self.label1.setGeometry(260, 90, 100, 26)

        self.label1.setText("Base")
        self.label2.setText("Height")
        self.lineEdit1.setPlaceholderText("Enter base value here")
        self.lineEdit2.setPlaceholderText("Enter height value here")

    def click_button(self, num):
        self.delete_2.setEnabled(True)
        self.var1 = 1
        text = self.main_text.text()
        if text == "0" or text == "Error":
            text = ""
        elif "Ans" in text or text == "Error":
            text = ""
            self.preview.setText("")
        self.main_text.setText(text + num)

    def decimal_button(self):
        text = self.main_text.text()
        text_list = list(text)
        if text_list[-1] == ".":
            self.main_text.setText(text)
        else:
            self.main_text.setText(text + ".")

    def function_button(self, function):
        self.delete_2.setEnabled(True)
        preview = self.preview.text()
        text = self.main_text.text()
        # self.enable_num()
        if "Ans" in text or text == "Error":
            self.preview.setText("")
        if preview == "" or self.var1 == 2:
            if "Ans" in text:
                text = text.replace("Ans = ", "")
                self.preview.setText(text + function)
            elif "Error" in text:
                number_original = preview.replace("/0", "")
                self.preview.setText(number_original + function)
            else:
                self.preview.setText(text + function)
        else:
            self.preview.setText(preview + text + function)
        self.main_text.setText("0")

    def equal_button(self):

        self.delete_2.setEnabled(False)
        # self.disable_num()

        text = self.main_text.text()
        preview = self.preview.text()

        try:
            if preview == "":
                solution = text
            else:
                self.preview.setText(preview + text)
                equation = self.preview.text()
                solution = eval(equation)

            self.main_text.setText(f"Ans = {solution}")
        except ZeroDivisionError:
            self.main_text.setText(f"Error")
        self.var1 = 2

    def clear_button(self):
        self.delete_2.setEnabled(True)
        self.enable_num()
        self.main_text.setText("0")
        self.preview.setText("")

    def delete_button(self):
        text = self.main_text.text()
        text1 = text[:-1]
        self.main_text.setText(text1)

    def negative_button(self):
        text = self.main_text.text()
        text1 = list(text)
        if not self.__negative:
            self.main_text.setText(f"-{text}")
            self.__negative = True
        else:
            if text1[0] == "-":
                self.main_text.setText(f"{text[1:]}")
            self.__negative = False

    def hide_radio(self):
        self.circle.hide()
        self.square.hide()
        self.rectangle.hide()
        self.triangle.hide()

    def show_radio(self):
        self.circle.show()
        self.square.show()
        self.rectangle.show()
        self.triangle.show()

    def mode_status(self):

        if not self.__mode:
            self.setFixedWidth(WIDTH_MODE)
            self.__mode = True
            # self.show_radio()
        else:
            self.setFixedWidth(WIDTH_NO_MODE)
            self.__mode = False
            # self.hide_radio()

    def disable_num(self):
        self.zero.setEnabled(False)
        self.one.setEnabled(False)
        self.two.setEnabled(False)
        self.three.setEnabled(False)
        self.four.setEnabled(False)
        self.five.setEnabled(False)
        self.six.setEnabled(False)
        self.seven.setEnabled(False)
        self.eight.setEnabled(False)
        self.nine.setEnabled(False)
        self.negative.setEnable(False)
        self.decimal.setEnable(False)

    def enable_num(self):
        self.zero.setEnabled(True)
        self.one.setEnabled(True)
        self.two.setEnabled(True)
        self.three.setEnabled(True)
        self.four.setEnabled(True)
        self.five.setEnabled(True)
        self.six.setEnabled(True)
        self.seven.setEnabled(True)
        self.eight.setEnabled(True)
        self.nine.setEnabled(True)
        self.negative.setEnabled(True)
        self.decimal.setEnabled(True)

    '''
    def set_width(self, width):
        if self.__mode:
            self.setFixedWidth(300)
            self.__mode = False
        else:
            self.setFixedWidth(400)
            self.__mode = True
            '''

