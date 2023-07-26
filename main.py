from tkinter import *
from tkcalendar import *
import datetime

def getDate():
    lable.config(text=cal.get_date())

root = Tk()
root.title('Calendar')
root.geometry('600x400')

# Get the current date
current_date = datetime.date.today()
year, month, day = current_date.year, current_date.month, current_date.day

cal = Calendar(root, selectmode="day", year=year, month=month, day=day)
cal.pack(pady=20)

button = Button(root, text='Date', command=getDate, font=("Arial", 12))
button.pack(pady=20)

lable = Label(root, text="", font=("Arial", 16), bg="lightgray")
lable.pack(pady=20)

root.mainloop()
