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