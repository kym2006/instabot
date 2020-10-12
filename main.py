import os
import sys
from time import sleep

from dotenv import load_dotenv
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--incognito")


class InstaBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://instagram.com")
        self.driver.maximize_window()
        sleep(1)

    def login(self, uid, pwd):
        user = self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input"
        )
        user.send_keys(uid)
        password = self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input"
        )
        password.send_keys(pwd)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button"
        ).click()
        sleep(2.5)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
        sleep(1)

    def followers(self):
        self.driver.get("https://www.instagram.com/{}/".format(USER))
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
        sleep(1)
        box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script(
                """
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """,
                box,
            )
        links = box.find_elements_by_tag_name("a")
        return [name.text for name in links if name != " "]

    def following(self):
        self.driver.get("https://www.instagram.com/{}/".format(USER))
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()
        sleep(1)
        box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script(
                """
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """,
                box,
            )
        links = box.find_elements_by_tag_name("a")
        names = [name.text for name in links if name != " "]
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()
        return names


load_dotenv()
IGN = os.getenv("IGN")
PASS = os.getenv("PASS")
USER = os.getenv("USR")

bot = InstaBot()
bot.login(IGN, PASS)
followers = bot.followers()
following = bot.following()

unfollowers = []
for name in following:
    if name not in followers:
        unfollowers.append(name)

sys.stdout = open(f"{USER}.txt", "w")

for i in range(len(unfollowers)):
    print(f"{i + 1}. {unfollowers[i]}")

sys.stdout.close()
bot.driver.close()
