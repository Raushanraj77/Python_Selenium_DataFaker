from selenium import webdriver
from faker import Faker
fake = Faker()
driver = webdriver.Chrome("C:/chromedrv/chromedriver.exe")
driver.get("http://newtours.demoaut.com/")

driver.find_element_by_xpath("//a[contains(text(),'REGISTER')]").click()
driver.find_element_by_xpath("//input[@name='firstName']").send_keys(fake.name())
driver.find_element_by_xpath("//input[@name='lastName']").send_keys(fake.name())
driver.find_element_by_xpath("//input[@name='phone']").send_keys(fake.phone_number())
driver.find_element_by_xpath("//input[@name='userName']").send_keys(fake.safe_email())

driver.find_element_by_xpath("//input[@name='email']").send_keys(fake.user_name())
password = fake.password()
driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
driver.find_element_by_xpath("//input[@name='confirmPassword']").send_keys(password)
driver.find_element_by_xpath("//input[@name='register']").click()
driver.close()