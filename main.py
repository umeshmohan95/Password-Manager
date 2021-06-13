from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = 9
    nr_symbols = 1
    nr_numbers = 2

    password_list = []

    for char in range(1, nr_letters + 1):
      password_list.append(random.choice(letters))

    for char in range(1, nr_symbols + 1):
      password_list += random.choice(symbols)

    for char in range(1, nr_numbers + 1):
      password_list += random.choice(numbers)


    random.shuffle(password_list)


    password = ""
    for char in password_list:
      password += char

    print(f"Your password is: {password}")
    password_input.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = web_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {website: {
        'email': email,
        'password': password
    }}
    if len(web_input.get()) == 0 or len(password_input.get())==0:
        messagebox.showinfo(title='Oops',message="Please make sure you haven't left any fields empty")

    else:
        is_ok = messagebox.askokcancel(title=web_input.get(), message=f'These are the details entered: \nEmail: {email_input.get()} '
                               f"\nPassword: {password_input.get()} \nIs it ok to save?")
        #
        if is_ok:
            # with open("data.txt",'a') as data_file:
            #     data_file.write(f"{web_input.get()} | {email_input.get()} | {password_input.get()}\n")
            #     web_input.delete(0,END)
            #     password_input.delete(0,END)

            try:
                with open("data.json", 'r') as data_file:
                    # Read Old data
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                # updating the old data with new data
                data.update(new_data)

                with open("data.json", 'w') as data_file:
                    # saving new data
                    json.dump(data, data_file, indent=4)
            finally:
                web_input.delete(0,END)
                password_input.delete(0,END)

    print(web_input.get())
    print(password_input.get())

# ---------------------------- UI SETUP ------------------------------- #


def search_button():
    password_input.delete(0, END)
    # with open("data.json", 'r') as data_file:
    #     # Read Old data
    #     data = json.load(data_file)
    #     pwd = data[web_input.get()]['password']
    #     password_input.insert(END, pwd)
    #     messagebox.showinfo('Password', f'Please find  the password for\nEmail: {web_input.get()}\n'
    #                         f'Password: {pwd}')

    try:
        with open("data.json", 'r') as data_file:
            # Read Old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo('Error', 'No Data file found')
    else:
        if web_input.get() in data:
            pwd = data[web_input.get()]['password']
            messagebox.showinfo('Password', f'Please find  the password for\nEmail: {web_input.get()}\n'
                                     f'Password: {pwd}')
        else:
            messagebox.showinfo('Password', f'No details for {web_input.get()} exists')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=240, height=240)
logo_img = PhotoImage(file='tomato.png')
canvas.create_image(103, 100, image=logo_img)
canvas.grid(column = 2, row=1)

# main_lable = Label(text= 'Timer', font =(FONT_NAME, 36, 'bold'), fg=GREEN, bg=YELLOW)
# main_lable.grid(column = 2, row=1)

web_lable = Label(text='Website: ')
web_lable.grid(column = 1, row=2)

web_input = Entry(width=58)
web_input.grid(column=2, row=2, columnspan=2)
web_input.focus()

search_button = Button(text = 'Search',width=15, highlightthickness=0,command=search_button )
search_button.grid(column=3, row=2)

email_lable = Label(text='Email/Username: ')
email_lable.grid(column = 1, row=3)

email_input = Entry(width=58)
email_input.grid(column=2, row=3, columnspan=2)
email_input.insert(END, 'umesh.mohan995@gmail.com')

password_lable = Label(text='Password: ')
password_lable.grid(column = 1, row=4)

password_input = Entry(width=39)
password_input.grid(column=2, row=4)

generate_button = Button(text = 'Generate Password', highlightthickness=0,command=password_generator )
generate_button.grid(column=3, row=4)

add_button = Button(text = 'add', highlightthickness=0, width=50, command=save)
add_button.grid(column=2, row=5, columnspan=2)

window.mainloop()





