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