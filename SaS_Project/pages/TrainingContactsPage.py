from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from Framework.WebDriverWrapper import WebDriverWrapper


class TrainingContactPage(WebDriverWrapper):

    CAREER_MENU = (By.XPATH, "//li/a[@href='#career']")

    def click_career_link(self):
        sleep(2)
        #self.wait.until(ec.presence_of_element_located((By.XPATH, "//li/a[@href='#career']")))
        #WebDriverWait(self.browser, 10).until(ec.presence_of_element_located((By.XPATH, "//li/a[@href='#career']")))
        #self.wait.until(ec.presence_of_element_located((By.XPATH, "//li/a[@href='#career']")))
        self.browser.find_element(*self.CAREER_MENU).click()
        return self
