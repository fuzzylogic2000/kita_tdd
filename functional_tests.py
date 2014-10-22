# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_main_page_opens_in_browser_and_includes_kita_overview(self):

        # Timo sucht nach einem KiTa-Platz für seine Tochter.
        # Er hat von einer super neuen Webseite gehört. Die besucht er.
        self.browser.get('http://localhost:8000')

        # Er bemerkt, dass schon in der Überschrift 'KiTa' erwähnt ist.
        self.assertIn('KiTa', self.browser.title)
        self.fail('Finish the test!')

        # Die Hauptseite ist eine Karte (erstmal: Liste), die KiTas ausflistet.

        # Er klickt eine und wird zu einer Infoseite über diese KiTa weiter geleitet. 
        # Bzw. eine Seite poppt auf.

    def test_search_for_kita_near_you(self):
        # Suche in Wohnortnähe!
        pass

if __name__ == '__main__':
    unittest.main(warnings='ignore')