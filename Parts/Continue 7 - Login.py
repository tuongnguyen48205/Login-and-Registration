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