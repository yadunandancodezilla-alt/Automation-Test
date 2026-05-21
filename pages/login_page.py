from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    username = (By.ID, "username")
    password = (By.ID, "password")
    login_btn = (By.CSS_SELECTOR, "button[type='submit']")
    message = (By.ID, "flash")

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def login(self, user, pwd):
        self.wait.until(EC.visibility_of_element_located(self.username)).send_keys(user)
        self.wait.until(EC.visibility_of_element_located(self.password)).send_keys(pwd)
        self.wait.until(EC.element_to_be_clickable(self.login_btn)).click()

    def get_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.message)).text