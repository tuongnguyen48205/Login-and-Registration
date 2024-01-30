# Login system
# Created by Tuong Bao Nguyen

# Import necessary libraries
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import webbrowser
from PIL import Image, ImageTk
from encryption import *
import csv 
import datetime
from tkinter import filedialog
from tkinter.filedialog import askopenfile

# Create instance of tkinter window and the labels found on the window (title, etc.)
login_window = Tk()
login_window.geometry("400x500")
login_window.title("Login")
login_window.resizable(False,False)

# Create a banner at the top
img_banner = Image.open('resized banner.png')
img_banner = img_banner.resize((480, 140))
img_banner = ImageTk.PhotoImage(img_banner)
lbl_banner = Label(master = login_window, image = img_banner)
lbl_banner.pack()

# Add create account button at the bottom
frm_register = Frame(master = login_window, background = '#538c50')
frm_register.pack(fill = X, side = BOTTOM)
for i in range(2):
    frm_register_grid = Frame(master = frm_register, relief = FLAT)
    frm_register_grid.grid(row = 0, column = i)
    if i == 0:
        lbl_register = Label(master = frm_register_grid, text = "      Don't have an account? Register now!      ", bg = '#538c50',
                            font = ("calibre", 11))
        lbl_register.pack()
    else:
        btn_register = Button(master = frm_register_grid, text = "Register",
                            font = ("calibre", 11), bg = "#264124", fg = "white",
                            activebackground = '#538c50', activeforeground = "black", command = lambda:register())
        btn_register.pack()

# Now insert logo and company name (in this example, I will use my own placeholder
# but these can be changed)
frm_logo = Frame(master = login_window)
frm_logo.pack()
img_logo = Image.open('logo task organiser.png') # This logo can be changed
img_logo = img_logo.resize((100, 100))
img_logo = ImageTk.PhotoImage(img_logo)
for i in range(2):
    frm_logo_grid = Frame(master = frm_logo)
    frm_logo_grid.grid(row = 0, column = i, padx = 10)
    if i == 0:
        lbl_logo = Label(master = frm_logo_grid, image = img_logo)
        lbl_logo.pack()
    else:
        # The following title label can be changed
        lbl_logo_text = Label(master = frm_logo_grid, text = "GROTANIX\nTask Organiser",
                              font = ("calibre", 20, "bold"), fg = "#538c50")
        lbl_logo_text.pack()
        btn_authorship = Button(master = frm_logo_grid, text = "by Tuong Bao Nguyen", font = 1, 
                                fg = "#264124", borderwidth = 0, 
                                command = lambda:webbrowser.open_new(r"https://github.com/tuongnguyen48205"))
        btn_authorship.pack()

# Now create the invalid text
lbl_invalid = Label(master = login_window, text = "Invalid username or password", fg = "SystemButtonFace",
                    font = 10)
lbl_invalid.pack()
invalid_login_flag = False

# Now create the username/email area
frm_username_login = Frame(master = login_window)
frm_username_login.pack(fill = X)
lbl_username_login = Label(master = frm_username_login, text = "          username or email:", font = 10)
lbl_username_login.pack(side = LEFT)
ent_username_login = Entry(master = login_window, width = 30)
ent_username_login.pack(pady = 15)

# Now create password area
frm_password_login = Frame(master = login_window)
frm_password_login.pack(fill = X)
lbl_password_login = Label(master = frm_password_login, text = "          password:", font = 10)
lbl_password_login.pack(side = LEFT)
ent_password_login = Entry(master = login_window, width = 30, show = '*')
ent_password_login.pack(pady = 15)

# Now create login button
frm_login = Frame(master = login_window, relief = RAISED, borderwidth = 5)
frm_login.pack()
btn_login = Button(master = frm_login, text = "Login", font = 10, bg = "#538c50", fg = "black",
                   activebackground = '#264124', activeforeground = "white", command = lambda:verify_login())
btn_login.pack()