import unittest
from selenium import webdriver


class CodeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

        cls.driver.get('http://localhost:8888/')
        cls.driver.title

    def test_enter_code1(self):
        self.code_field = self.driver.find_element_by_name('code')
        self.code_field.clear()

        self.code_field.send_keys('Whq nąfln mhvw grsudzgb xurfcb')
        self.code_field.submit()

        product = self.driver.find_element_by_tag_name('body')
        self.assertEqual(product.text, 'Ten kącik jest doprawdy uroczy')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
