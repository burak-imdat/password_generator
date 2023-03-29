# import random and string module
import string
import random
# importing PyQt5 for new window and creating an application
from PyQt5 import QtWidgets


# Creating a function for generating passwords
def generate_password():
    password_length = int(password_length_entry.text())

    # defining all characters
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Convert the list into a string
    password = "".join(random.choice(all_characters) for i in range(password_length))

    # save all passwords in a file
    with open('passwords.txt', 'a') as f:
        f.write('Your ' + str(password_length) + '-characters password: ' + password + '\n')

    password_label.setText('Generated Password: ' + password)


# Creating a 350x200 window
app = QtWidgets.QApplication([])
window = QtWidgets.QWidget()
window.setWindowTitle('Random Password Generator')
window.setGeometry(300,300,350,200)

layout = QtWidgets.QVBoxLayout()

password_length_label = QtWidgets.QLabel('Enter the length of the password: ')
layout.addWidget(password_length_label)

password_length_entry = QtWidgets.QLineEdit()
layout.addWidget(password_length_entry)

# Creating password generate button
generate_button = QtWidgets.QPushButton('Generate Password')
generate_button.clicked.connect(generate_password)
layout.addWidget(generate_button)

password_label = QtWidgets.QLabel("")
layout.addWidget(password_label)

window.setLayout(layout)
window.show()

app.exec_()
