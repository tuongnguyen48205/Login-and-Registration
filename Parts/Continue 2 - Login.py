def continue2():
    '''
    Here we will verify if the phone number inputted is valid and continue to
    the next step of registration
    '''
    global register_window
    global ent_phone
    global lbl_phone
    global flagged_phone
    global lbl_invalid_phone
    global user_info

    # Get the phone number from the entry
    phone = ent_phone.get()

    # Either it is left empty or the phone number must be a digit
    if phone == '':
        pass
    elif phone.isdigit() is False or len(phone) > 20:
        if flagged_phone is False:
            flagged_phone = True
            lbl_invalid_phone = Label(master = register_window, text = "Invalid phone number. Try again.", font = 10, fg = "red")
            lbl_invalid_phone.pack()
            return
        else:
            lbl_invalid_phone.config(text = "Invalid phone number. Try again.")
            return
    else:
        # Now check if the number already exists
        decrypt('Login and registration/users.csv')
        csv_file = open('Login and registration/users.csv')
        for line in csv.reader(csv_file):
            if line[1] == phone:
                if flagged_phone is True:
                    lbl_invalid_phone.config(text = "This phone number already exists.")
                else:
                    flagged_phone = True
                    lbl_invalid_phone = Label(master = register_window, text = "This phone number already exists.", font = 10, fg = "red")
                    lbl_invalid_phone.pack()
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

    # Remove the phone entry and prompt and invalid text
    lbl_phone.forget()
    ent_phone.forget()
    flagged_phone = False
    try:
        lbl_invalid_phone.forget()
    except Exception:
        pass
        
    # Place phone into the users info list
    user_info[1] = phone

    phase3()