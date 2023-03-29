# import random and string module
import string
import random
# import tkinker for window
import tkinter as tk


# Creating a function for generating passwords
def generate_password():
    password_length = int(password_length_entry.get())

    # defining all characters
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Convert the list into a string
    password = "".join(random.choice(all_characters) for i in range(password_length))

    # save all passwords in a file
    with open('passwords.txt', 'a') as f:
        f.write('Your ' + str(password_length) + '-characters password: ' + password + '\n')

    password_label.config(text='Generated Password: ' + password)


# Creating a 350x200 window
root = tk.Tk()
root.title('Random Password Generator')
root.geometry('350x200')

password_length_label = tk.Label(root, text='Enter the length of the password: ')
password_length_label.pack()

password_length_entry = tk.Entry(root)
password_length_entry.pack()

# Creating password generate button
generate_button = tk.Button(root, text='Generate Password', command=generate_password)
generate_button.pack()

password_label = tk.Label(root, text='')
password_label.pack()

root.mainloop()
