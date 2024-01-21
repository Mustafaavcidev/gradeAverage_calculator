from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("Grade Average")
window.config(pady=20,padx=20)
FONT = "Arial", 12, "italic"

#calculator def
def calculator_average():
    name = name_entry.get()
    if name == "" or not name.isalpha():
        result_label.config(text="Please enter a value alpha")
    else:
        try:
            quiz_note = int(quiz1_entry.get())
            finally_note = int(quiz2_entry.get())
            average_note = (quiz_note + finally_note) / 2
            if quiz_note < 0 or finally_note < 0:
                result_label.config(text="Please enter a value greater than zero..!")
            else:
                if quiz_note > 100 or finally_note > 100:
                    result_label.config(text="Please enter value less than one hundred..!")
                else:
                    if average_note <= 40:
                        result_label.config(text=f"{name}'s average : {average_note} -- status : unsuccessful ")
                    elif (average_note > 41) and (average_note <= 60):
                        result_label.config(text=f"{name}'s average : {average_note} -- status : provisory ")
                    elif average_note >= 61:
                        result_label.config(text=f"{name}'s average : {average_note} -- status : successful ")
        except:
            result_label.config(text="Please enter value numeric..!")
#load the image
image = Image.open("average.png")
image = ImageTk.PhotoImage(image)
#label widget to display the image
image_label = Label(window, image=image)
image_label.pack()
#label
name_label = Label(text="Please enter name : ", font=FONT, pady=10, padx=10)
name_label.pack()
name_entry = Entry()
name_entry.focus()
name_entry.pack()
quiz1_label = Label(text="please enter quiz note : ", font=FONT, padx=10,pady=10)
quiz1_label.pack()
quiz1_entry = Entry()
quiz1_entry.pack()
quiz2_label = Label(text="please enter finally note : ", font=FONT, padx=10,pady=10)
quiz2_label.pack()
quiz2_entry = Entry()
quiz2_entry.pack()
calculation_button = Button(text="calculator", font=FONT, command=calculator_average)
calculation_button.pack()
result_label = Label(font=FONT)
result_label.pack()

window.mainloop()


