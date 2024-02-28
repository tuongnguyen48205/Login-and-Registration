# The following modules need to be accessed by multiple functions regarding the avatar
lbl_avatar = "placeholder"
lbl_pfp = "placeholder"
btn_upload = "placeholder"
chosen_image = "placeholder"
frm_avatar = "placeholder"
frm_avatar_grid = "placeholder"

def phase9():
    '''
    The user can now choose to upload a profile picture
    '''
    global register_window
    global lbl_avatar
    global lbl_pfp
    global btn_upload
    global current_screen
    global frm_continue
    global btn_continue
    global frm_avatar
    global frm_avatar_grid

    current_screen = 8

    # Make a default profile picture based on gender
    if user_info[5] == "Male":
        profile_image = Image.open('Male.png')
    elif user_info[5] == "Female":
        profile_image = Image.open('Female.png')
    else:
        profile_image = Image.open('other.png')
    image_name = profile_image.filename

    # Place it into userinfo list for now
    profile_image = profile_image.resize((1000, 1000))
    profile_image.save(f'{image_name}')
    user_info[10] = image_name

    # Now time to place everything on the screen 
    frm_avatar = Frame(master = register_window, relief = FLAT)
    frm_avatar.pack()
    frm_avatar_grid = Frame(master = frm_avatar, relief = FLAT)
    frm_avatar_grid.grid(row = 0, column = 0)
    lbl_avatar = Label(master = frm_avatar_grid, text = "\nPlease choose a profile picture:", font = 10)
    lbl_avatar.pack(pady = 10, padx = 20)
    frm_avatar_grid = Frame(master = frm_avatar, relief = FLAT)
    frm_avatar_grid.grid(row = 1, column = 0)
    btn_upload = Button(master = frm_avatar_grid, text = "Choose image", font = ("calibre", 11),
                        fg = "black", command = lambda:upload_file())
    btn_upload.pack(pady = 10, padx = 20)
    frm_avatar_grid = Frame(master = frm_avatar, relief = FLAT)
    frm_avatar_grid.grid(row = 0, column = 1, rowspan = 2)
    profile_image = profile_image.resize((125, 125))
    profile_image = ImageTk.PhotoImage(profile_image)
    lbl_pfp = Label(master = frm_avatar_grid, image = profile_image, bg = register_window.cget('bg'))
    lbl_pfp.image = profile_image
    lbl_pfp.pack(padx = 20)

    # Redirect continue button
    btn_continue.config(command = lambda:continue9())  