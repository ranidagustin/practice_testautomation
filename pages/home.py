from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
# import unittest

class HomeLetsKodeIt:
  URL                       = 'https://letskodeit.teachable.com/p/practice'
  RADIO_EXAMPLE_BMW         = (By.ID, 'bmwradio')
  RADIO_EXAMPLE_BENZ        = (By.ID, 'benzradio')
  RADIO_EXAMPLE_HONDA       = (By.ID, 'hondaradio')
  SELECT_EXAMPLE            = (By.ID, 'carselect')
  SELECT_EXAMPLE_BMW        = (By.XPATH, "//option[contains(text(),'BMW')]")
  SELECT_EXAMPLE_BENZ       = (By.XPATH, "//option[contains(text(),'Benz')]")
  SELECT_EXAMPLE_HONDA      = (By.XPATH, "//option[contains(text(),'Honda')]")
  MULTIPLE_EXAMPLE          = (By.ID, 'multiple-select-example')
  SELECT_EXAMPLE_APPLE      = (By.XPATH, "//option[contains(text(),'Apple')]")
  SELECT_EXAMPLE_ORANGE     = (By.XPATH, "//option[contains(text(),'Orange')]")
  SELECT_EXAMPLE_PEACH      = (By.XPATH, "//option[contains(text(),'Peach')]")
  CHKBOX_EXAMPLE_BMW        = (By.ID, 'bmwcheck')
  CHKBOX_EXAMPLE_BENZ       = (By.ID, 'benzcheck')
  CHKBOX_EXAMPLE_HONDA      = (By.ID, 'hondacheck')
  

  def __init__(self, driver):
    self.driver = driver

  def load(self):
    self.driver.get(self.URL)

  def click_radio_example(self,option_text):
     radio_bmw   = self.driver.find_element(*self.RADIO_EXAMPLE_BMW)
     radio_benz  = self.driver.find_element(*self.RADIO_EXAMPLE_BENZ)
     radio_honda = self.driver.find_element(*self.RADIO_EXAMPLE_HONDA)

     if (option_text == "BMW"):
            radio_bmw.click()
     if (option_text == "Benz"):
            radio_benz.click()
     if (option_text == "Honda"):
            radio_honda.click()
         
  def radio_bmw_is_selected(self):
      radio_bmw = self.driver.find_element(*self.RADIO_EXAMPLE_BMW)
      return radio_bmw.is_selected()

  def radio_benz_is_selected(self):
      radio_benz = self.driver.find_element(*self.RADIO_EXAMPLE_BENZ)
      return radio_benz.is_selected()

  def radio_honda_is_selected(self):
      radio_honda = self.driver.find_element(*self.RADIO_EXAMPLE_HONDA)
    #   self.assertTrue(True,radio_honda.is_selected())
    #   self.assertFalse(False,radio_honda.is_selected())
      return radio_honda.is_selected()
  
  def select_example(self,option_text):
      select_example = Select(self.driver.find_element(*self.SELECT_EXAMPLE))
      select_example.select_by_visible_text(option_text)
  
  def select_bmw_is_selected(self):
      select_bmw =  self.driver.find_element(*self.SELECT_EXAMPLE_BMW)
      return select_bmw.is_selected() 

  def select_benz_is_selected(self):
      select_benz =  self.driver.find_element(*self.SELECT_EXAMPLE_BENZ)
      return select_benz.is_selected()

  def select_honda_is_selected(self):
      select_honda =  self.driver.find_element(*self.SELECT_EXAMPLE_HONDA)
      return select_honda.is_selected()

  def select_multiple_example(self,is_option1,is_option2,is_option3):
      select_multiple_example = Select(self.driver.find_element(*self.MULTIPLE_EXAMPLE))

      if (is_option1 == 1):
        select_multiple_example.select_by_visible_text("Apple")
      if (is_option2 == 1):
        select_multiple_example.select_by_visible_text("Orange")
      if (is_option3 == 1):
        select_multiple_example.select_by_visible_text("Peach")

  def select_apple_is_selected(self):
      select_apple =  self.driver.find_element(*self.SELECT_EXAMPLE_APPLE)
      return select_apple.is_selected() 

  def select_orange_is_selected(self):
      select_orange =  self.driver.find_element(*self.SELECT_EXAMPLE_ORANGE)
      return select_orange.is_selected()

  def select_peach_is_selected(self):
      select_peach =  self.driver.find_element(*self.SELECT_EXAMPLE_PEACH)
      return select_peach.is_selected()
  
  def tick_chkbox_example(self,is_option1,is_option2,is_option3):
      chkbox_example_bmw   = self.driver.find_element(*self.CHKBOX_EXAMPLE_BMW)
      chkbox_example_benz  = self.driver.find_element(*self.CHKBOX_EXAMPLE_BENZ)
      chkbox_example_honda = self.driver.find_element(*self.CHKBOX_EXAMPLE_HONDA)

      if (is_option1 == 1):
        chkbox_example_bmw.click()
      if (is_option2 == 1):
        chkbox_example_benz.click()
      if (is_option3 == 1):
        chkbox_example_honda.click()
  
  def chkbox_bmw_is_selected(self):
      chkbox_bmw = self.driver.find_element(*self.CHKBOX_EXAMPLE_BMW)
      return chkbox_bmw.is_selected()

  def chkbox_benz_is_selected(self):
      chkbox_benz = self.driver.find_element(*self.CHKBOX_EXAMPLE_BENZ)
      return chkbox_benz.is_selected()

  def chkbox_honda_is_selected(self):
      chkbox_honda = self.driver.find_element(*self.CHKBOX_EXAMPLE_HONDA)
      return chkbox_honda.is_selected()

    