def previous():
    '''
    This function sends the user to the previous screen
    '''
    global current_screen
    global frm_back
    global btn_back
    global frm_continue
    global btn_continue
    global lbl_phone
    global ent_phone
    global lbl_invalid_phone
    global lbl_firstname
    global ent_firstname
    global lbl_surname
    global ent_surname
    global frm_name
    global frm_name_grid
    global lbl_invalid_name
    global lbl_title
    global opt_title
    global lbl_gender
    global opt_gender
    global lbl_invalid_choice
    global frm_gender_grid
    global frm_gender
    global lbl_birthday
    global cmb_date
    global cmb_month
    global cmb_year
    global frm_date
    global frm_date_grid
    global lbl_invalid_date
    global lbl_nationality
    global cmb_nationality
    global lbl_invalid_nationality
    global lbl_password
    global ent_password
    global lbl_confirm
    global ent_confirm
    global frm_password
    global frm_password_grid
    global btn_show
    global lbl_invalid_password
    global lbl_username
    global ent_username
    global lbl_invalid_username
    global lbl_avatar
    global lbl_pfp
    global btn_upload
    global frm_avatar
    global frm_avatar_grid
    global lbl_final
    global btn_final

    if current_screen == 1:
        frm_back.forget()
        btn_back.forget()
        btn_continue.forget()
        frm_continue.forget()
        try:
            lbl_phone.forget()
            ent_phone.forget()
            lbl_invalid_phone.forget()
        except Exception:
            pass
        phase1()
    elif current_screen == 2:
        lbl_firstname.forget()
        ent_firstname.forget()
        lbl_surname.forget()
        ent_surname.forget() 
        lbl_surname
        frm_name_grid.forget()
        frm_name.forget()
        try:
            lbl_invalid_name.forget()
        except Exception:
            pass
        phase2()
    elif current_screen == 3:
        lbl_title.forget()
        opt_title.forget()
        lbl_gender.forget()
        opt_gender.forget()
        frm_gender_grid.forget()
        frm_gender.forget()
        try:
            lbl_invalid_choice.forget()
        except Exception:
            pass
        phase3()
    elif current_screen == 4:
        lbl_birthday.forget()
        cmb_date.forget()
        cmb_month.forget()
        cmb_year.forget()
        frm_date.forget()
        frm_date_grid.forget()
        try:
            lbl_invalid_date.forget()
        except Exception:
            pass
        phase4()
    elif current_screen == 5:
        lbl_nationality.forget()
        cmb_nationality.forget()
        try:
            lbl_invalid_nationality.forget()
        except Exception:
            pass
        phase5()
    elif current_screen == 6:
        lbl_password.forget()
        ent_password.forget()
        lbl_confirm.forget()
        ent_confirm.forget()
        frm_password.forget()
        frm_password_grid.forget()
        btn_show.forget()
        try:
            lbl_invalid_password.forget()
        except Exception:
            pass
        phase6()
    elif current_screen == 7:
        lbl_username.forget()
        ent_username.forget()
        try:
            lbl_invalid_username.forget()
        except Exception:
            pass
        phase7()
    elif current_screen == 8:
        lbl_avatar.forget()
        lbl_pfp.forget()
        btn_upload.forget()
        frm_avatar.forget()
        frm_avatar_grid.forget()
        phase8()
    elif current_screen == 9:
        lbl_final.forget()
        btn_final.forget()
        phase9()