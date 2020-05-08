from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException  
from time import sleep 
from secrets import password 
from secrets import stalk 
import pyautogui as gui
from secrets import xpos
from secrets import ypos 
class InstaBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        self.driver.maximize_window()
    def login(self,uid,pwd):
        username=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
        username.send_keys(uid)
        password = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
        password.send_keys(pwd)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button").click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
        sleep(2)
    def followers(self):
        self.driver.get("https://www.instagram.com/{}/".format(stalk))
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
        gui.moveTo(xpos,ypos)
        sleep(2)
        for i in range(200):
            gui.scroll(-1000)
        box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        links = box.find_elements_by_tag_name('a')
        return [name.text for name in links if name != ' ']
    def following(self):
        self.driver.get("https://www.instagram.com/{}/".format(stalk))
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()
        gui.moveTo(xpos,ypos)
        sleep(2)
        for i in range(200):
            gui.scroll(-1000)
        box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        links = box.find_elements_by_tag_name('a')
        return [name.text for name in links if name != ' ']


bot = InstaBot()
username="kangyiming2017"
bot.login(username,password)
followers = bot.followers()
following = bot.following()
unfollowers = []
for name in following:
    if name not in followers:
        unfollowers.append(name)

print(unfollowers)
