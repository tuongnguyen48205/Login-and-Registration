def show_password():
    '''
    This function reveals the password that the user has inputted
    '''
    global ent_confirm
    global ent_password
    global btn_show
    global hidden

    if hidden is False:
        ent_confirm.config(show = '')
        ent_password.config(show = '')
        btn_show.config(text = "Hide")
        hidden = True
    elif hidden is True:
        ent_confirm.config(show = '*')
        ent_password.config(show = '*')
        btn_show.config(text = "Show")
        hidden = False