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