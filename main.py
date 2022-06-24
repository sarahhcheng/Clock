import tkinter as display
import datetime
import time
import calendar

print(calendar.calendar(2022))



window = display.Tk()


def clock():
    time_display = time.strftime('%H:%M:%S %p')
    digital_clock_lbl.config(text=time_display)
    digital_clock_lbl.after(1000, clock)


digital_clock_lbl = display.Label(window, text="",
                                      font="Poppins 80")

digital_clock_lbl.pack()

clock()

x = str(datetime.datetime.now())
print(x)

window.mainloop()

