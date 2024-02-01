def access_granted(account):
    '''
    This function allows for the user to access whatever is on the other side
    of this login and reigstration system whether it be a task manager, a databse,
    a daily planner, etc. In this case, it closes the main login window. It has the 
    users account as the argument so that it can be personalised to each user
    '''
    # Create a new window for whatever application
    global login_window
    login_window.destroy()
    application_window = Tk()
    application_window.attributes('-fullscreen', True)
    application_window.title("Application")

    # Place a bar at top and bottom
    frm_bar = Frame(master = application_window, height = 100, bg = "#538c50")
    frm_bar.pack(fill = X, side = TOP)

    # Quick summary of the users information
    lbl_user_summary_title = Label(master = application_window, text = "User Summary:", font = ('ariel', 80, 'bold'))
    lbl_user_summary_title.pack()
    lbl_user_summary = Label(master = application_window, font = ('ariel', 30), text = f"Welcome {account[4]} {account[2]} {account[3]}\nemail: {account[0]}\nphone number: {account[1]}\ngender: {account[5]}\nbirthday (YYYY-MM-DD): {account[6]}\nnationality: {account[7]}\nusername: {account[8]}")
    lbl_user_summary.pack()

    # Place in their profile iamge
    profimg = Image.open(f'{account[10]}')
    profimg = profimg.resize((300, 300))
    profimg = ImageTk.PhotoImage(profimg)
    lbl_profimg = Label(image = profimg)
    lbl_profimg.pack()

    # Say happy birtday if it's the users's birthday
    today = datetime.date.today()
    if str(today)[9:5:-1] == account[6][9:5:-1]:
        lbl_happybday = Label(master = application_window, text = "Happy Birthday!!", font = ('ariel', 30))
        lbl_happybday.pack()

    # Create an exit button to close the application
    frm_exit = Frame(master = application_window, relief = RAISED, height = 100, bg = "#538c50")
    frm_exit.pack(fill = X, side = BOTTOM)
    btn_exit = Button(master = frm_exit, text = "Exit", font = ('ariel', 30, 'bold'), command = lambda:application_window.destroy())
    btn_exit.pack(side = BOTTOM)

    application_window.mainloop()