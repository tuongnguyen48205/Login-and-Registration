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

def verify_login():
    '''
    This function verifies that the password the user inputted matches their username/email.
    If it does, the user will be granted access
    '''
    global ent_username
    global ent_password
    global lbl_invalid
    global invalid_login_flag

    # First check if the username/email entry is blank
    username = ent_username_login.get()
    password = ent_password_login.get()

    if username == '':
        if invalid_login_flag is False:
            invalid_login_flag = True
            lbl_invalid.config(fg = "red")
        return

    # Now decrypt the csv file and open it
    decrypt("Login and registration/users.csv")
    user_csv = open("Login and registration/users.csv")

    # First check if the username/email string contains the '@' symbol. If it does, it
    # means that the user has entered their email and if it does not, it means that the user
    # has entered their username. This is used to determine which part of the csv needs to 
    # be checked
    logged_in = False # A flag used to check if the user has logged in or not
    account = 'placeholder'

    for line in csv.reader(user_csv):
        # Skip the first line
        if line[0] == "email":
            pass
        elif username == line[0] or username == line[9]:
            # Check if the password matches, the user may login
            if password == line[8]:
                logged_in = True
                account = line
                break
            else:
                continue

    # If the user inputs do not exist, raise invalid text
    if logged_in is False:
        if invalid_login_flag is False:
            invalid_login_flag = True
            lbl_invalid.config(fg = "red")
        # Reencrypt the csv file
        generate_key()
        encrypt("Login and registration/users.csv")
        user_csv.close()
        return

    # Always encrypt the csv file after. Generate a new key every time for security and so the key
    # can't be copied
    generate_key()
    encrypt("Login and registration/users.csv")
    user_csv.close()

    # The user is granted access
    access_granted(account)

def access_granted(account):
    '''
    This function allows for the user to access whatever is on the other side
    of this login and reigstration system whether it be a task manager, a databse,
    a daily planner, etc. In this case, it closes the main login window. It has the 
    users account as the argument so that it can be personalised to each user
    '''
    # Create a new window for whatever application
    global login_window
    login_window.destroy()
    application_window = Tk()
    application_window.attributes('-fullscreen', True)
    application_window.title("Application")

    # Place a bar at top and bottom
    frm_bar = Frame(master = application_window, height = 100, bg = "#538c50")
    frm_bar.pack(fill = X, side = TOP)

    # Quick summary of the users information
    lbl_user_summary_title = Label(master = application_window, text = "User Summary:", font = ('ariel', 80, 'bold'))
    lbl_user_summary_title.pack()
    lbl_user_summary = Label(master = application_window, font = ('ariel', 30), text = f"Welcome {account[4]} {account[2]} {account[3]}\nemail: {account[0]}\nphone number: {account[1]}\ngender: {account[5]}\nbirthday (YYYY-MM-DD): {account[6]}\nnationality: {account[7]}\nusername: {account[8]}")
    lbl_user_summary.pack()

    # Place in their profile iamge
    profimg = Image.open(f'{account[10]}')
    profimg = profimg.resize((300, 300))
    profimg = ImageTk.PhotoImage(profimg)
    lbl_profimg = Label(image = profimg)
    lbl_profimg.pack()

    # Say happy birtday if it's the users's birthday
    today = datetime.date.today()
    if str(today)[9:5:-1] == account[6][9:5:-1]:
        lbl_happybday = Label(master = application_window, text = "Happy Birthday!!", font = ('ariel', 30))
        lbl_happybday.pack()

    # Create an exit button to close the application
    frm_exit = Frame(master = application_window, relief = RAISED, height = 100, bg = "#538c50")
    frm_exit.pack(fill = X, side = BOTTOM)
    btn_exit = Button(master = frm_exit, text = "Exit", font = ('ariel', 30, 'bold'), command = lambda:application_window.destroy())
    btn_exit.pack(side = BOTTOM)

    application_window.mainloop()

#---------------------------------------------------------------------------------------------------------------------------------------#
# The following code is all related to the registration process                                                                         #
#---------------------------------------------------------------------------------------------------------------------------------------#

# The following will temporary store all the users info which will be encrypted later in a csv
user_info = ["email", "phone_number", "firstname", "surname", "title", "gender", "birthday", "nationality", "password", "username", "profile_image"]

register_window = "placeholder" # This acts as a placeholder for the registration window

def register():
    '''
    This function allows for the user to register an account
    '''
    global register_window

    # Create instance of tkinter window and the labels found on the window (title, etc.)
    register_window = Toplevel()
    register_window.geometry("800x500")
    register_window.title("Register")
    register_window.resizable(False,False)
    
    # Create a banner along the bottom of the window
    img_register_banner = Image.open('register banner.png')
    img_register_banner = img_register_banner.resize((960, 140))
    img_register_banner.image = img_register_banner
    img_register_banner = ImageTk.PhotoImage(img_register_banner)
    lbl_register_banner = Label(master = register_window, image = img_register_banner)
    lbl_register_banner.image = img_register_banner
    lbl_register_banner.pack(side = BOTTOM)

    # Now insert logo and company name (in this example, I will use my own placeholder
    # but these can be changed)
    frm_register_logo = Frame(master = register_window)
    frm_register_logo.pack()
    img_register_logo = Image.open('logo task organiser.png') # This logo can be changed
    img_register_logo = img_register_logo.resize((150, 150))
    img_register_logo = ImageTk.PhotoImage(img_register_logo)
    for i in range(2):
        frm_register_logo_grid = Frame(master = frm_register_logo)
        frm_register_logo_grid.grid(row = 0, column = i, padx = 10)
        if i == 0:
            lbl_register_logo = Label(master = frm_register_logo_grid, image = img_register_logo)
            lbl_register_logo.pack()
        else:
            # The following title label can be changed
            lbl_register_logo_text = Label(master = frm_register_logo_grid, text = "GROTANIX Task Organiser",
                                font = ("calibre", 25, "bold"), fg = "#538c50")
            lbl_register_logo_text.pack()
            lbl_register = Label(master = frm_register_logo_grid, text = "Registration",
                                font = ("calibre", 20, "bold"), fg = "#264124")
            lbl_register.pack()

    # Now to get the users information
    # Start with phase 1 by getting the users email
    phase1()

    register_window.mainloop()

# The following modules need to be accessed by multiple functions regarding the email
lbl_email = "placeholder"
ent_email = "placeholder"
frm_continue = "placeholder"
btn_continue = "placeholder"
lbl_invalid_email = "placeholder"
frm_back = "placeholder"
btn_back = "placeholder"
current_screen = 0

def phase1():
    '''
    This is the email screen
    '''
    global register_window
    global lbl_email
    global ent_email
    global frm_continue
    global btn_continue
    global current_screen

    current_screen = 0

    # Create a place to enter the email
    lbl_email = Label(master = register_window, text = "\nPlease enter your email address:", font = 10)
    lbl_email.pack()
    ent_email = Entry(master = register_window, width = 40)
    ent_email.pack(pady = 10)

    # Create a continue button
    frm_continue = Frame(master = register_window, relief = RAISED, borderwidth = 5)
    frm_continue.pack(side = BOTTOM)
    btn_continue = Button(master = frm_continue, text = "Continue", font = 10, bg = "#538c50", fg = "black",
                        activebackground = '#264124', activeforeground = "white", command = lambda:continue1())
    btn_continue.pack()

flagged_email = False # This keeps track of if the "invalid email address" has appeared

def continue1():
    '''
    Here we will verify if the email inputted is valid and continue to
    the next step of registration
    '''
    global register_window
    global ent_email
    global lbl_email
    global flagged_email
    global lbl_invalid_email
    global frm_back
    global btn_back
    global user_info

    # Get the email from the entry
    email = ent_email.get()

    # Email must contain @ symbol and .com. The minimum length for an email is also 7 characters
    # This will also check if the entry has been left blank
    if (".com" not in email) or ('@' not in email) or (len(email) < 7) or (' ' in email):
        if flagged_email is False:
            flagged_email = True
            lbl_invalid_email = Label(master = register_window, text = "Invalid email address. Try again.", font = 10, fg = "red")
            lbl_invalid_email.pack()
        else:
            lbl_invalid_email.config(text = "Invalid email address. Try again.")
    else:
        # Now check if the email already exists
        decrypt('Login and registration/users.csv')
        csv_file = open('Login and registration/users.csv')
        for line in csv.reader(csv_file):
            if line[0] == email:
                if flagged_email is True:
                    lbl_invalid_email.config(text = "This email address already exists.")
                else:
                    flagged_email = True
                    lbl_invalid_email = Label(master = register_window, text = "This email address already exists.", font = 10, fg = "red")
                    lbl_invalid_email.pack()
                # Encrypt it again
                generate_key()
                encrypt('Login and registration/users.csv')
                csv_file.close()
                return
            else:
                continue

        # Encrypt it again
        generate_key()
        encrypt('Login and registration/users.csv')
        csv_file.close()

        # Remove the email entry and prompt and invalid text
        lbl_email.forget()
        ent_email.forget()
        flagged_email = False
        try:
            lbl_invalid_email.forget()
        except Exception:
            pass
        
        # Place email into the users info list
        user_info[0] = email

        # Add a back button
        frm_back = Frame(master = register_window)
        frm_back.pack(fill = X)
        btn_back = Button(master = frm_back, text = "             ↩ Previous", font = 10, borderwidth = 0, fg = "#264124",
                          command = lambda:previous())
        btn_back.pack(side = LEFT)

        phase2()

def previous():
    '''
    This function sends the user to the previous screen
    '''
    global current_screen
    global frm_back
    global btn_back
    global frm_continue
    global btn_continue
    global lbl_phone
    global ent_phone
    global lbl_invalid_phone
    global lbl_firstname
    global ent_firstname
    global lbl_surname
    global ent_surname
    global frm_name
    global frm_name_grid
    global lbl_invalid_name
    global lbl_title
    global opt_title
    global lbl_gender
    global opt_gender
    global lbl_invalid_choice
    global frm_gender_grid
    global frm_gender
    global lbl_birthday
    global cmb_date
    global cmb_month
    global cmb_year
    global frm_date
    global frm_date_grid
    global lbl_invalid_date
    global lbl_nationality
    global cmb_nationality
    global lbl_invalid_nationality
    global lbl_password
    global ent_password
    global lbl_confirm
    global ent_confirm
    global frm_password
    global frm_password_grid
    global btn_show
    global lbl_invalid_password
    global lbl_username
    global ent_username
    global lbl_invalid_username
    global lbl_avatar
    global lbl_pfp
    global btn_upload
    global frm_avatar
    global frm_avatar_grid
    global lbl_final
    global btn_final

    if current_screen == 1:
        frm_back.forget()
        btn_back.forget()
        btn_continue.forget()
        frm_continue.forget()
        try:
            lbl_phone.forget()
            ent_phone.forget()
            lbl_invalid_phone.forget()
        except Exception:
            pass
        phase1()
    elif current_screen == 2:
        lbl_firstname.forget()
        ent_firstname.forget()
        lbl_surname.forget()
        ent_surname.forget() 
        lbl_surname
        frm_name_grid.forget()
        frm_name.forget()
        try:
            lbl_invalid_name.forget()
        except Exception:
            pass
        phase2()
    elif current_screen == 3:
        lbl_title.forget()
        opt_title.forget()
        lbl_gender.forget()
        opt_gender.forget()
        frm_gender_grid.forget()
        frm_gender.forget()
        try:
            lbl_invalid_choice.forget()
        except Exception:
            pass
        phase3()
    elif current_screen == 4:
        lbl_birthday.forget()
        cmb_date.forget()
        cmb_month.forget()
        cmb_year.forget()
        frm_date.forget()
        frm_date_grid.forget()
        try:
            lbl_invalid_date.forget()
        except Exception:
            pass
        phase4()
    elif current_screen == 5:
        lbl_nationality.forget()
        cmb_nationality.forget()
        try:
            lbl_invalid_nationality.forget()
        except Exception:
            pass
        phase5()
    elif current_screen == 6:
        lbl_password.forget()
        ent_password.forget()
        lbl_confirm.forget()
        ent_confirm.forget()
        frm_password.forget()
        frm_password_grid.forget()
        btn_show.forget()
        try:
            lbl_invalid_password.forget()
        except Exception:
            pass
        phase6()
    elif current_screen == 7:
        lbl_username.forget()
        ent_username.forget()
        try:
            lbl_invalid_username.forget()
        except Exception:
            pass
        phase7()
    elif current_screen == 8:
        lbl_avatar.forget()
        lbl_pfp.forget()
        btn_upload.forget()
        frm_avatar.forget()
        frm_avatar_grid.forget()
        phase8()
    elif current_screen == 9:
        lbl_final.forget()
        btn_final.forget()
        phase9()

# The following modules need to be accessed by multiple functions regarding the users phone number
lbl_phone = "placeholder"
ent_phone = "placeholder"
lbl_invalid_phone = "placeholder"

def phase2():
    '''
    We will now get the users phone number
    '''
    global register_window
    global lbl_phone
    global ent_phone
    global frm_continue
    global btn_continue
    global current_screen

    current_screen = 1

    # Create a place to enter the phone number
    lbl_phone = Label(master = register_window, text = "\nPlease enter your phone number (if applicable):", font = 10)
    lbl_phone.pack()
    ent_phone = Entry(master = register_window, width = 40)
    ent_phone.pack(pady = 10)

    # Redirect continue button
    btn_continue.config(command = lambda:continue2())

flagged_phone = False # This keeps track of if the "invalid phone number" has appeared

def continue2():
    '''
    Here we will verify if the phone number inputted is valid and continue to
    the next step of registration
    '''
    global register_window
    global ent_phone
    global lbl_phone
    global flagged_phone
    global lbl_invalid_phone
    global user_info

    # Get the phone number from the entry
    phone = ent_phone.get()

    # Either it is left empty or the phone number must be a digit
    if phone == '':
        pass
    elif phone.isdigit() is False or len(phone) > 20:
        if flagged_phone is False:
            flagged_phone = True
            lbl_invalid_phone = Label(master = register_window, text = "Invalid phone number. Try again.", font = 10, fg = "red")
            lbl_invalid_phone.pack()
            return
        else:
            lbl_invalid_phone.config(text = "Invalid phone number. Try again.")
            return
    else:
        # Now check if the number already exists
        decrypt('Login and registration/users.csv')
        csv_file = open('Login and registration/users.csv')
        for line in csv.reader(csv_file):
            if line[1] == phone:
                if flagged_phone is True:
                    lbl_invalid_phone.config(text = "This phone number already exists.")
                else:
                    flagged_phone = True
                    lbl_invalid_phone = Label(master = register_window, text = "This phone number already exists.", font = 10, fg = "red")
                    lbl_invalid_phone.pack()
                # Encrypt it again
                generate_key()
                encrypt('Login and registration/users.csv')
                csv_file.close()
                return
            else:
                continue

        # Encrypt it again
        generate_key()
        encrypt('Login and registration/users.csv')
        csv_file.close()

    # Remove the phone entry and prompt and invalid text
    lbl_phone.forget()
    ent_phone.forget()
    flagged_phone = False
    try:
        lbl_invalid_phone.forget()
    except Exception:
        pass
        
    # Place phone into the users info list
    user_info[1] = phone

    phase3()

# The following modules need to be accessed by multiple functions regarding the users phone number
lbl_firstname = "placeholder"
ent_firstname = "placeholder"
lbl_surname = "placeholder"
ent_surname = "placeholder"
lbl_invalid_name = "placeholder"
frm_name = "placeholder"
frm_name_grid = "placeholder"

def phase3():
    '''
    We will now get the users firstname and lastname
    '''
    global register_window
    global lbl_firstname
    global ent_firstname
    global lbl_surname
    global ent_surname
    global frm_continue
    global btn_continue
    global current_screen
    global frm_name
    global frm_name_grid

    current_screen = 2

    # Create a place to enter the firstname and surname
    frm_name = Frame(master = register_window)
    frm_name.pack()
    for i in range(2):
        for j in range(2):
            frm_name_grid = Frame(master = frm_name, relief = FLAT)
            frm_name_grid.grid(row = i, column = j)
            if i == 0 and j == 0:
                lbl_firstname = Label(master = frm_name_grid, text = "\nEnter your firstname:", font = ("calibre", 11))
                lbl_firstname.pack()
            elif i == 0 and j == 1:
                lbl_surname = Label(master = frm_name_grid, text = "\nEnter your surname:", font = ("calibre", 11))
                lbl_surname.pack()
            elif i == 1 and j == 0:
                ent_firstname = Entry(master = frm_name_grid, width = 40)
                ent_firstname.pack(pady = 10, padx = 15)
            elif i == 1 and j == 1:
                ent_surname = Entry(master = frm_name_grid, width = 40)
                ent_surname.pack(pady = 10, padx = 15)

    # Redirect continue button
    btn_continue.config(command = lambda:continue3())

flagged_name = False # This keeps track of if the "invalid name" has appeared

def continue3():
    '''
    Here we will verify if the name inputted is valid and continue to
    the next step of registration
    '''
    global register_window
    global ent_firstname
    global lbl_firstname
    global lbl_surname
    global ent_surname
    global flagged_name
    global lbl_invalid_name
    global user_info
    global frm_name
    global frm_name_grid

    # Get the phone number from the entry
    firstname = ent_firstname.get()
    surname = ent_surname.get()

    invalid_flag = False
    invalid_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
                       '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
                       '<', '>', '/', ',', '.', '?', '"', ']', '[', '{', 
                       '}', '\'', '|', '`', '-', '_', '+', '=', ';', ':']

    # Check if either entry has been left blank
    if firstname == '' or surname == '':
        invalid_flag = True
    for i in invalid_symbols:
        if i in firstname or i in surname:
            invalid_flag = True
    
    if invalid_flag is True:
        if flagged_name is False:
            flagged_name = True
            lbl_invalid_name = Label(master = register_window, text = "Invalid firstname or lastname", font = 10, fg = "red")
            lbl_invalid_name.pack()
        else:
            pass
    else:
        # Place the name into the user info list
        user_info[2] = firstname
        user_info[3] = surname

        # Remove the name entries and prompts and invalid text
        lbl_firstname.forget()
        ent_firstname.forget()
        lbl_surname.forget()
        ent_surname.forget()
        frm_name_grid.forget()
        frm_name.forget()
        flagged_name = False
        try:
            lbl_invalid_name.forget()
        except Exception:
            pass

        phase4()

# The following modules need to be accessed by multiple functions regarding the users gender
var_title = "placeholder"
opt_title = "placeholder"
lbl_gender = "placeholder"
var_gender = "placeholder"
opt_gender = "placeholder"
lbl_invalid_choice = "placeholder"
frm_gender = "placeholder"
frm_gender_grid = "placeholder"

def phase4():
    '''
    This will get the users title and gender
    '''
    global register_window
    global frm_continue
    global btn_continue
    global current_screen
    global lbl_title 
    global var_title 
    global opt_title
    global lbl_gender 
    global var_gender
    global opt_gender 
    global lbl_invalid_choice
    global frm_gender 
    global frm_gender_grid 

    current_screen = 3

    # Create options for the title
    title_options = ["Please select below", "-------------------", "Mr", "Mrs", "Ms", "Miss", "Dr", "Other", "Prefer not to say"] # More can be added if necessary
    var_title = StringVar(register_window)
    var_title.set(title_options[0])

    # Create options for the gender
    gender_options = ["Please select below", "-------------------", "Male", "Female", "Non-binary", "Other", "Prefer not to say"] # More can be added if necessary
    var_gender = StringVar(register_window)
    var_gender.set(gender_options[0])

    # Create a place to enter the title and gender
    frm_gender = Frame(master = register_window)
    frm_gender.pack()
    for i in range(2):
        for j in range(2):
            frm_gender_grid = Frame(master = frm_gender, relief = FLAT)
            frm_gender_grid.grid(row = i, column = j)
            if i == 0 and j == 0:
                lbl_title = Label(master = frm_gender_grid, text = "\nWhat is your title?", font = ("calibre", 11))
                lbl_title.pack(padx = 25)
            elif i == 0 and j == 1:
                lbl_gender = Label(master = frm_gender_grid, text = "\nWhat is your gender?", font = ("calibre", 11))
                lbl_gender.pack(padx = 25)
            elif i == 1 and j == 0:
                opt_title = OptionMenu(frm_gender_grid, var_title, *title_options)
                opt_title.config(width = 17)
                opt_title.pack(pady = 10, padx = 15)
            elif i == 1 and j == 1:
                opt_gender = OptionMenu(frm_gender_grid, var_gender, *gender_options)
                opt_gender.config(width = 17)
                opt_gender.pack(pady = 10, padx = 15)

    # Redirect continue button
    btn_continue.config(command = lambda:continue4())

flagged_gender = False # This keeps track of if the "invalid input" has appeared

def continue4():
    '''
    Here we will verify if the user's inputs are valid and continue to the 
    next step of registration
    '''
    global register_window
    global frm_continue
    global btn_continue
    global lbl_title 
    global var_title 
    global opt_title
    global lbl_gender 
    global var_gender
    global opt_gender 
    global lbl_invalid_choice
    global frm_gender 
    global frm_gender_grid 
    global flagged_gender
    global user_info
    
    title = var_title.get()
    gender = var_gender.get()

    invalid_options = ["Please select below", "-------------------"]
    
    if title in invalid_options or gender in invalid_options:
        if flagged_gender is False:
            flagged_gender = True
            lbl_invalid_choice = Label(master = register_window, text = "Invalid choice/s. Please select again.", font = 10, fg = "red")
            lbl_invalid_choice.pack()
        else:
            pass
    else:
        # Place the title and gender into the user info list
        user_info[4] = title
        user_info[5] = gender

        # Remove the gender and title options and prompts and invalid text
        lbl_title.forget()
        opt_title.forget()
        lbl_gender.forget()
        opt_gender.forget()
        frm_gender_grid.forget()
        frm_gender.forget()
        flagged_gender = False
        try:
            lbl_invalid_choice.forget()
        except Exception:
            pass

        phase5()

# The following modules need to be accessed by multiple functions regarding the users birthday
lbl_birthday = "placeholder"
var_date = "placeholder"
cmb_date = "placeholder"
var_month = "placeholder"
cmb_month = "placeholder"
var_year = "placeholder"
cmb_year = "placeholder"
lbl_invalid_date = "placeholder"
frm_date = "placeholder"
frm_date_grid = "placeholder"

def phase5():
    '''
    Now we will get the users bday
    '''

    global register_window
    global frm_continue
    global btn_continue
    global current_screen
    global lbl_birthday
    global var_date
    global cmb_date
    global var_month
    global cmb_month
    global var_year
    global cmb_year
    global lbl_invalid_date
    global frm_date
    global frm_date_grid 

    current_screen = 4

    # Create options for the date
    var_date = StringVar(register_window)
    date_options = ["Date", "------"] 
    for i in range(31):
        if i < 9:
            date_options.append('0' + str(i + 1))
        else:
            date_options.append(str(i + 1))
    var_date.set(date_options[0])

    # Create options for the month
    month_options = ["Month    ", "-----------", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    var_month = StringVar(register_window)
    var_month.set(month_options[0])

    # Create options for the year
    year_options = ["Year", "------"] 
    today = datetime.date.today()
    current_year = today.year
    for i in range(current_year, 1899, -1):
        year_options.append(str(i))
    var_year = StringVar(register_window)
    var_year.set(year_options[0])

    # Place the label
    lbl_birthday = Label(master = register_window, text = "\nWhen is your birthday?", font = ("calibre", 11))
    lbl_birthday.pack()

    # Create a place to enter the birthday
    frm_date = Frame(master = register_window)
    frm_date.pack()
    for i in range(3):
        frm_date_grid = Frame(master = frm_date, relief = FLAT)
        frm_date_grid.grid(row = 0, column = i)
        if i == 0:
            cmb_date = ttk.Combobox(frm_date_grid, width = 6, textvariable = var_date)
            cmb_date['values'] = tuple(date_options)
            cmb_date.grid(column = 1, row = 10)
            cmb_date.current()
            cmb_date.pack(pady = 10, padx = 12)
        elif i == 1:
            cmb_month = ttk.Combobox(frm_date_grid, width = 11, textvariable = var_month)
            cmb_month['values'] = tuple(month_options)
            cmb_month.grid(column = 1, row = 10)
            cmb_month.current()
            cmb_month.pack(pady = 10, padx = 12)
        elif i == 2:
            cmb_year = ttk.Combobox(frm_date_grid, width = 6, textvariable = var_year)
            cmb_year['values'] = tuple(year_options)
            cmb_year.grid(column = 1, row = 10)
            cmb_year.current()
            cmb_year.pack(pady = 10, padx = 12)

    # Redirect the continue button
    btn_continue.config(command = lambda:continue5())   
            
flagged_date = False # This keeps track of if the "invalid input" has appeared

def continue5():
    '''
    Here we will confirm if the date chosen is valid
    '''
    global register_window
    global lbl_birthday
    global var_date
    global cmb_date
    global var_month
    global cmb_month
    global var_year
    global cmb_year
    global lbl_invalid_date
    global frm_date
    global frm_date_grid 
    global user_info
    global flagged_date

    # Get the user inputs
    date = var_date.get()
    month = var_month.get()
    year = var_year.get()

    dict_months = {'January': '01',
                   'February': '02',
                   'March': '03',
                   'April': '04',
                   'May': '05',
                   'June': '06',
                   'July': '07',
                   'August': '08',
                   'September': '09',
                   'October': '10',
                   'November': '11',
                   'December': '12'}

    # Valid dates
    valid_dates = []
    for i in range(31):
        if i < 9:
            valid_dates.append('0' + str(i + 1))
        else:
            valid_dates.append(str(i + 1))
    # Valid months
    valid_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    # Valid years
    valid_years = []
    today = datetime.date.today()
    current_year = today.year
    for i in range(current_year, 1899, -1):
        valid_years.append(str(i))

    # If the user does not input a date
    if (date not in valid_dates) or (month not in valid_months) or (year not in valid_years):
        if flagged_date is False:
            flagged_date = True
            lbl_invalid_date = Label(master = register_window, text = "Invalid birthday. Please select again.", font = 10, fg = "red")
            lbl_invalid_date.pack()
        else:
            pass
        return

    # If the date does not correlate to a month correctly
    months_30 = ["April", "June", "September", "November"]
    if ((month in months_30) and (date == '31')) or ((month == "February") and (date in ["30", "31"])):
        if flagged_date is False:
            flagged_date = True
            lbl_invalid_date = Label(master = register_window, text = "Invalid birthday. Please select again.", font = 10, fg = "red")
            lbl_invalid_date.pack()
        else:
            pass
        return

    # If the dates dont correlate to a leap year
    if (month == "February" and date == "29"):
        if int(year) % 4 != 0:
            if flagged_date is False:
                flagged_date = True
                lbl_invalid_date = Label(master = register_window, text = "Invalid birthday. Please select again.", font = 10, fg = "red")
                lbl_invalid_date.pack()
            else:
                pass
            return
    
    # If the date is in the future
    future_flag = False
    if (int(year) == current_year):
        if int(dict_months[month]) > today.month:
            future_flag = True
        elif int(dict_months[month]) == today.month:
            if int(date) > today.day:
                future_flag = True
    
    if future_flag is True:
        if flagged_date is False:
                flagged_date = True
                lbl_invalid_date = Label(master = register_window, text = "Invalid birthday. Please select again.", font = 10, fg = "red")
                lbl_invalid_date.pack()
        else:
            pass
        return


    # Reformat the birthday and place it into user info list
    birthday = f'{year}-{dict_months[month]}-{date}'
    user_info[6] = birthday

    # Forget everything and move on to the next section
    lbl_birthday.forget()
    cmb_date.forget()
    cmb_month.forget()
    cmb_year.forget()
    frm_date.forget()
    frm_date_grid.forget()
    flagged_date = False
    try:
        lbl_invalid_date.forget()
    except Exception:
        pass

    phase6()

# The following modules need to be accessed by multiple functions regarding the users nationality
lbl_nationality = "placeholder"
cmb_nationality = "placeholder"
lbl_invalid_nationality = "placeholder"
var_nationality = "placeholder"

def phase6():
    '''
    Now we will get the users nationality
    '''
    global register_window
    global frm_continue
    global btn_continue
    global current_screen
    global lbl_nationality
    global cmb_nationality
    global var_nationality
    
    current_screen = 5

    # Tuple of nationalities
    NATIONALITIES_tuple = ('Nationalities', '--------------------', 'Afghan', 'Albanian', 'Algerian', 'American', 'Andorran', 'Angolan', 'Antiguans', 'Argentinean', 'Armenian', 'Australian', 'Austrian', 'Azerbaijani', 'Bahamian', 'Bahraini', 'Bangladeshi', 'Barbadian', 'Barbudans', 'Batswana', 'Belarusian', 'Belgian', 'Belizean', 'Beninese', 'Bhutanese', 'Bolivian', 'Bosnian', 'Brazilian', 'British', 'Bruneian', 'Bulgarian', 'Burkinabe', 'Burmese', 'Burundian', 'Cambodian', 'Cameroonian', 'Canadian', 'Cape Verdean', 'Central African', 'Chadian', 'Chilean', 'Chinese', 'Colombian', 'Comoran',  'Congolese', 'Costa Rican', 'Croatian', 'Cuban', 'Cypriot', 'Czech', 'Danish', 'Djibouti', 'Dominican', 'Dutch', 'Dutchman', 'Dutchwoman', 'East Timorese', 'Ecuadorean', 'Egyptian', 'Emirian', 'Equatorial Guinean', 'Eritrean', 'Estonian', 'Ethiopian', 'Fijian', 'Filipino', 'Finnish', 'French', 'Gabonese', 'Gambian', 'Georgian', 'German', 'Ghanaian', 'Greek', 'Grenadian', 'Guatemalan', 'Guinea-Bissauan', 'Guinean', 'Guyanese', 'Haitian', 'Herzegovinian', 'Honduran', 'Hungarian', 'I-Kiribati', 'Icelander', 'Indian', 'Indonesian', 'Iranian', 'Iraqi', 'Irish', 'Israeli', 'Italian', 'Ivorian', 'Jamaican', 'Japanese', 'Jordanian', 'Kazakhstani', 'Kenyan', 'Kittian and Nevisian', 'Kuwaiti', 'Kyrgyz', 'Laotian', 'Latvian', 'Lebanese', 'Liberian', 'Libyan', 'Liechtensteiner', 'Lithuanian', 'Luxembourger', 'Macedonian', 'Malagasy', 'Malawian', 'Malaysian', 'Maldivan', 'Malian', 'Maltese', 'Marshallese', 'Mauritanian', 'Mauritian', 'Mexican', 'Micronesian', 'Moldovan', 'Monacan', 'Mongolian', 'Moroccan', 'Mosotho', 'Motswana', 'Mozambican', 'Namibian', 'Nauruan', 'Nepalese', 'Netherlander', 'New Zealander', 'Ni-Vanuatu', 'Nicaraguan', 'Nigerian', 'Nigerien', 'North Korean', 'Northern Irish', 'Norwegian', 'Omani', 'Pakistani', 'Palauan', 'Panamanian', 'Papua New Guinean', 'Paraguayan', 'Peruvian', 'Polish', 'Portuguese', 'Qatari', 'Romanian', 'Russian', 'Rwandan', 'Saint Lucian', 'Salvadoran', 'Samoan', 'San Marinese', 'Sao Tomean', 'Saudi', 'Scottish', 'Senegalese', 'Serbian', 'Seychellois', 'Sierra Leonean', 'Singaporean', 'Slovakian', 'Slovenian', 'Solomon Islander', 'Somali', 'South African', 'South Korean', 'Spanish', 'Sri Lankan', 'Sudanese', 'Surinamer', 'Swazi', 'Swedish', 'Swiss', 'Syrian', 'Taiwanese', 'Tajik', 'Tanzanian', 'Thai', 'Togolese', 'Tongan', 'Trinidadian or Tobagonian', 'Tunisian', 'Turkish', 'Tuvaluan', 'Ugandan', 'Ukrainian', 'Uruguayan', 'Uzbekistani', 'Venezuelan', 'Vietnamese', 'Welsh', 'Yemenite', 'Zambian', 'Zimbabwean')
    var_nationality = StringVar(register_window)
    var_nationality.set(NATIONALITIES_tuple[0])

    # Now create a place to input the nationalities
    lbl_nationality = Label(master = register_window, text = "\nWhat is your nationality?", font = ("calibre", 11))
    lbl_nationality.pack()
    cmb_nationality = ttk.Combobox(register_window, width = 20, textvariable = var_nationality)
    cmb_nationality['values'] = NATIONALITIES_tuple
    cmb_nationality.current()
    cmb_nationality.pack(pady = 10)

    # Redirect continue button
    btn_continue.config(command = lambda:continue6())   

flagged_nationality = False # This keeps track of if the "invalid input" has appeared

def continue6():
    '''
    Check validity of nationality
    '''
    global register_window
    global lbl_nationality
    global cmb_nationality
    global lbl_invalid_nationality
    global user_info
    global flagged_nationality
    global var_nationality

    nationality = var_nationality.get()

    NATIONALITIES_tuple2 = ('Afghan', 'Albanian', 'Algerian', 'American', 'Andorran', 'Angolan', 'Antiguans', 'Argentinean', 'Armenian', 'Australian', 'Austrian', 'Azerbaijani', 'Bahamian', 'Bahraini', 'Bangladeshi', 'Barbadian', 'Barbudans', 'Batswana', 'Belarusian', 'Belgian', 'Belizean', 'Beninese', 'Bhutanese', 'Bolivian', 'Bosnian', 'Brazilian', 'British', 'Bruneian', 'Bulgarian', 'Burkinabe', 'Burmese', 'Burundian', 'Cambodian', 'Cameroonian', 'Canadian', 'Cape Verdean', 'Central African', 'Chadian', 'Chilean', 'Chinese', 'Colombian', 'Comoran',  'Congolese', 'Costa Rican', 'Croatian', 'Cuban', 'Cypriot', 'Czech', 'Danish', 'Djibouti', 'Dominican', 'Dutch', 'Dutchman', 'Dutchwoman', 'East Timorese', 'Ecuadorean', 'Egyptian', 'Emirian', 'Equatorial Guinean', 'Eritrean', 'Estonian', 'Ethiopian', 'Fijian', 'Filipino', 'Finnish', 'French', 'Gabonese', 'Gambian', 'Georgian', 'German', 'Ghanaian', 'Greek', 'Grenadian', 'Guatemalan', 'Guinea-Bissauan', 'Guinean', 'Guyanese', 'Haitian', 'Herzegovinian', 'Honduran', 'Hungarian', 'I-Kiribati', 'Icelander', 'Indian', 'Indonesian', 'Iranian', 'Iraqi', 'Irish', 'Israeli', 'Italian', 'Ivorian', 'Jamaican', 'Japanese', 'Jordanian', 'Kazakhstani', 'Kenyan', 'Kittian and Nevisian', 'Kuwaiti', 'Kyrgyz', 'Laotian', 'Latvian', 'Lebanese', 'Liberian', 'Libyan', 'Liechtensteiner', 'Lithuanian', 'Luxembourger', 'Macedonian', 'Malagasy', 'Malawian', 'Malaysian', 'Maldivan', 'Malian', 'Maltese', 'Marshallese', 'Mauritanian', 'Mauritian', 'Mexican', 'Micronesian', 'Moldovan', 'Monacan', 'Mongolian', 'Moroccan', 'Mosotho', 'Motswana', 'Mozambican', 'Namibian', 'Nauruan', 'Nepalese', 'Netherlander', 'New Zealander', 'Ni-Vanuatu', 'Nicaraguan', 'Nigerian', 'Nigerien', 'North Korean', 'Northern Irish', 'Norwegian', 'Omani', 'Pakistani', 'Palauan', 'Panamanian', 'Papua New Guinean', 'Paraguayan', 'Peruvian', 'Polish', 'Portuguese', 'Qatari', 'Romanian', 'Russian', 'Rwandan', 'Saint Lucian', 'Salvadoran', 'Samoan', 'San Marinese', 'Sao Tomean', 'Saudi', 'Scottish', 'Senegalese', 'Serbian', 'Seychellois', 'Sierra Leonean', 'Singaporean', 'Slovakian', 'Slovenian', 'Solomon Islander', 'Somali', 'South African', 'South Korean', 'Spanish', 'Sri Lankan', 'Sudanese', 'Surinamer', 'Swazi', 'Swedish', 'Swiss', 'Syrian', 'Taiwanese', 'Tajik', 'Tanzanian', 'Thai', 'Togolese', 'Tongan', 'Trinidadian or Tobagonian', 'Tunisian', 'Turkish', 'Tuvaluan', 'Ugandan', 'Ukrainian', 'Uruguayan', 'Uzbekistani', 'Venezuelan', 'Vietnamese', 'Welsh', 'Yemenite', 'Zambian', 'Zimbabwean')
    if nationality not in NATIONALITIES_tuple2:
        if flagged_nationality is False:
                flagged_nationality = True
                lbl_invalid_nationality = Label(master = register_window, text = "Invalid nationality. Please choose again.", font = 10, fg = "red")
                lbl_invalid_nationality.pack()
        else:
            pass
        return
    
    # Place nationality into user info tuple
    user_info[7] = nationality

    # Clean up the screen
    lbl_nationality.forget()
    cmb_nationality.forget()
    flagged_nationality = False
    try:
        lbl_invalid_nationality.forget()
    except Exception:
        pass

    phase7()

# The following modules need to be accessed by multiple functions regarding the users password
lbl_password = "placeholder"
ent_password = "placeholder"
lbl_confirm = "placeholder"
ent_confirm = "placeholder"
frm_password = "placeholder"
frm_password_grid = "placeholder"
btn_show = "placeholder"
lbl_invalid_password = "placeholder"

def phase7():
    '''
    Now we will get a password for the user's account. The password
    is completely optional. A user does not need a password
    '''
    global register_window
    global lbl_password
    global ent_password
    global lbl_confirm
    global ent_confirm
    global frm_continue
    global btn_continue
    global current_screen
    global frm_password
    global frm_password_grid
    global btn_show

    current_screen = 6

    # Create a place to enter the password and password confirmation
    frm_password = Frame(master = register_window)
    frm_password.pack()
    for i in range(2):
        for j in range(3):
            frm_password_grid = Frame(master = frm_password, relief = FLAT)
            frm_password_grid.grid(row = i, column = j)
            if i == 0 and j == 0:
                lbl_password = Label(master = frm_password_grid, text = "\nChoose a password:", font = ("calibre", 11))
                lbl_password.pack()
            elif i == 0 and j == 1:
                lbl_confirm = Label(master = frm_password_grid, text = "\nConfirm your password:", font = ("calibre", 11))
                lbl_confirm.pack()
            elif i == 1 and j == 0:
                ent_password = Entry(master = frm_password_grid, width = 40, show = '*')
                ent_password.pack(pady = 10, padx = 15)
            elif i == 1 and j == 1:
                ent_confirm = Entry(master = frm_password_grid, width = 40, show = '*')
                ent_confirm.pack(pady = 10, padx = 15)
            elif i == 1 and j == 2:
                btn_show = Button(master = frm_password_grid, text = "Show", font = ("calibre", 11),
                                  fg = "black", command = lambda:show_password())
                btn_show.pack()
            else:
                pass

    # Redirect continue button
    btn_continue.config(command = lambda:continue7())

hidden = False # This is used to track if the password is currently hidden or not

def show_password():
    '''
    This function reveals the password that the user has inputted
    '''
    global ent_confirm
    global ent_password
    global btn_show
    global hidden

    if hidden is False:
        ent_confirm.config(show = '')
        ent_password.config(show = '')
        btn_show.config(text = "Hide")
        hidden = True
    elif hidden is True:
        ent_confirm.config(show = '*')
        ent_password.config(show = '*')
        btn_show.config(text = "Show")
        hidden = False

flagged_password = False # This keeps track of if the "invalid input" has appeared

def continue7():
    '''
    Here we will verify if the password matches the confirmation
    '''
    global register_window
    global lbl_password
    global ent_password
    global lbl_confirm
    global ent_confirm
    global frm_password
    global frm_password_grid
    global btn_show
    global lbl_invalid_password
    global user_info
    global flagged_password

    password = ent_password.get()
    confirm = ent_confirm.get()

    # If the password does not match the confirmation, it is invalid
    if password != confirm:
        if flagged_password is False:
            flagged_password = True
            lbl_invalid_password = Label(master = register_window, text = "Password does not match.", font = 10, fg = "red")
            lbl_invalid_password.pack()
        else:
            pass
        return
    
    # Place the password into the user info list
    user_info[8] = password

    # Now clean up the screen
    lbl_password.forget()
    ent_password.forget()
    lbl_confirm.forget()
    ent_confirm.forget()
    frm_password.forget()
    frm_password_grid.forget()
    btn_show.forget()
    try:
        lbl_invalid_password.forget()
    except Exception:
        pass

    phase8()

# The following modules need to be accessed by multiple functions regarding the username
lbl_username = "placeholder"
ent_username = "placeholder"
lbl_invalid_username = "placeholder"

def phase8():
    '''
    The user can now pick a username
    '''
    global register_window
    global lbl_username
    global ent_username
    global current_screen
    global frm_continue
    global btn_continue

    current_screen = 7

    # Create a place to enter the username
    lbl_username = Label(master = register_window, text = "\nPlease choose a username:", font = 10)
    lbl_username.pack()
    ent_username = Entry(master = register_window, width = 40)
    ent_username.pack(pady = 10)

    # Redirect the continue button
    btn_continue.config(command = lambda:continue8())   
    
flagged_username = False # This keeps track of if the "invalid input" has appeared

def continue8():
    '''
    Now we will check if this username is already taken
    '''
    global register_window
    global ent_username
    global lbl_username
    global flagged_username
    global lbl_invalid_username
    global user_info

    # Get the username from the entry
    username = ent_username.get()

    # Either it is left empty or it is too long
    if username == '' or len(username) > 20:
        if flagged_username is False:
            flagged_username = True
            lbl_invalid_username = Label(master = register_window, text = "Invalid username. Try again.", font = 10, fg = "red")
            lbl_invalid_username.pack()
            return
        else:
            lbl_invalid_username.config(text = "Invalid username. Try again.")
            return
    else:
        # Now check if the username already exists
        decrypt('Login and registration/users.csv')
        csv_file = open('Login and registration/users.csv')
        for line in csv.reader(csv_file):
            if line[8] == username:
                if flagged_username is True:
                    lbl_invalid_username.config(text = "This username already exists.")
                else:
                    flagged_username = True
                    lbl_invalid_username = Label(master = register_window, text = "This username already exists.", font = 10, fg = "red")
                    lbl_invalid_username.pack()
                # Encrypt it again
                generate_key()
                encrypt('Login and registration/users.csv')
                csv_file.close()
                return
            else:
                continue

        # Encrypt it again
        generate_key()
        encrypt('Login and registration/users.csv')
        csv_file.close()

    # Remove the username entry and prompt and invalid text
    lbl_username.forget()
    ent_username.forget()
    flagged_username = False
    try:
        lbl_invalid_username.forget()
    except Exception:
        pass
        
    # Place phone into the users info list
    user_info[9] = username

    phase9()

# The following modules need to be accessed by multiple functions regarding the avatar
lbl_avatar = "placeholder"
lbl_pfp = "placeholder"
btn_upload = "placeholder"
chosen_image = "placeholder"
frm_avatar = "placeholder"
frm_avatar_grid = "placeholder"

def phase9():
    '''
    The user can now choose to upload a profile picture
    '''
    global register_window
    global lbl_avatar
    global lbl_pfp
    global btn_upload
    global current_screen
    global frm_continue
    global btn_continue
    global frm_avatar
    global frm_avatar_grid

    current_screen = 8

    # Make a default profile picture based on gender
    if user_info[5] == "Male":
        profile_image = Image.open('Male.png')
    elif user_info[5] == "Female":
        profile_image = Image.open('Female.png')
    else:
        profile_image = Image.open('other.png')
    image_name = profile_image.filename

    # Place it into userinfo list for now
    profile_image = profile_image.resize((1000, 1000))
    profile_image.save(f'{image_name}')
    user_info[10] = image_name

    # Now time to place everything on the screen 
    frm_avatar = Frame(master = register_window, relief = FLAT)
    frm_avatar.pack()
    frm_avatar_grid = Frame(master = frm_avatar, relief = FLAT)
    frm_avatar_grid.grid(row = 0, column = 0)
    lbl_avatar = Label(master = frm_avatar_grid, text = "\nPlease choose a profile picture:", font = 10)
    lbl_avatar.pack(pady = 10, padx = 20)
    frm_avatar_grid = Frame(master = frm_avatar, relief = FLAT)
    frm_avatar_grid.grid(row = 1, column = 0)
    btn_upload = Button(master = frm_avatar_grid, text = "Choose image", font = ("calibre", 11),
                        fg = "black", command = lambda:upload_file())
    btn_upload.pack(pady = 10, padx = 20)
    frm_avatar_grid = Frame(master = frm_avatar, relief = FLAT)
    frm_avatar_grid.grid(row = 0, column = 1, rowspan = 2)
    profile_image = profile_image.resize((125, 125))
    profile_image = ImageTk.PhotoImage(profile_image)
    lbl_pfp = Label(master = frm_avatar_grid, image = profile_image, bg = register_window.cget('bg'))
    lbl_pfp.image = profile_image
    lbl_pfp.pack(padx = 20)

    # Redirect continue button
    btn_continue.config(command = lambda:continue9())  

def upload_file():
    '''
    Here the user can choose a picture from their system to use as their 
    profile picture
    '''
    global user_info
    global lbl_pfp

    # Open the user's files
    f_types = [('Png Files','*.png'), ('Jpg Files', '*.jpg')]   # type of files to select 
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(file=filename)

    # Place it into user info list
    img = ImageTk.getimage(img)
    img = img.resize((1000, 1000))
    img.save(f'{filename}')
    user_info[10] = filename
    
    # Now display it
    img = img.resize((125, 125))
    img = ImageTk.PhotoImage(img)
    lbl_pfp.config(image = img)
    lbl_pfp.image = img

def continue9():
    '''
    Here we will clear up the screen
    '''
    global lbl_avatar
    global lbl_pfp
    global btn_upload
    global frm_avatar
    global frm_avatar_grid

    lbl_avatar.forget()
    lbl_pfp.forget()
    btn_upload.forget()
    frm_avatar.forget()
    frm_avatar_grid.forget()

    phase10()

# The following modules need to be accessed by multiple functions regarding the avatar
lbl_final = "placeholder"
btn_final = "placeholder"

def phase10():
    '''
    We will now confirm that all the user's details are correct
    '''

    global register_window
    global lbl_final
    global btn_final
    global current_screen
    global frm_continue
    global btn_continue

    current_screen = 9

    # Place everything necessary on the screen
    lbl_final = Label(master = register_window, text = "\nAre all your details correct?", font = 10)
    lbl_final.pack()
    btn_final =  Button(master = register_window, text = "View details", font = ("calibre", 11),
                        fg = "black", command = lambda:view_details())
    btn_final.pack(pady = 10)

    # Change the continue button
    btn_continue.config(text = "Submit", command = lambda:continue10())

def view_details():
    '''
    Here the user can see all their details
    '''
    # Create instance of tkinter window and the labels found on the window (title, etc.)
    details_window = Toplevel()
    details_window.geometry("800x600")
    details_window.title("Details")
    details_window.resizable(False,False)

    # Now insert logo and company name (in this example, I will use my own placeholder
    # but these can be changed)
    frm_details_logo = Frame(master = details_window)
    frm_details_logo.pack(pady = 15)
    img_details_logo = Image.open('logo task organiser.png') # This logo can be changed
    img_details_logo = img_details_logo.resize((150, 150))
    img_details_logo = ImageTk.PhotoImage(img_details_logo)
    for i in range(2):
        frm_details_logo_grid = Frame(master = frm_details_logo)
        frm_details_logo_grid.grid(row = 0, column = i, padx = 10)
        if i == 0:
            lbl_details_logo = Label(master = frm_details_logo_grid, image = img_details_logo)
            lbl_details_logo.pack()
            lbl_details_logo.image = img_details_logo
        else:
            # The following title label can be changed
            lbl_details_logo_text = Label(master = frm_details_logo_grid, text = "GROTANIX Task Organiser",
                                font = ("calibre", 25, "bold"), fg = "#538c50")
            lbl_details_logo_text.pack()
            lbl_details = Label(master = frm_details_logo_grid, text = "User Details",
                                font = ("calibre", 20, "bold"), fg = "#264124")
            lbl_details.pack()

    # Now time to place in all the user details
    template = ["                                        Email                                        ", 
                "                                        Phone Number                                 ", 
                "                                        Firstname                                    ", 
                "                                        Surname                                      ", 
                "                                        Title                                        ", 
                "                                        Gender                                       ", 
                "                                        Birthday (YYYY/MM/DD)                        ", 
                "                                        Nationality                                  ", 
                "                                        Password                                     ", 
                "                                        Username                                     ", 
                "                                        Profile Photo                                "]
    for i in range(len(user_info)):
        if i % 2 == 0:
            frm_master = Frame(master = details_window)
            frm_master.pack(fill = X, pady = 5)
            frm_sub_grid = Frame(master = frm_master)
            frm_sub_grid.grid(row = i, column = 0)
            lbl_template = Label(master = frm_sub_grid, text = template[i], font = 10)
            lbl_template.pack()
            frm_sub_grid = Frame(master = frm_master)
            frm_sub_grid.grid(row = i, column = 1)
            lbl_info = Label(master = frm_sub_grid, text = user_info[i], font = 10)
            lbl_info.pack()
        else:
            frm_master = Frame(master = details_window, bg = 'light grey')
            frm_master.pack(fill = X, pady = 5)
            frm_sub_grid = Frame(master = frm_master)
            frm_sub_grid.grid(row = i, column = 0)
            lbl_template = Label(master = frm_sub_grid, text = template[i], font = 10, bg = 'light grey')
            lbl_template.pack()
            frm_sub_grid = Frame(master = frm_master)
            frm_sub_grid.grid(row = i, column = 1)
            lbl_info = Label(master = frm_sub_grid, text = user_info[i], font = 10, bg = 'light grey')
            lbl_info.pack()

    # Add an exit button at the bottom
    frm_exit_final = Frame(master = details_window, relief = RAISED, borderwidth = 5)
    frm_exit_final.pack()
    btn_exit_final = Button(master = frm_exit_final, text = "Done", command = lambda:details_window.destroy(),
                            font = ("calibre", 11), fg = "black",)
    btn_exit_final.pack()

def continue10():
    '''
    This is where the user submits their registration form
    '''
    global lbl_final
    global btn_final
    global frm_continue
    global btn_continue
    global frm_back
    global btn_back

    # Clean things up
    lbl_final.forget()
    btn_final.forget()

    lbl_finished = Label(master = register_window, text = "\nThank you for registering!\nYou can now sign in using your account.",
                         font = ("calibre", 20), fg = "#538c50")
    lbl_finished.pack()

    # Redirect the continue button
    btn_continue.config(text = "Close", command = lambda: register_window.destroy())

    # Remove previous button
    btn_back.forget()
    frm_back.forget()

    # Put the user's detail into the csv
    decrypt("Login and registration/users.csv")
    user_csv = open(r"Login and registration/users.csv", "a", newline = '')
    writer = csv.writer(user_csv)
    writer.writerow(user_info)
    user_csv.close()
    generate_key()
    encrypt("Login and registration/users.csv")

    return

login_window.mainloop()