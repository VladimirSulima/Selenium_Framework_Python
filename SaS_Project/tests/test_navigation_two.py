from SaS_Project.pages.StartPage import StartPage
import pytest

def test_navigate_to_meet_us(browser):
    StartPage(browser)\
        #.fail_test()
        #.click_meet_us_navigation_menu()\
       # .expand_search_filter_menu()\
       # .select_sector_ddl_value("Aerospace & Defence")\
       # .check_page_header_text("Step inside our world")


def test_navigate_to_meet_us_one(browser):
    StartPage(browser)\
       # .click_meet_us_navigation_menu()


# def test_navigate_to_meet_us_two(browser):
#     StartPage(browser)\
#        # .click_meet_us_navigation_menu()