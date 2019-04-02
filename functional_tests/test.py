from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

class NewVisitorTest(LiveServerTestCase):
  def setUp(self):
    self.browser = webdriver.Firefox()

  def check_for_row_in_list_table(self, row_text):
    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    self.assertIn(row_text , [row.text for row in rows])


  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):
    self.browser.get(self.live_server_url)

    self.assertIn('To-Do',self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('To-Do', header_text)

    inputbox = self.browser.find_element_by_id('id_new_item')
    self.assertEqual(
      inputbox.get_attribute('placeholder'),
      'Enter a to-do item'
    )

    inputbox.send_keys('Buy peacock feathers')
    inputbox.send_keys(Keys.ENTER)
    #time.sleep(1)
    WebDriverWait(self.browser, 10).until(
            expected_conditions.text_to_be_present_in_element(
                (By.ID, 'id_list_table'), 'Buy peacock feathers'))

    self.check_for_row_in_list_table('1: Buy peacock feathers')

    inputbox = self.browser.find_element_by_id('id_new_item')
    inputbox.send_keys('Use peacock feathers to make a fly')
    inputbox.send_keys(Keys.ENTER)
    #time.sleep(1)
    WebDriverWait(self.browser, 10).until(
            expected_conditions.text_to_be_present_in_element(
                (By.ID, 'id_list_table'), 'Use peacock feathers to make a fly'))

    self.check_for_row_in_list_table('1: Buy peacock feathers')
    self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

    #self.fail('Finish the test!')

