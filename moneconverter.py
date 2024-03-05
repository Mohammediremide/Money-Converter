import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import requests

class CurrencyConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Currency Converter')

        self.amount_label = QLabel('Amount:')
        self.amount_edit = QLineEdit()

        self.from_label = QLabel('From:')
        self.from_edit = QLineEdit()

        self.to_label = QLabel('To:')
        self.to_edit = QLineEdit()

        self.result_label = QLabel('Result:')
        self.result_display = QLabel()

        self.convert_button = QPushButton('Convert')
        self.convert_button.clicked.connect(self.convert)

        layout = QVBoxLayout()
        layout.addWidget(self.amount_label)
        layout.addWidget(self.amount_edit)
        layout.addWidget(self.from_label)
        layout.addWidget(self.from_edit)
        layout.addWidget(self.to_label)
        layout.addWidget(self.to_edit)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_display)
        layout.addWidget(self.convert_button)

        self.setLayout(layout)

    def convert(self):
        amount = self.amount_edit.text()
        source_currency = self.from_edit.text()
        target_currency = self.to_edit.text()

        try:
            amount = float(amount)
        except ValueError:
            self.result_display.setText('Invalid amount')
            return

        try:
            response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{source_currency}')
            data = response.json()
            exchange_rate = data['rates'][target_currency]
            result = amount * exchange_rate
            self.result_display.setText(f'{amount} {source_currency} = {result} {target_currency}')
        except Exception as e:
            self.result_display.setText(f'Error: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = CurrencyConverter()
    converter.show()
    sys.exit(app.exec_())
