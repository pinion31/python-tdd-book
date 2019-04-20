import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
from unittest import skip

MAX_WAIT=10

class FunctionalTest(StaticLiveServerTestCase):
  def setUp(self):
    self.browser = webdriver.Firefox()
    staging_server = os.environ.get('STAGING_SERVER')
    if staging_server:
      self.live_server_url = 'http://' + staging_server

  def tearDown(self):
    self.browser.quit()

  def wait_for_row_in_list_table(self, row_text):
    WebDriverWait(self.browser, 10).until(
            expected_conditions.text_to_be_present_in_element(
                (By.ID, 'id_list_table'), row_text))

  def wait_for(self, fn):
    start_time = time.time()
    while True:
      try:
        return fn()
      except (AssertionError, WebDriverException) as e:
        if time.time() - start_time > MAX_WAIT:
          raise e
        time.sleep(0.5)

  def get_item_input_box(self):
    return self.browser.find_element_by_id('id_text')
