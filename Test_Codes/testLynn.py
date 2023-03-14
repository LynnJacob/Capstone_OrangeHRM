# testLynn.py

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from Test_Data.data import Login_Data
from Test_Locators.locators import Login_Locators
from time import sleep
import pytest

class Test_Lynn:
    # booting function for running the Pytest testcases

    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.get(Login_Data().url)
        self.driver.maximize_window()
        yield
        #self.driver.close()

    def test_login(self, boot):
        self.driver.find_element(by=By.NAME, value=Login_Locators().username_locator).send_keys(Login_Data().username)
        self.driver.find_element(by=By.NAME, value=Login_Locators().password_locator).send_keys(Login_Data().password)
        self.driver.find_element(by=By.XPATH, value=Login_Locators().submit_locator).click()


    def test_invalid_login(self, boot):
        self.driver.find_element(by=By.NAME, value=Login_Locators().username_locator).send_keys(Login_Data().username)
        self.driver.find_element(by=By.NAME, value=Login_Locators().password_locator).send_keys(Login_Data().invalid_password)
        self.driver.find_element(by=By.XPATH, value=Login_Locators().submit_locator).click()
        element = self.driver.find_element(by=By.XPATH, value=Login_Locators().fetch_error_locator).text
        print("Fetching Error Message from Web Page : ", element)
        assert self.driver.current_url != Login_Data().url, "Invalid Login Credentials" 


    def test_pim_add_emp(self, boot):
        self.test_login(self)
        self.driver.implicitly_wait(5)
        self.driver.find_element(by=By.XPATH, value=Login_Locators().pim_locator).click()
        self.driver.find_element(by=By.XPATH, value=Login_Locators().add_locator).click()
        
        # entering basic details
        self.driver.find_element(by=By.NAME, value=Login_Locators().firstname_locator).send_keys(Login_Data().firstname)
        self.driver.find_element(by=By.NAME, value=Login_Locators().middlename_locator).send_keys(Login_Data().middlename)
        self.driver.find_element(by=By.NAME, value=Login_Locators().lastname_locator).send_keys(Login_Data().lastname)
        self.driver.find_element(by=By.XPATH, value=Login_Locators().upload_img_locator).send_keys(Login_Data().filepath)
        self.driver.find_element(by=By.XPATH, value=Login_Locators().save_emp_locator).click()

        # entering personal details
        
        self.driver.find_element(by=By.XPATH, value=Login_Locators().nickname_locator).send_keys(Login_Data().nickname)
        self.driver.find_element(by=By.XPATH, value=Login_Locators().otherid_locator).send_keys(Login_Data().otherid)
        self.driver.find_element(by=By.XPATH, value=Login_Locators().license_num_locator).send_keys(Login_Data().license_num)
        self.driver.find_element(by=By.XPATH, value=Login_Locators().license_exp_date_locator).send_keys(Login_Data().lic_exp_date)
        self.driver.find_element(by=By.XPATH, value=Login_Locators().ssn_num_locator).send_keys(Login_Data().ssn_num)
        self.driver.find_element(by=By.XPATH, value=Login_Locators().sin_num_locator).send_keys(Login_Data().sin_num)
        self.driver.find_element(by=By.XPATH, value=Login_Locators().dob_locator).send_keys(Login_Data().date_of_birth)
        self.driver.find_element(by=By.XPATH, value=Login_Locators().gender_locator).click()
        self.driver.find_element(by=By.XPATH, value=Login_Locators().mil_serv_locator).send_keys(Login_Data().mil_service)
        self.driver.find_element(by=By.XPATH, value=Login_Locators().edit_save_locator).click()


    def test_delete_emp(self, boot):
        self.test_login(self)
        self.driver.find_element(by=By.XPATH, value=Login_Locators().pim_locator).click()
        self.driver.find_element(by=By.XPATH, value=Login_Locators().emp_name_locator).send_keys(Login_Data().emp_name_search)
        self.driver.find_element(by=By.XPATH, value=Login_Locators().search_locator).click()
        sleep(6)
        self.driver.find_element(by=By.XPATH, value=Login_Locators().del_emp_locator).click()
        self.driver.find_element(by=By.XPATH, value=Login_Locators().del_confirm_locator).click()
        
                  
    def test_pim_edit_emp(self, boot):
        self.test_login(self)
        self.driver.find_element(by=By.XPATH, value=Login_Locators().pim_locator).click()
        self.driver.find_element(by=By.XPATH, value=Login_Locators().add_locator).click()
        
        self.driver.find_element(by=By.NAME, value=Login_Locators().firstname_locator).send_keys(Login_Data().firstname)
        self.driver.find_element(by=By.NAME, value=Login_Locators().middlename_locator).send_keys(Login_Data().middlename)
        self.driver.find_element(by=By.NAME, value=Login_Locators().lastname_locator).send_keys(Login_Data().lastname)
        self.driver.find_element(by=By.XPATH, value=Login_Locators().save_emp_locator).click()

        self.driver.find_element(by=By.XPATH, value=Login_Locators().pim_locator).click()
        self.driver.find_element(by=By.XPATH, value=Login_Locators().emp_name_locator).send_keys(Login_Data().emp_name_search)
        self.driver.find_element(by=By.XPATH, value=Login_Locators().search_locator).click()
        sleep(7)
        
        self.driver.find_element(by=By.XPATH, value=Login_Locators().edit_emp_locator).click()
        self.driver.find_element(by=By.XPATH, value=Login_Locators().edit_firstname_locator).clear()
        self.driver.find_element(by=By.XPATH, value=Login_Locators().edit_firstname_locator).send_keys(Login_Data().edit_firstname)
        self.driver.find_element(by=By.XPATH, value=Login_Locators().edit_save_locator).click()
    
  
        
    
    
        



















        
        
    

    
        








            








