from tkinter import *
from tkinter import messagebox


def get_height():

# This function gets height value from Entry field

    height = float(ENTRY2.get())
    return height


def get_weight():

# This function gets weight value from Entry field

    weight = float(ENTRY1.get())
    return weight


def calculate_bmi(a=""): # "a" is there because the bind function gives an argument to the function....
    print(a)

# This function calculates the result

    try:
        height = get_height()
        weight = get_weight()
        height = height / 100.0
    bmi = weight / (height ** 2)
    except ZeroDivisionError:
    messagebox.showinfo("Result", "Please enter positive height:")
    except ValueError:
messagebox.showinfo("Result", "Please enter valid data:")
else:
if bmi <= 15.0:
res = "Your BMI is " + str(bmi) + "Remarks: Very severely underweight!!"
messagebox.showinfo("Result", res)
elif 15.0 < bmi <= 16.0:
res = "Your BMI is " + str(bmi) + "Remarks: Severely underweight!"
messagebox.showinfo("Result", res)
elif 16.0 < bmi < 18.5:
res = "Your BMI is " + str(bmi) + "Remarks: Underweight!"
messagebox.showinfo("Result", res)
elif 18.5 <= bmi <= 25.0:
res = "Your BMI is " + str(bmi) + "Remarks: Normal."
messagebox.showinfo("Result", res)
elif 25.0 < bmi <= 30:
res = "Your BMI is " + str(bmi) + "Remarks: Overweight."
messagebox.showinfo("Result", res)
elif 30.0 < bmi <= 35.0:
res = "Your BMI is " + str(bmi) + "Remarks: Moderately obese!"
messagebox.showinfo("Result", res)
elif 35.0 < bmi <= 40.0:
res = "Your BMI is " + str(bmi) + "Remarks: Severely obese!"
messagebox.showinfo("Result", res)
else:
res = "Your BMI is " + str(bmi) + "Remarks: Super obese!!"
messagebox.showinfo("Result", res)


if __name__ == '__main__':
root = Tk()
root.bind("", calculate_bmi)
root.geometry("900x700")
root.configure(bg="#ffffff")
root.title("BMI Calculator")
root.resizable(width=False, height=False)


frame = Frame(root, width=750, height=550, relief='raised', bg='#222')
frame.place(relx=0.15, rely=0.1)

LABLE = Label(root, bg="#307678", text="IDEAL BODY MASS INDEX CALCULATOR", font=("Helvetica", 15, "bold"), pady=10)
LABLE.place(x=300, y=0)
LABLE1 = Label(root, bg="#cef0f1", text="Enter Weight (in kg):", bd=6,
font=("Helvetica", 10, "bold"), pady=5)
LABLE1.place(x=155, y=160)
ENTRY1 = Entry(root, bd=8, width=6, font="Roboto 11")
ENTRY1.place(x=340, y=160)
LABLE2 = Label(root, bg="#cef0f1", text="Enter Height (in cm):", bd=6,
font=("Helvetica", 10, "bold"), pady=5)
LABLE2.place(x=155, y=121)
ENTRY2 = Entry(root, bd=8, width=6, font="Roboto 11")
ENTRY2.place(x=340, y=121)
BUTTON = Button(bg="#2187e7", bd=12, text="BMI", padx=33, pady=15, command=calculate_bmi,
font=("Helvetica", 20, "bold"))
BUTTON.grid(row=3, column=0, sticky=W)
BUTTON.place(x=450, y=250)

gender = Label(frame, text="Gender:", bg='#222', fg='white')
gender.place(rely=0.52, relx=0.1)

age = Label(frame, text="Age:", bg='#222', fg='white')
age.place(rely=0.8, relx=0.1)
age_entry = Entry(frame, state='readonly')
age_entry.place(rely=0.8, relx=0.4)

options = ['Select...', 'Male', "Female"]
variable = StringVar(frame)
variable.set(options[0])


def activate(value):
variable.set(value)
if value != "Select...":
age_entry.config(state='normal')
else:
age_entry.config(state='readonly')


gender_menu = OptionMenu(frame, variable, *options, command=activate)
gender_menu.place(relx=0.4, rely=0.5)

root.mainloop()
