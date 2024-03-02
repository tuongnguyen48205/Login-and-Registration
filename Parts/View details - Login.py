def view_details():
    '''
    Here the user can see all their details
    '''
    # Create instance of tkinter window and the labels found on the window (title, etc.)
    details_window = Toplevel()
    details_window.geometry("800x600")
    details_window.title("Details")
    details_window.resizable(False,False)

    # Now insert logo and company name (in this example, I will use my own placeholder
    # but these can be changed)
    frm_details_logo = Frame(master = details_window)
    frm_details_logo.pack(pady = 15)
    img_details_logo = Image.open('logo task organiser.png') # This logo can be changed
    img_details_logo = img_details_logo.resize((150, 150))
    img_details_logo = ImageTk.PhotoImage(img_details_logo)
    for i in range(2):
        frm_details_logo_grid = Frame(master = frm_details_logo)
        frm_details_logo_grid.grid(row = 0, column = i, padx = 10)
        if i == 0:
            lbl_details_logo = Label(master = frm_details_logo_grid, image = img_details_logo)
            lbl_details_logo.pack()
            lbl_details_logo.image = img_details_logo
        else:
            # The following title label can be changed
            lbl_details_logo_text = Label(master = frm_details_logo_grid, text = "GROTANIX Task Organiser",
                                font = ("calibre", 25, "bold"), fg = "#538c50")
            lbl_details_logo_text.pack()
            lbl_details = Label(master = frm_details_logo_grid, text = "User Details",
                                font = ("calibre", 20, "bold"), fg = "#264124")
            lbl_details.pack()

    # Now time to place in all the user details
    template = ["                                        Email                                        ", 
                "                                        Phone Number                                 ", 
                "                                        Firstname                                    ", 
                "                                        Surname                                      ", 
                "                                        Title                                        ", 
                "                                        Gender                                       ", 
                "                                        Birthday (YYYY/MM/DD)                        ", 
                "                                        Nationality                                  ", 
                "                                        Password                                     ", 
                "                                        Username                                     ", 
                "                                        Profile Photo                                "]
    for i in range(len(user_info)):
        if i % 2 == 0:
            frm_master = Frame(master = details_window)
            frm_master.pack(fill = X, pady = 5)
            frm_sub_grid = Frame(master = frm_master)
            frm_sub_grid.grid(row = i, column = 0)
            lbl_template = Label(master = frm_sub_grid, text = template[i], font = 10)
            lbl_template.pack()
            frm_sub_grid = Frame(master = frm_master)
            frm_sub_grid.grid(row = i, column = 1)
            lbl_info = Label(master = frm_sub_grid, text = user_info[i], font = 10)
            lbl_info.pack()
        else:
            frm_master = Frame(master = details_window, bg = 'light grey')
            frm_master.pack(fill = X, pady = 5)
            frm_sub_grid = Frame(master = frm_master)
            frm_sub_grid.grid(row = i, column = 0)
            lbl_template = Label(master = frm_sub_grid, text = template[i], font = 10, bg = 'light grey')
            lbl_template.pack()
            frm_sub_grid = Frame(master = frm_master)
            frm_sub_grid.grid(row = i, column = 1)
            lbl_info = Label(master = frm_sub_grid, text = user_info[i], font = 10, bg = 'light grey')
            lbl_info.pack()

    # Add an exit button at the bottom
    frm_exit_final = Frame(master = details_window, relief = RAISED, borderwidth = 5)
    frm_exit_final.pack()
    btn_exit_final = Button(master = frm_exit_final, text = "Done", command = lambda:details_window.destroy(),
                            font = ("calibre", 11), fg = "black",)
    btn_exit_final.pack()