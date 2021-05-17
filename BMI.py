from tkinter import *

BMI = Tk()
BMI.title("MBI-calulator")
BMI.geometry("500x500")

Male = IntVar()
Female = IntVar()
Height= StringVar
Weight = StringVar()
Age = StringVar()

heading_label = Label(BMI, text="Mzwandile Stuurman ")
instruction_label= Label(BMI, text=" Enter your weight, height and gender")
heading_label.pack()
instruction_label.pack()


frame_1 = LabelFrame(BMI) # creating frame for inputs
def conditions():
    if BMI_entry.get()


def BMI_funcion():
    weight = weight_entry.get()
    height = height_entry.get()
    bmi = weight/(height/100)^2
    return bmi

def Ideal_BMI_function():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    age = float(age_entry)
    if age_menu.get() == "Female":
        ideal = 0.5*weight/(height/100)^2+11.5
        return ideal
    else:
        if age_menu.get() == "Male":
            ideal = 0.5 * weight / (height / 100) ^ 2 + 0.03 * age + 11
            return ideal

weight_label = Label(frame_1, text="Weight:")
weight_entry = Entry(frame_1)
kilogram_weight = Label(frame_1, text="Kilograms")
gender_label= Label(frame_1, text="Gender")

height_label = Label(frame_1, text="Height")
height_entry= Entry(frame_1)
height_entry.pack()
height_label.pack()


age_menu = Menubutton(frame_1, text="Select", relief=RAISED)

age_menu.menu = Menu(age_menu, tearoff=0)
age_menu['menu'] = age_menu.menu


age_menu.menu.add_checkbutton(label="Male", variable=Male)
age_menu.menu.add_checkbutton(label="Female", variable=Female)

BMI_entry = Entry(BMI)
BMI_label = Label(BMI, text="BMI")
BMI_entry.pack()
BMI_label.pack()

Ideal_BMI_entry= Entry(BMI)
Ideal_BMI_label=Entry(BMI)
Ideal_BMI_entry.pack()
Ideal_BMI_label.pack()



age_label=Label(frame_1,text="Age")
age_entry=Entry(frame_1)




calclulate_BMI_button= Button(BMI, text="Calculate your Ideal Body Mass Index")
clear_button= Button(BMI, text="clear")
exit_button=Button(BMI, text="Exit")

calclulate_BMI_button.pack()
age_label.pack()
age_entry.pack()
age_menu.pack()
gender_label.pack()
weight_entry.pack()
weight_label.pack()
kilogram_weight.pack()
frame_1.pack()










BMI.mainloop()

