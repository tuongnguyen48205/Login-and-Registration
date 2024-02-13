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