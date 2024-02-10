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
