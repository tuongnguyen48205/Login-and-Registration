# The following modules need to be accessed by multiple functions regarding the avatar
lbl_final = "placeholder"
btn_final = "placeholder"

def phase10():
    '''
    We will now confirm that all the user's details are correct
    '''

    global register_window
    global lbl_final
    global btn_final
    global current_screen
    global frm_continue
    global btn_continue

    current_screen = 9

    # Place everything necessary on the screen
    lbl_final = Label(master = register_window, text = "\nAre all your details correct?", font = 10)
    lbl_final.pack()
    btn_final =  Button(master = register_window, text = "View details", font = ("calibre", 11),
                        fg = "black", command = lambda:view_details())
    btn_final.pack(pady = 10)

    # Change the continue button
    btn_continue.config(text = "Submit", command = lambda:continue10())