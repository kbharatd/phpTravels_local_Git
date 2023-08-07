from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    Text_Email_XPATH = (By.XPATH, "//input[@id='email']")
    Text_Password_XPATH = (By.XPATH, "//input[@id='password']")
    Click_Login_XPATH = (By.XPATH, "//button[@id='submit']")
    Click_Menu_XPATH = (By.XPATH, "//a[@id='dropdownUser1']")
    Click_Logout_XPATH = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)

    def Enter_Email(self, email):
        self.wait.until(expected_conditions.presence_of_element_located(self.Text_Email_XPATH))
        self.driver.find_element(*LoginPage.Text_Email_XPATH).send_keys(email)

    def Enter_Password(self, password):
        self.wait.until(expected_conditions.presence_of_element_located(self.Text_Password_XPATH))
        self.driver.find_element(*LoginPage.Text_Password_XPATH).send_keys(password)

    def Click_Login(self):
        self.driver.find_element(*LoginPage.Click_Login_XPATH).click()

    def Click_Menu(self):
        self.driver.find_element(*LoginPage.Click_Menu_XPATH).click()

    def Click_Logout(self):
        self.driver.find_element(*LoginPage.Click_Logout_XPATH).click()


