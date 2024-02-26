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