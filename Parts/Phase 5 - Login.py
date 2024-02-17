# The following modules need to be accessed by multiple functions regarding the users birthday
lbl_birthday = "placeholder"
var_date = "placeholder"
cmb_date = "placeholder"
var_month = "placeholder"
cmb_month = "placeholder"
var_year = "placeholder"
cmb_year = "placeholder"
lbl_invalid_date = "placeholder"
frm_date = "placeholder"
frm_date_grid = "placeholder"

def phase5():
    '''
    Now we will get the users bday
    '''

    global register_window
    global frm_continue
    global btn_continue
    global current_screen
    global lbl_birthday
    global var_date
    global cmb_date
    global var_month
    global cmb_month
    global var_year
    global cmb_year
    global lbl_invalid_date
    global frm_date
    global frm_date_grid 

    current_screen = 4

    # Create options for the date
    var_date = StringVar(register_window)
    date_options = ["Date", "------"] 
    for i in range(31):
        if i < 9:
            date_options.append('0' + str(i + 1))
        else:
            date_options.append(str(i + 1))
    var_date.set(date_options[0])

    # Create options for the month
    month_options = ["Month    ", "-----------", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    var_month = StringVar(register_window)
    var_month.set(month_options[0])

    # Create options for the year
    year_options = ["Year", "------"] 
    today = datetime.date.today()
    current_year = today.year
    for i in range(current_year, 1899, -1):
        year_options.append(str(i))
    var_year = StringVar(register_window)
    var_year.set(year_options[0])

    # Place the label
    lbl_birthday = Label(master = register_window, text = "\nWhen is your birthday?", font = ("calibre", 11))
    lbl_birthday.pack()

    # Create a place to enter the birthday
    frm_date = Frame(master = register_window)
    frm_date.pack()
    for i in range(3):
        frm_date_grid = Frame(master = frm_date, relief = FLAT)
        frm_date_grid.grid(row = 0, column = i)
        if i == 0:
            cmb_date = ttk.Combobox(frm_date_grid, width = 6, textvariable = var_date)
            cmb_date['values'] = tuple(date_options)
            cmb_date.grid(column = 1, row = 10)
            cmb_date.current()
            cmb_date.pack(pady = 10, padx = 12)
        elif i == 1:
            cmb_month = ttk.Combobox(frm_date_grid, width = 11, textvariable = var_month)
            cmb_month['values'] = tuple(month_options)
            cmb_month.grid(column = 1, row = 10)
            cmb_month.current()
            cmb_month.pack(pady = 10, padx = 12)
        elif i == 2:
            cmb_year = ttk.Combobox(frm_date_grid, width = 6, textvariable = var_year)
            cmb_year['values'] = tuple(year_options)
            cmb_year.grid(column = 1, row = 10)
            cmb_year.current()
            cmb_year.pack(pady = 10, padx = 12)

    # Redirect the continue button
    btn_continue.config(command = lambda:continue5())   
