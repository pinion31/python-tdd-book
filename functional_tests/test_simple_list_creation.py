from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(FunctionalTest):
  def test_can_start_a_list_for_one_user(self):
    self.browser.get(self.live_server_url)
    inputbox = get_item_input_box()

    inputbox.send_keys('Buy peacock feathers')
    inputbox.send_keys(Keys.ENTER)
    self.wait_for_row_in_list_table('Buy peacock feathers')

  def test_multiple_users_can_start_lists_at_different_urls(self):
    self.browser.get(self.live_server_url)
    inputbox = get_item_input_box()

    inputbox.send_keys('Buy peacock feathers')
    inputbox.send_keys(Keys.ENTER)
    self.wait_for_row_in_list_table('Buy peacock feathers')

    edith_list_url = self.browser.current_url
    self.assertRegex(edith_list_url, '/lists/.+')

    self.browser.quit()
    self.browser = webdriver.Firefox()

    self.browser.get(self.live_server_url)
    page_text = self.browser.find_element_by_tag_name('body').text
    self.assertNotIn('Buy peacock feathers', page_text)
    self.assertNotIn('make a fly', page_text)

    inputbox = get_item_input_box()
    inputbox.send_keys('Buy milk')
    inputbox.send_keys(Keys.ENTER)
    self.wait_for_row_in_list_table('Buy milk')

    francis_list_url = self.browser.current_url
    self.assertRegex(francis_list_url, '/lists/.+')
    self.assertNotEqual(francis_list_url, edith_list_url)

    page_text = self.browser.find_element_by_tag_name('body').text
    self.assertNotIn('Buy peacock feathers', page_text)
    self.assertIn('Buy milk', page_text)
