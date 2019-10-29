from time import sleep

from selenium.webdriver.common.by import By
from Framework.WebDriverWrapper import WebDriverWrapper
from SaS_Project.pages.MeetUsPage import MeetUsPage
from SaS_Project.pages.TrainingContactsPage import TrainingContactPage


class StartPage(WebDriverWrapper):
    TRAINING_CONTACTS_NAVIGATION_MENU = (By.XPATH, "//li/a[@href='/en/training-contract']")
    MEET_US_NAVIGATION_MENU = (By.XPATH, "//li/a[@href='/en/meet-us']")

    def click_training_contacts_navigation_menu(self):
        self.find_and_click(self.TRAINING_CONTACTS_NAVIGATION_MENU)
        return TrainingContactPage(self.browser)

    def click_meet_us_navigation_menu(self):
        self.find_and_click(self.MEET_US_NAVIGATION_MENU)
        return MeetUsPage(self.browser)

    def fail_test(self):
        sleep(3)
        raise AssertionError("Custom fail")

