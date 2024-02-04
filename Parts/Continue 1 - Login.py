flagged_email = False # This keeps track of if the "invalid email address" has appeared

def continue1():
    '''
    Here we will verify if the email inputted is valid and continue to
    the next step of registration
    '''
    global register_window
    global ent_email
    global lbl_email
    global flagged_email
    global lbl_invalid_email
    global frm_back
    global btn_back
    global user_info

    # Get the email from the entry
    email = ent_email.get()

    # Email must contain @ symbol and .com. The minimum length for an email is also 7 characters
    # This will also check if the entry has been left blank
    if (".com" not in email) or ('@' not in email) or (len(email) < 7) or (' ' in email):
        if flagged_email is False:
            flagged_email = True
            lbl_invalid_email = Label(master = register_window, text = "Invalid email address. Try again.", font = 10, fg = "red")
            lbl_invalid_email.pack()
        else:
            lbl_invalid_email.config(text = "Invalid email address. Try again.")
    else:
        # Now check if the email already exists
        decrypt('Login and registration/users.csv')
        csv_file = open('Login and registration/users.csv')
        for line in csv.reader(csv_file):
            if line[0] == email:
                if flagged_email is True:
                    lbl_invalid_email.config(text = "This email address already exists.")
                else:
                    flagged_email = True
                    lbl_invalid_email = Label(master = register_window, text = "This email address already exists.", font = 10, fg = "red")
                    lbl_invalid_email.pack()
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

        # Remove the email entry and prompt and invalid text
        lbl_email.forget()
        ent_email.forget()
        flagged_email = False
        try:
            lbl_invalid_email.forget()
        except Exception:
            pass
        
        # Place email into the users info list
        user_info[0] = email

        # Add a back button
        frm_back = Frame(master = register_window)
        frm_back.pack(fill = X)
        btn_back = Button(master = frm_back, text = "             ↩ Previous", font = 10, borderwidth = 0, fg = "#264124",
                          command = lambda:previous())
        btn_back.pack(side = LEFT)

        phase2()