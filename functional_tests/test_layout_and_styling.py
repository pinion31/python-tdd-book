from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys

class LayoutAndStylingTest(FunctionalTest):
  def test_layout_and_styling(self):
    self.browser.get(self.live_server_url)
    self.browser.set_window_size(1024, 768)


    inputbox = get_item_input_box()
    inputbox.send_keys('testing')
    inputbox.send_keys(Keys.ENTER)

    self.wait_for_row_in_list_table('testing')
    inputbox = get_item_input_box()
    self.assertAlmostEqual(
      inputbox.location['x'] + inputbox.size['width'] / 2,
      512,
      delta=10
    )

