import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit

class SimpleCalculator(QWidget):
    def __init__(self):
        super().__init__()

        
        self.setWindowTitle("Santosh Calculator")
        self.setGeometry(100, 100, 250, 300)

        self.display = QLineEdit(self)
        self.display.setReadOnly(True)

        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.display)

        self.grid = QGridLayout()
        self.layout.addLayout(self.grid)

        
        self.create_buttons()

        
        self.setLayout(self.layout)

        
        self.first_operand = None
        self.operator = None
        self.current_input = ""

    def create_buttons(self):
        """ Create and arrange buttons on the calculator grid """
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('+', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('-', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('*', 2, 3),
            ('C', 3, 1), ('0', 3, 1), ('=', 3, 2), ('/', 3, 3)
        ]
        
        for text, row, col in buttons:
            button = QPushButton(text)
            button.clicked.connect(self.on_button_click)
            self.grid.addWidget(button, row, col)

    def on_button_click(self):
        """ Handle button click events """
        sender = self.sender()
        text = sender.text()

        if text == 'C':
            self.clear()
        elif text == '=':
            self.calculate()
        else:
            self.handle_input(text)

    def clear(self):
        """ Clear the display and reset the calculator """
        self.display.clear()
        self.current_input = ""
        self.first_operand = None
        self.operator = None

    def handle_input(self, text):
        """ Handle numeric or operator button click """
        if text in '+-*/':
            self.set_operator(text)
        else:
            self.current_input += text
            self.display.setText(self.current_input)

    def set_operator(self, operator):
        """ Set the operator and store the first operand """
        if self.first_operand is None:
            self.first_operand = float(self.current_input)
            self.operator = operator
            self.current_input = ""
        else:
            self.display.setText("Error")

    def calculate(self):
        """ Perform the calculation based on the stored operands and operator """
        if self.first_operand is not None and self.operator is not None:
            try:
                second_operand = float(self.current_input)
                result = self.compute_result(self.first_operand, second_operand, self.operator)
                self.display.setText(str(result))
                self.first_operand = None  # Reset operand after calculation
                self.operator = None  # Reset operator
                self.current_input = str(result)  # Store the result
            except ZeroDivisionError:
                self.display.setText("Error")
        else:
            self.display.setText("Error")

    def compute_result(self, first_operand, second_operand, operator):
        """ Perform the specified arithmetic operation """
        if operator == '+':
            return first_operand + second_operand
        elif operator == '-':
            return first_operand - second_operand
        elif operator == '*':
            return first_operand * second_operand
        elif operator == '/':
            if second_operand == 0:
                raise ZeroDivisionError
            return first_operand / second_operand



app = QApplication(sys.argv)
window = SimpleCalculator()
window.show()
sys.exit(app.exec_())
