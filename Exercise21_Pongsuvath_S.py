from tkinter import *

def calculate(event):
    h = float(textbox_hight.get())
    h = h/100
    w = float(textbox_wight.get())
    bmi = w/(h*h)
    bmi = round(bmi,1)
    statuslist = ["Tin", "normal", "over_weight", "FAT", "Over size"]
    staus = 0
    if bmi <= 18.5:
        status = statuslist[0]
    elif bmi < 23:
        status = statuslist[1]
    elif bmi < 25.0:
        status = statuslist[2]
    elif bmi < 30.0:
        status = statuslist[3]
    else:
        status = statuslist[4]

    result.configure(text= bmi)
    status_show.configure(text=status,bg="white")

window = Tk()
label_mian = Label(window, text="BMI Culculator",font=100).grid(row=0)

label_height = Label(window,text="Height (Cm.)").grid(row=1,column=1)
textbox_hight = Entry(window)
textbox_hight.grid(row=2,column=1)


label_weight = Label(window,text="Weight (Kg.)").grid(row=3,column=1)
textbox_wight = Entry(window)
textbox_wight.grid(row=4,column=1)

calculate_Button = Button(window,text="Calculate ")
calculate_Button.grid(row=4,column=2)
calculate_Button.bind('<Button-1>',calculate)


result = Label(window,text=" ",font=25)
result.grid(row=6,column=2)



status_Label = Label(window, text="Weight Status",highlightcolor= "blue").grid(row=6, column=0)
status_show = Label(window, text=" ")
status_show.grid(row=6, column=1)

window.mainloop()
