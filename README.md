
# How to Use Selenium for Automated Testing

1. **Install Required Packages**
   - Ensure you have Python installed on your machine.
   - Install the necessary packages using pip:
     ```bash
     pip install selenium
     ```

2. **Download ChromeDriver**
   - Download the ChromeDriver executable compatible with your version of Chrome from [ChromeDriver downloads](https://sites.google.com/chromium.org/driver/).
   - Place the `chromedriver.exe` in a directory of your choice (e.g., `C:\Users\YourUsername\Desktop\automated\`).

3. **Import Necessary Modules**
   - Create a new Python script and import the following modules:
     ```python
     import unittest
     from selenium import webdriver
     from selenium.webdriver.common.by import By
     from selenium.webdriver.chrome.service import Service
     from selenium.webdriver.chrome.options import Options
     ```

4. **Set Up the WebDriver**
   - Define a class that inherits from `unittest.TestCase` and set up the Chrome WebDriver:
     ```python
     class FrontendTest(unittest.TestCase):
         @classmethod
         def setUpClass(cls):
             chrome_options = Options()
             chrome_options.add_argument("--no-sandbox")
             chrome_options.add_argument("--disable-dev-shm-usage")
             service = Service(r"C:\Users\YourUsername\Desktop\automated\chromedriver.exe")
             cls.driver = webdriver.Chrome(service=service, options=chrome_options)
             cls.driver.set_window_size(1280, 900)
             cls.driver.implicitly_wait(10)
     ```

5. **Write Test Cases**
   - Implement test methods to automate interactions with the web application:
   - you can use this website to try https://practicetestautomation.com/practice-test-login/
     ```python
     def test_login(self):
         self.driver.get("https://practicetestautomation.com/practice-test-login/")
         username_input = self.driver.find_element(By.XPATH, "//input[@id='username']")
         username_input.send_keys("student")
         password_input = self.driver.find_element(By.XPATH, "//input[@id='password']")
         password_input.send_keys("Password123")
         submit_button = self.driver.find_element(By.XPATH, "//button[@id='submit']")
         submit_button.click()
     ```

6. **Clean Up After Tests**
   - Ensure that the WebDriver quits after tests have completed:
     ```python
     @classmethod
     def tearDownClass(cls):
         cls.driver.quit()
     ```

7. **Run the Tests**
   - Add the following code to execute the tests:
     ```python
     if __name__ == "__main__":
         unittest.main()
     ```
   - Run your script to execute the tests.
  

## Common Selenium Commands
- **Find Element**: `self.driver.find_element(By.XPATH, "xpath")`
- **Send Keys**: `element.send_keys("text")`
- **Click**: `element.click()`
- **Wait for Element**: Use `implicitly_wait(seconds)` to set a default wait time

## Importing Modules and Their Roles
1. **Importing the unittest Module**
   This imports the unittest framework, which is used to create and run test cases in Python.

2. **Importing the WebDriver**
   The webdriver from the selenium package is imported to control web browsers programmatically.

3. **Importing By for Element Locating**
   The By class is imported from selenium.webdriver.common to define different strategies for locating web elements (like using XPath or ID).

4. **Importing the Service Class**
   The Service class from selenium.webdriver.chrome.service is imported to manage the ChromeDriver process that communicates with the Chrome browser.

5. **Importing Options for Browser Configuration**
   The Options class from selenium.webdriver.chrome.options is imported to set various configuration options for the ChromeDriver, such as running in headless mode or specifying window size.

6. **Creating a Test Class**
   A test class is defined by subclassing unittest.TestCase, which allows you to group related test cases together.

7. **Setting Up and Tearing Down Tests**
   You define setup and teardown methods (like setUpClass and tearDownClass) to initialize the WebDriver before tests run and to quit the browser after all tests are complete.

