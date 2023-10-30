import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    link_customers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    link_customer_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    addnew_xpath = "//a[normalize-space()='Add new']"
    input_email_xpath = "//input[@id='Email']"
    input_password_xpath = "//input[@id='Password']"
    input_firstname_xpath = "//input[@id='FirstName']"
    input_lastname_xpath = "//input[@id='LastName']"
    gender_male_xpath = "//input[@id='Gender_Male']"
    gender_female_xpath = "//input[@id='Gender_Male']"
    dob_xpath = "//input[@id='DateOfBirth']"
    companyname_xpath = "//input[@id='Company']"
    taxattempt_xpath = "//input[@id='IsTaxExempt']"
    customrole_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    registered_xpath = "//li[@id='c07efefd-133f-48cc-ab8a-ba530d6acd16']"
    vendors_xpath = "//li[contains(text(),'Vendors')]"
    guests_xpath = "//li[normalize-space()='Guests']"
    Forummoderators_xpath = "//li[normalize-space()='Forum Moderators']"
    administrators_xpath = "//li[normalize-space()='Administrators']"
    manage_vendor_xpath = "//select[@id='VendorId']"
    checkbox_xpath = "//input[@id='Active']"
    comment_xpath = "//textarea[@id='AdminComment']"
    save_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver = driver

    def clickoncustomersmenu(self):
        self.driver.find_element(By.XPATH, self.link_customers_menu_xpath).click()

    def clickoncustomersmenuitem(self):
        self.driver.find_element(By.XPATH, self.link_customer_menuitem_xpath).click()

    def clickonAddnew(self):
        self.driver.find_element(By.XPATH, self.addnew_xpath).click()

    def setemail(self, email):
        self.driver.find_element(By.XPATH, self.input_email_xpath).send_keys(email)

    def setpassword(self, password):
        self.driver.find_element(By.XPATH, self.input_password_xpath).send_keys(password)

    def setfirstname(self, firstname):
        self.driver.find_element(By.XPATH, self.input_firstname_xpath).send_keys(firstname)

    def setlastname(self, lastname):
        self.driver.find_element(By.XPATH, self.input_lastname_xpath).send_keys(lastname)

    def setdob(self, dob):
        self.driver.find_element(By.XPATH, self.dob_xpath).send_keys(dob)

    def setcompanyname(self, companyname):
        self.driver.find_element(By.XPATH, self.companyname_xpath).send_keys(companyname)

    def setcustomersroles(self, role):
        self.driver.find_element(By.XPATH, self.customrole_xpath).click()
        if role == 'Registerd':
            self.listitem = self.driver.find_element(By.XPATH, self.registered_xpath)
        elif role == 'vendor':
            self.listitem = self.driver.find_element(By.XPATH, self.vendors_xpath)
        elif role == 'Guests':
            self.listitem = self.driver.find_element(By.XPATH, self.guests_xpath)
        elif role == 'Forem Moderators':
            self.listitem = self.driver.find_element(By.XPATH, self.Forummoderators_xpath)

        else:
            self.listitem = self.driver.find_element(By.XPATH, self.guests_xpath)

        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setmanagerrole(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.manage_vendor_xpath))
        drp.select_by_visible_text(value)

    def setgender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH, self.gender_male_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.gender_female_xpath).click()

    def admincontent(self, comment):
        self.driver.find_element(By.XPATH, self.comment_xpath).send_keys(comment)

    def clicksave(self):
        self.driver.find_element(By.XPATH, self.save_xpath).click()
