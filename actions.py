import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


horn_url = "https://www.mousehuntgame.com/turn.php"
login_url = "https://www.mousehuntgame.com/login.php"
game_url = "https://www.mousehuntgame.com/"


def login(driver, user_dets):
    driver.get(login_url)
    driver.find_element_by_class_name("signInText").click()
    time.sleep(0.1)
    login = driver.find_elements_by_class_name("login")[-1]
    login.find_element_by_name("username").send_keys(user_dets["username"])
    login.find_element_by_name("password").send_keys(user_dets["password"])
    login.find_element_by_class_name("actionButton").click()
    driver.get(game_url)

