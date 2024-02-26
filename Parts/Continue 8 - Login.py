flagged_username = False # This keeps track of if the "invalid input" has appeared

def continue8():
    '''
    Now we will check if this username is already taken
    '''
    global register_window
    global ent_username
    global lbl_username
    global flagged_username
    global lbl_invalid_username
    global user_info

    # Get the username from the entry
    username = ent_username.get()

    # Either it is left empty or it is too long
    if username == '' or len(username) > 20:
        if flagged_username is False:
            flagged_username = True
            lbl_invalid_username = Label(master = register_window, text = "Invalid username. Try again.", font = 10, fg = "red")
            lbl_invalid_username.pack()
            return
        else:
            lbl_invalid_username.config(text = "Invalid username. Try again.")
            return
    else:
        # Now check if the username already exists
        decrypt('Login and registration/users.csv')
        csv_file = open('Login and registration/users.csv')
        for line in csv.reader(csv_file):
            if line[8] == username:
                if flagged_username is True:
                    lbl_invalid_username.config(text = "This username already exists.")
                else:
                    flagged_username = True
                    lbl_invalid_username = Label(master = register_window, text = "This username already exists.", font = 10, fg = "red")
                    lbl_invalid_username.pack()
                # Encrypt it again
                generate_key()
                encrypt('Login and registration/users.csv')
                csv_file.close()
                return
            else:
                continue

        # Encrypt it again
        generate_key()
        encrypt('Login and registration/users.csv')
        csv_file.close()

    # Remove the username entry and prompt and invalid text
    lbl_username.forget()
    ent_username.forget()
    flagged_username = False
    try:
        lbl_invalid_username.forget()
    except Exception:
        pass
        
    # Place phone into the users info list
    user_info[9] = username

    phase9()