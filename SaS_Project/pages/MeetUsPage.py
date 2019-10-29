from selenium.webdriver.common.by import By
from Framework.WebDriverWrapper import WebDriverWrapper
from SaS_Project.pages.TrainingContactsPage import *
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select


class MeetUsPage(WebDriverWrapper):

    # <editor-fold desc="Locators">
    EXPAND_SEARCH_FILTER_BUTTON = (By.XPATH, "//button[contains(text(),'Search / filter')]")
    SEAR_INPUT_FIELD = (By.XPATH, "//input[@placeholder='Search by name or keyword']")
    SECTOR_DDL_LIST = (By.XPATH, "//button[contains(text(),'Sector')]")
    OPENED_DDL = "//div[@class='dropdown dropdown--open']"
    PAGE_HEADER = (By.XPATH, "//h1")
    # </editor-fold>

    # <editor-fold desc="Click actions">
    def expand_search_filter_menu(self):
        self.find_and_click(self.EXPAND_SEARCH_FILTER_BUTTON)
        return self

    def select_sector_ddl_value(self, sector_name):
        self.find_and_click(self.SECTOR_DDL_LIST)
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.OPENED_DDL)))
        self.find_and_click(f"{self.OPENED_DDL}//a[contains(text(),'{sector_name}')]", By.XPATH)
        return self
    # </editor-fold>

    # <editor-fold desc="Set actions">
    def set_search_by_name_input_field(self, text):

        self.find_and_set_text(self.SEAR_INPUT_FIELD, text)

        return self
    # </editor-fold>

    # <editor-fold desc="Check actions">
    def check_page_header_text(self, expected_header):

        text = self.find_and_get_text(self.PAGE_HEADER)

        assert expected_header == text, f'Header  should be "{expected_header.upper()}, but was "{text.upper()}"'

        return self
    # </editor-fold>

