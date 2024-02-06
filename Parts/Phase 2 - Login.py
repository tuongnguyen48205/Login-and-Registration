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