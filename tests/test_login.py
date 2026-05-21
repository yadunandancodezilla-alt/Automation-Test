from pages.login_page import LoginPage

def test_valid_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login("tomsmith", "SuperSecretPassword!")
    
    assert "You logged into a secure area!" in login.get_message()


def test_invalid_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login("wrong", "wrong")
    
    assert "Your username is invalid!" in login.get_message()