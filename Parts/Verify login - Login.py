def verify_login():
    '''
    This function verifies that the password the user inputted matches their username/email.
    If it does, the user will be granted access
    '''
    global ent_username
    global ent_password
    global lbl_invalid
    global invalid_login_flag

    # First check if the username/email entry is blank
    username = ent_username_login.get()
    password = ent_password_login.get()

    if username == '':
        if invalid_login_flag is False:
            invalid_login_flag = True
            lbl_invalid.config(fg = "red")
        return

    # Now decrypt the csv file and open it
    decrypt("Login and registration/users.csv")
    user_csv = open("Login and registration/users.csv")

    # First check if the username/email string contains the '@' symbol. If it does, it
    # means that the user has entered their email and if it does not, it means that the user
    # has entered their username. This is used to determine which part of the csv needs to 
    # be checked
    logged_in = False # A flag used to check if the user has logged in or not
    account = 'placeholder'

    for line in csv.reader(user_csv):
        # Skip the first line
        if line[0] == "email":
            pass
        elif username == line[0] or username == line[9]:
            # Check if the password matches, the user may login
            if password == line[8]:
                logged_in = True
                account = line
                break
            else:
                continue

    # If the user inputs do not exist, raise invalid text
    if logged_in is False:
        if invalid_login_flag is False:
            invalid_login_flag = True
            lbl_invalid.config(fg = "red")
        # Reencrypt the csv file
        generate_key()
        encrypt("Login and registration/users.csv")
        user_csv.close()
        return

    # Always encrypt the csv file after. Generate a new key every time for security and so the key
    # can't be copied
    generate_key()
    encrypt("Login and registration/users.csv")
    user_csv.close()

    # The user is granted access
    access_granted(account)