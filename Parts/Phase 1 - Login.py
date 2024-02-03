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