from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""
# ---------------------------- TIMER RESET ------------------------------- #


def reset_time():
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    check.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    minute = math.floor(count / 60)
    second = count % 60

    canvas.itemconfig(timer_text, text=f"{minute}:{second:02}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
            check.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=2, row=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tom_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tom_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

button1 = Button(text="Start", command=start_timer)
button1.grid(column=0, row=3)

button2 = Button(text="Reset", command=reset_time)
button2.grid(column=3, row=3)

check = Label(fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 20, "bold"))
check.grid(column=2, row=4)

window.mainloop()
