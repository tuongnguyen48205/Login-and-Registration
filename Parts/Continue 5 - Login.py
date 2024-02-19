flagged_date = False # This keeps track of if the "invalid input" has appeared

def continue5():
    '''
    Here we will confirm if the date chosen is valid
    '''
    global register_window
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
    global user_info
    global flagged_date

    # Get the user inputs
    date = var_date.get()
    month = var_month.get()
    year = var_year.get()

    dict_months = {'January': '01',
                   'February': '02',
                   'March': '03',
                   'April': '04',
                   'May': '05',
                   'June': '06',
                   'July': '07',
                   'August': '08',
                   'September': '09',
                   'October': '10',
                   'November': '11',
                   'December': '12'}

    # Valid dates
    valid_dates = []
    for i in range(31):
        if i < 9:
            valid_dates.append('0' + str(i + 1))
        else:
            valid_dates.append(str(i + 1))
    # Valid months
    valid_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    # Valid years
    valid_years = []
    today = datetime.date.today()
    current_year = today.year
    for i in range(current_year, 1899, -1):
        valid_years.append(str(i))

    # If the user does not input a date
    if (date not in valid_dates) or (month not in valid_months) or (year not in valid_years):
        if flagged_date is False:
            flagged_date = True
            lbl_invalid_date = Label(master = register_window, text = "Invalid birthday. Please select again.", font = 10, fg = "red")
            lbl_invalid_date.pack()
        else:
            pass
        return

    # If the date does not correlate to a month correctly
    months_30 = ["April", "June", "September", "November"]
    if ((month in months_30) and (date == '31')) or ((month == "February") and (date in ["30", "31"])):
        if flagged_date is False:
            flagged_date = True
            lbl_invalid_date = Label(master = register_window, text = "Invalid birthday. Please select again.", font = 10, fg = "red")
            lbl_invalid_date.pack()
        else:
            pass
        return

    # If the dates dont correlate to a leap year
    if (month == "February" and date == "29"):
        if int(year) % 4 != 0:
            if flagged_date is False:
                flagged_date = True
                lbl_invalid_date = Label(master = register_window, text = "Invalid birthday. Please select again.", font = 10, fg = "red")
                lbl_invalid_date.pack()
            else:
                pass
            return
    
    # If the date is in the future
    future_flag = False
    if (int(year) == current_year):
        if int(dict_months[month]) > today.month:
            future_flag = True
        elif int(dict_months[month]) == today.month:
            if int(date) > today.day:
                future_flag = True
    
    if future_flag is True:
        if flagged_date is False:
                flagged_date = True
                lbl_invalid_date = Label(master = register_window, text = "Invalid birthday. Please select again.", font = 10, fg = "red")
                lbl_invalid_date.pack()
        else:
            pass
        return


    # Reformat the birthday and place it into user info list
    birthday = f'{year}-{dict_months[month]}-{date}'
    user_info[6] = birthday

    # Forget everything and move on to the next section
    lbl_birthday.forget()
    cmb_date.forget()
    cmb_month.forget()
    cmb_year.forget()
    frm_date.forget()
    frm_date_grid.forget()
    flagged_date = False
    try:
        lbl_invalid_date.forget()
    except Exception:
        pass

    phase6()