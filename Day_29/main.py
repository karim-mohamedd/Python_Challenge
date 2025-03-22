from tkinter import *
from tkinter import messagebox
import random
import  json

EXPECTED_PASS = 8
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    pass_len = len(password)

    new_data = {
        website:
                {
                    "email":email,
                    "password":password
                }
        }
    
    if pass_len >= EXPECTED_PASS and len(website) > 3:
        try:
            with open("Data.json", mode="r") as data_file:
            # To update data in json format: (1) Reading the data by "load()" Method  (2) Updating old data "data.update()" Method  (3) Saving the updated data by using "dump()"Method
            
            # Reading the data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("Data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:                                               # This will work if everything in 'try' works successfully
            # Updating the data
             data.update(new_data)

             with open("Data.json", mode="w") as data_file: 
            # Writing the data
                json.dump(data, data_file, indent=4)               
                messagebox.showinfo(title=website , message=f"Your private information added successfully")
        finally:
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            website_entry.focus()
    else:
        messagebox.showerror(title="not valid", message=f"Sorry check the website: {website}\nand make sure your password: {password} is more than 8 characters")

#----------------------------- Search -----------------------------------------#

def Find_Password():
    website = website_entry.get()
    try:
        with open("Data.json", mode="r") as data_file:
            #reading the data
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror("No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="error", message=f"No details for This Website: '{website}' exists.")

# ---------------------------- UI SETUP --------------------------------------- #
window = Tk()
window.title("password man")
window.config(padx=20,pady=20)
#-------------------------------- Labels -------------------------------------- #
website_label = Label(text="Website/Username: ")
website_label.grid(row=1, column=0, sticky="e")

email_label = Label(text="Email: ")
email_label.grid(row=2, column=0, sticky="e")

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0, sticky="e")
#-------------------------------- Entries ------------------------------------- #
website_entry = Entry(width=39)
website_entry.grid(row=1, column=1, columnspan=2, pady=5)
website_entry.focus()

email_entry = Entry(width=39)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "karimelwaraky50@gmail.com")

password_entry = Entry(width=26)
password_entry.grid(row=3, column=1, pady=5, sticky="e")
#------------------------------ Buttons ---------------------------------------- #
generate_password_button = Button(text="Generate Password", width=15, command=generate_password)
generate_password_button.grid(row=3, column=2, padx=1, pady=3)

add_password_button = Button(text="Add", width=33, command=add_password)
add_password_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=15, command=Find_Password)
search_button.grid(row=1, column=2, padx=1, pady=3)
#------------------------------------------------------------------------------- #
canvas = Canvas(width=200, height=200, highlightthickness=0)
password_man = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=password_man)
canvas.grid(row=0, column=1)
window.mainloop()
