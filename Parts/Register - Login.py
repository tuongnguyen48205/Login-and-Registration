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