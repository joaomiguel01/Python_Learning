from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QLineEdit, QPushButton, QCheckBox)
from PyQt5.QtCore import Qt
import sys


class ToDoList(QWidget):
    def __init__(self):
        super().__init__()
        self.task_input = QLineEdit(self)
        self.add_button = QPushButton("Add", self)
        self.title_label = QLabel("To-Do List", self)
        self.initUI()
    

    def initUI(self):
        self.setWindowTitle("To Do List")

        vbox = QVBoxLayout()

        self.setLayout(vbox)

        hbox_task_input = QHBoxLayout()
        hbox_task_input.addWidget(self.task_input)
        hbox_task_input.addWidget(self.add_button)

        self.vbox_all_tasks = QVBoxLayout()


        vbox.addWidget(self.title_label)
        vbox.addLayout(hbox_task_input)
        vbox.addLayout(self.vbox_all_tasks)


        self.add_button.setObjectName("add_button")
        self.task_input.setPlaceholderText("Enter your task")
        self.task_input.setMinimumWidth(500)

        self.setStyleSheet("""
            QLabel{
                font-family: calibri;
                font-size: 50px;
            }
            QLineEdit, QPushButton#add_button{
                font-family: arial;
                font-size: 30px;
                padding: 10px;
            }
            QPushButton{
                font-family: arial; 
            }
            QCheckBox{
                font-family: arial;
                font-weight: bold;
                font-size: 20px;
            }
            QCheckBox::indicator{
                width: 24px;
                height: 24px;
            }
            QPushButton#delete_task_button{
                font-size: 15px;
                font-weight: bold;
                padding: 5px;
            }
            QPushButton#add_button{
                font-weight: bold;
            }
        """)


        # Functions
        self.add_button.clicked.connect(self.add_task)
        self.task_input.returnPressed.connect(self.add_task)


    def add_task(self):
        task_text = self.task_input.text().capitalize()
        if not task_text:
            return

        task_widget = QWidget(self)
        hbox_task = QHBoxLayout(task_widget)
        hbox_task.setContentsMargins(0, 0, 0, 0)

        task_check = QCheckBox(task_text)
        delete_task_button = QPushButton("X")

        delete_task_button.setFixedSize(35, 35)
        delete_task_button.setObjectName("delete_task_button")

        delete_task_button.clicked.connect(
            lambda: self.remove_task(task_widget)
        )
        task_check.stateChanged.connect(
            lambda: self.toggle_task(task_check)
        )

        hbox_task.addWidget(task_check)
        hbox_task.addWidget(delete_task_button)

        self.vbox_all_tasks.addWidget(task_widget)
        self.task_input.clear()


    def remove_task(self, widget: QWidget):
        widget.setParent(None)
        widget.deleteLater()


    def toggle_task(self, check_box: QCheckBox):
        font = check_box.font()
        font.setStrikeOut(check_box.isChecked())
        check_box.setFont(font)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    to_do_app = ToDoList()
    to_do_app.show()
    sys.exit(app.exec_())