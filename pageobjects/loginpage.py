from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    test_email = "Email"
    test_password = "Password"
    button_login_xpath = "//button[normalize-space()='Log in']"
    input_logout_xpath = "//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver = driver


    def Setusername(self,username):
        self.driver.find_element(By.ID, self.test_email).clear()
        self.driver.find_element(By.ID, self.test_email).send_keys(username)

    def Setpassword(self,password):
        self.driver.find_element(By.ID, self.test_password).clear()
        self.driver.find_element(By.ID, self.test_password).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clicklogout(self):
        self.driver.find_element(By.XPATH, self.input_logout_xpath).click()