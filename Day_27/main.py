from tkinter import *

#Miles to kilometers converter program with tkinter
def miles_to_kilometer():
    miles = float(miles_input.get())
    kilometers = miles * 1.609
    kilometer_result.config(text=f"{kilometers}")

# The window
window = Tk()
window.title("Miles to kilometers program")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)

#the entry
miles_input = Entry(width=7)
miles_input.grid(column=1 ,row=0)

#the labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result = Label(text="0")
kilometer_result.grid(column=1, row=1)

kilometer = Label(text="Km")
kilometer.grid(column=2, row=1)

#button
calculate_button = Button(text="calculate", command=miles_to_kilometer)
calculate_button.grid(column=1, row=2)



window.mainloop()