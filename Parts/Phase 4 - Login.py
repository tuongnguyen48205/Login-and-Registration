# The following modules need to be accessed by multiple functions regarding the users gender
var_title = "placeholder"
opt_title = "placeholder"
lbl_gender = "placeholder"
var_gender = "placeholder"
opt_gender = "placeholder"
lbl_invalid_choice = "placeholder"
frm_gender = "placeholder"
frm_gender_grid = "placeholder"

def phase4():
    '''
    This will get the users title and gender
    '''
    global register_window
    global frm_continue
    global btn_continue
    global current_screen
    global lbl_title 
    global var_title 
    global opt_title
    global lbl_gender 
    global var_gender
    global opt_gender 
    global lbl_invalid_choice
    global frm_gender 
    global frm_gender_grid 

    current_screen = 3

    # Create options for the title
    title_options = ["Please select below", "-------------------", "Mr", "Mrs", "Ms", "Miss", "Dr", "Other", "Prefer not to say"] # More can be added if necessary
    var_title = StringVar(register_window)
    var_title.set(title_options[0])

    # Create options for the gender
    gender_options = ["Please select below", "-------------------", "Male", "Female", "Non-binary", "Other", "Prefer not to say"] # More can be added if necessary
    var_gender = StringVar(register_window)
    var_gender.set(gender_options[0])

    # Create a place to enter the title and gender
    frm_gender = Frame(master = register_window)
    frm_gender.pack()
    for i in range(2):
        for j in range(2):
            frm_gender_grid = Frame(master = frm_gender, relief = FLAT)
            frm_gender_grid.grid(row = i, column = j)
            if i == 0 and j == 0:
                lbl_title = Label(master = frm_gender_grid, text = "\nWhat is your title?", font = ("calibre", 11))
                lbl_title.pack(padx = 25)
            elif i == 0 and j == 1:
                lbl_gender = Label(master = frm_gender_grid, text = "\nWhat is your gender?", font = ("calibre", 11))
                lbl_gender.pack(padx = 25)
            elif i == 1 and j == 0:
                opt_title = OptionMenu(frm_gender_grid, var_title, *title_options)
                opt_title.config(width = 17)
                opt_title.pack(pady = 10, padx = 15)
            elif i == 1 and j == 1:
                opt_gender = OptionMenu(frm_gender_grid, var_gender, *gender_options)
                opt_gender.config(width = 17)
                opt_gender.pack(pady = 10, padx = 15)

    # Redirect continue button
    btn_continue.config(command = lambda:continue4())

flagged_gender = False # This keeps track of if the "invalid input" has appeared