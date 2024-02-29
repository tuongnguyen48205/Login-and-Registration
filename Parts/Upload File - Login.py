def upload_file():
    '''
    Here the user can choose a picture from their system to use as their 
    profile picture
    '''
    global user_info
    global lbl_pfp

    # Open the user's files
    f_types = [('Png Files','*.png'), ('Jpg Files', '*.jpg')]   # type of files to select 
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(file=filename)

    # Place it into user info list
    img = ImageTk.getimage(img)
    img = img.resize((1000, 1000))
    img.save(f'{filename}')
    user_info[10] = filename
    
    # Now display it
    img = img.resize((125, 125))
    img = ImageTk.PhotoImage(img)
    lbl_pfp.config(image = img)
    lbl_pfp.image = img