import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QCheckBox, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sign up to Dribble")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Title
        title_label = QLabel("Discover the world's top Designers & Creatives.")
        title_label.setObjectName("title")
        layout.addWidget(title_label)

        # Sign up form
        form_label = QLabel("Sign up to Dribble")
        form_label.setObjectName("form_label")
        layout.addWidget(form_label)

        full_name_label = QLabel("Full Name")
        full_name_input = QLineEdit()
        full_name_input.setObjectName("full_name_input")
        layout.addWidget(full_name_label)
        layout.addWidget(full_name_input)

        username_label = QLabel("Username")
        username_input = QLineEdit()
        username_input.setObjectName("username_input")
        layout.addWidget(username_label)
        layout.addWidget(username_input)

        email_label = QLabel("Email Address")
        email_input = QLineEdit()
        email_input.setObjectName("email_input")
        layout.addWidget(email_label)
        layout.addWidget(email_input)

        password_label = QLabel("Password")
        password_input = QLineEdit()
        password_input.setEchoMode(QLineEdit.EchoMode.Password)
        password_input.setObjectName("password_input")
        layout.addWidget(password_label)
        layout.addWidget(password_input)

        terms_checkbox = QCheckBox("I certify that I'm over 16 years old and I agree with the Terms of Service, Privacy Policy and Cookie Policy.")
        terms_checkbox.setObjectName("terms_checkbox")
        layout.addWidget(terms_checkbox)

        create_account_button = QPushButton("Create Account")
        create_account_button.setObjectName("create_account_button")
        layout.addWidget(create_account_button)

        # Apply styles
        self.setStyleSheet("""
            #title {
                font-size: 28px;
                color: #4C4C4C;
                margin-bottom: 20px;
            }
            #form_label {
                font-size: 32px;
                color: #FF6060;
                margin-bottom: 30px;
            }
            QLineEdit {
                font-size: 16px;
                padding: 10px;
                border: 2px solid #DDDDDD;
                border-radius: 8px;
            }
            QPushButton {
                font-size: 18px;
                padding: 10px 20px;
                border: none;
                border-radius: 8px;
                background-color: #FF6060;
                color: white;
            }
            QPushButton:hover {
                background-color: #FF4141;
            }
            QCheckBox {
                font-size: 14px;
                color: #4C4C4C;
            }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
