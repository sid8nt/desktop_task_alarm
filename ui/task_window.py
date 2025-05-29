from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
import random

class TaskWindow(QDialog):
    def __init__(self, task_type):
        super().__init__()
        self.setWindowTitle("Complete Task to Dismiss Alarm")
        self.setMinimumSize(400, 200)
        layout = QVBoxLayout()

        self.input = QLineEdit()
        self.submit_btn = QPushButton("Submit")
        self.submit_btn.setStyleSheet("font-size: 16px; padding: 8px;")
        self.submit_btn.clicked.connect(self.check_answer)
        self.input.returnPressed.connect(self.check_answer)

        if task_type == "Math Task":
            self.a = random.randint(10, 50)
            self.b = random.randint(10, 50)
            self.answer = str(self.a + self.b)
            layout.addWidget(QLabel(f"Solve: {self.a} + {self.b}"))
        else:
            self.phrase = "I am focused and ready"
            self.answer = self.phrase
            layout.addWidget(QLabel(f"Type the phrase exactly: '{self.phrase}'"))


        layout.addWidget(self.input)
        layout.addWidget(self.submit_btn)
        self.setLayout(layout)

    def check_answer(self):
        if self.input.text().strip() == self.answer:
            self.accept()
        else:
            self.input.setText("")
            self.input.setPlaceholderText("Try again...")
