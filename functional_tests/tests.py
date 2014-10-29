# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_main_page_opens_in_browser_and_includes_kita_overview(self):

        # Timo sucht nach einem KiTa-Platz für seine Tochter.
        # Er hat von einer super neuen Webseite gehört. Die besucht er.
        self.browser.get('http://localhost:8000')

        # Er bemerkt, dass schon in den Überschriften (page header and title) 'KiTa' erwähnt ist.
        self.assertIn('KiTa', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('KiTa', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.
        self.fail('Finish the test!')

        # She visits that URL - her to-do list is still there.

        # Die Hauptseite ist eine Karte (erstmal: Liste), die KiTas ausflistet.

        # Er klickt eine und wird zu einer Infoseite über diese KiTa weiter geleitet. 
        # Bzw. eine Seite poppt auf.

    def test_search_for_kita_near_you(self):
        # Suche in Wohnortnähe!
        pass

if __name__ == '__main__':
    unittest.main(warnings='ignore')