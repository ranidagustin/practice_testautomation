import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

import pytest
from src.testproject.sdk.drivers import webdriver

from pages.home import HomeLetsKodeIt

@pytest.fixture
def driver():
  # Initialize ChromeDriver
    driver = webdriver.Chrome(token='9Zt1JzMlud93DxFhPQ72pK33TL5bDwrBo8TIjma65ec1')
  
  # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(10)
  
  # Return the driver object at the end of setup
    yield driver
  
  # For cleanup, quit the driver
    driver.quit()

def test_latihan1(driver):
    #parameter list
    STR_OPTION_BMW   = "BMW"
    STR_OPTION_BENZ  = "Benz"
    STR_OPTION_HONDA = "Honda"

    BOOL_OPTION_APPLE   = 0
    BOOL_OPTION_ORANGE  = 1
    BOOL_OPTION_PEACH   = 1

    BOOL_OPTION_BMW   = 0
    BOOL_OPTION_BENZ  = 1
    BOOL_OPTION_HONDA = 1

    # Buka halaman home
    home_page = HomeLetsKodeIt(driver)
    home_page.load()

    #choose radio button option
    home_page.click_radio_example(STR_OPTION_HONDA)

    #choose select option
    home_page.select_example(STR_OPTION_HONDA)

    #choose multiple select option
    home_page.select_multiple_example(BOOL_OPTION_APPLE,BOOL_OPTION_ORANGE,BOOL_OPTION_PEACH)

    #tick checkbox
    home_page.tick_chkbox_example(BOOL_OPTION_BMW,BOOL_OPTION_BENZ,BOOL_OPTION_HONDA)

    #assert the choice
    # home_page.radio_honda_is_selected()
    # print(home_page.radio_honda_is_selected())
    if (home_page.radio_honda_is_selected() == 1):
        print ("Honda selected")
    else:
        print ("Honda not selected")

    if (home_page.select_honda_is_selected() == 1):
        print ("Honda selected")
    else:
        print ("Honda not selected")

    if (home_page.select_orange_is_selected() == 1 and home_page.select_peach_is_selected() == 1):
        print ("Orange and Peach selected")
    else:
        print ("Orange and Peach not selected")
    
    if (home_page.chkbox_benz_is_selected() == 1 and home_page.chkbox_honda_is_selected() == 1):
        print ("Benz and Honda selected")
    else:
        print ("Benz and Honda not selected")
  

    

