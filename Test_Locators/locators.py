# locators.py

class Login_Locators:

    # login
    username_locator = 'username'  # name
    password_locator = 'password'  # name
    submit_locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'  # xpath

    # pim - add employee
    pim_locator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'  # xpath    
    add_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'  # xpath

    firstname_locator = 'firstName'  # name
    middlename_locator = 'middleName'  # name
    lastname_locator = 'lastName'  # name
    upload_img_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/div/button'  # xpath
    save_emp_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'  # xpath

    # personal details
    nickname_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input'  # xpath
    otherid_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input'  # xpath
    license_num_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input' # xpath
    ssn_num_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input'  # xpath
    sin_num_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input'  # xpath
    mil_serv_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input'  # xpath
    license_exp_date_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'  # xpath
    dob_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input'  # xpath
    gender_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label/span'
    marital_status_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div'
    add_save_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'  # xpath

    # search employee
    emp_name_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input'  # xpath
    search_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'  # xpath

    # error
    fetch_error_locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p'  # xpath
   
    # delete employee
    del_emp_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]'  # xpath
    del_confirm_locator = '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]'  # xpath

    # edit employee
    edit_emp_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]'  # xpath
    edit_firstname_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input'  # xpath
    edit_save_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'  # xpath

    