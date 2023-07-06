import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from pageobjects.addnewcustomer import AddCustomer
from pageobjects.loginpage import Login
from utilities.readproprties import ReadConfig
from utilities.CustomLogger import LogGen
from utilities import XLUtils

class Test_003_addcustomer:
    path = ".\\TestData\mytestdata.xlsx"
    baseURL = ReadConfig.getAppliationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()




    def test_addcustomer(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.Setusername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickoncustomersmenu()
        self.addcust.clickoncustomersmenuitem()
        self.addcust.clickonAddnew()
        self.addcust.setemail("thriveni498@gmail.com")
        self.addcust.setpassword("thri@123")
        self.addcust.setfirstname("Thriveni")
        self.addcust.setlastname("veeramreddy")
        self.addcust.setdob("22/03/1995")
        self.addcust.setcompanyname("abc")
        self.addcust.setcustomersroles("Register")
        self.addcust.setmanagerrole("Vendor 1")
        self.addcust.setgender("Female")
        self.addcust.admincontent("all are filled")
        self.addcust.clicksave()



