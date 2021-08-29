from tkinter import *


def shifting_form():
    screen.destroy()
    import student_login


screen = Tk()

# -----Variables
email = StringVar()
password = StringVar()

# -----Screen GUI
screen.geometry("1350x900")
screen.config(bg="#34495E")
screen.title("Registration")

title = Label(text="LOG IN", font=("Broadway", 72, "bold"), pady="5", bg="#000080", fg="#008080").pack(pady="50")

# login frame
login_frame = Frame(screen, width="700", height="500", bg="#946f6a")
login_frame.pack()

Fac_login = Button(login_frame, text="Faculty Login", command=shifting_form, bg='#7fffd4', fg='black',
                   font=('Calibri', 20, 'bold'))
Fac_login.grid(row=0, column=0)

Stu_login = Button(login_frame, text="Student Login", command=shifting_form, bg='#7fffd4', fg='black',
                   font=('Calibri', 20, 'bold'))
Stu_login.grid(row=0, column=2)

screen.mainloop()