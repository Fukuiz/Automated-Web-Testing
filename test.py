import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class FrontendTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        service = Service(r"C:\path\to\your\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service, options=chrome_options)
        cls.driver.set_window_size(1280, 900)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_example(self):
        self.driver.get("https://example.com")
        element = self.driver.find_element(By.XPATH, "//input[@id='username']")
        element.send_keys("your_username")
        # Add more actions...

if __name__ == "__main__":
    unittest.main()
