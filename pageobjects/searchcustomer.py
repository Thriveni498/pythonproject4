from selenium import webdriver
from selenium.webdriver.common.by import By

class searchcustomer:
    serach_email_id="SearchEmail"
    serach_firstname_id="SearchFirstName"
    serach_lastname_id="SearchLastName"
    search_id="search-customers"


    table_xpath ="//div[@class='dataTables_scrollHeadInner']//table[@class='table table-bordered table-hover table-striped dataTable no-footer']"


    def __init__(self,driver):
        self.driver=driver

    def enteremail(self,email):
        self.driver.find_element(By.ID, self.serach_email_id).send_keys(email)

    def enterfirstname(self,firstname):
        self.driver.find_element(By.ID, self.serach_firstname_id).send_keys(firstname)

    def enterlastname(self, lastname):
        self.driver.find_element(By.ID, self.serach_lastname_id).send_keys(lastname)

    def clickonsearch(self):
        self.driver.find_element(By.ID, self.search_id).click()



