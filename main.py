
import json
from selenium import webdriver
from actions import *
horn_url = "https://www.mousehuntgame.com/turn.php"
login_url = "https://www.mousehuntgame.com/login.php"
game_url = "https://www.mousehuntgame.com/"


with open('user_details.json', 'r') as myfile:
    data=myfile.read()
user_dets = json.loads(data)
driver = webdriver.Chrome(executable_path=user_dets["location"])

login(driver,user_dets)

while True:
    driver.get(horn_url)
    time.sleep(901) ######<<------ time in seconds
    driver.refresh()
driver.quit()