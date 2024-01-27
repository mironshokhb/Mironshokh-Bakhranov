from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import unittest
from faker import Faker
import time

faker_class = Faker()


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_chrome(self):
        driver = self.driver
        driver.get("https://qasvus.wordpress.com")

        try:
            assert "California Real Estate" in driver.title
        except AssertionError:
            print("Driver title in Chrome is:", driver.title)

        try:
            driver.find_element(By.XPATH, '//*[@value="Close and accept"]').click()
        except NoSuchElementException:
            print("No 'Close and accept' appear")

        driver.find_element(By.XPATH, '//*[text()="Send Us a Message"]')
        nameField = driver.find_element(By.ID, 'g2-name')
        nameField.clear()
        nameField.send_keys(faker_class.name())

        driver.find_element(By.NAME, 'g2-email')
        emailField = driver.find_element(By.ID, 'g2-email')
        emailField.clear()
        emailField.send_keys(faker_class.email())

        driver.find_element(By.ID, 'contact-form-comment-g2-message')
        textField = driver.find_element(By.ID, 'contact-form-comment-g2-message')
        textField.clear()
        textField.send_keys(faker_class.text())

        time.sleep(5)
        driver.find_element(By.CLASS_NAME, 'pushbutton-wide').click()

        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Go back')]")))

        driver.find_element(By.XPATH, "//a[contains(text(),'Go back')]").send_keys('\n')
        print(driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").get_attribute("type"))

        time.sleep(2)
        assert "California Real Estate" in driver.title
        print("Testing page has", driver.title + "as Page title. Test complete and each step done correctly.")

    def test_edge_1820x1050(self):
        driver = self.driver
        driver.set_window_size(1820, 1050)
        driver.get("https://qasvus.wordpress.com")
        try:
            assert "California Real Estate" in driver.title
        except AssertionError:
            print("Driver title in Chrome is:", driver.title)

        try:
            driver.find_element(By.XPATH, '//*[@value="Close and accept"]').click()
        except NoSuchElementException:
            print("No 'Close and accept' appear")

        driver.find_element(By.XPATH, '//*[text()="Send Us a Message"]')
        nameField = driver.find_element(By.ID, 'g2-name')
        nameField.clear()
        nameField.send_keys(faker_class.name())

        driver.find_element(By.NAME, 'g2-email')
        emailField = driver.find_element(By.ID, 'g2-email')
        emailField.clear()
        emailField.send_keys(faker_class.email())

        driver.find_element(By.ID, 'contact-form-comment-g2-message')
        textField = driver.find_element(By.ID, 'contact-form-comment-g2-message')
        textField.clear()
        textField.send_keys(faker_class.text())

        time.sleep(5)
        driver.find_element(By.CLASS_NAME, 'pushbutton-wide').click()

        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Go back')]")))

        driver.find_element(By.XPATH, "//a[contains(text(),'Go back')]").send_keys('\n')
        print(driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").get_attribute("type"))

        time.sleep(2)
        assert "California Real Estate" in driver.title
        print("Testing page has", driver.title + "as Page title. Test complete and each step done correctly.")

    def test_chrome_2560x1440(self):
        driver = self.driver
        driver.set_window_size(2560, 1440)
        driver.get("https://qasvus.wordpress.com")
        try:
            assert "California Real Estate" in driver.title
        except AssertionError:
            print("Driver title in Chrome is:", driver.title)

        try:
            driver.find_element(By.XPATH, '//*[@value="Close and accept"]').click()
        except NoSuchElementException:
            print("No 'Close and accept' appear")

        driver.find_element(By.XPATH, '//*[text()="Send Us a Message"]')
        nameField = driver.find_element(By.ID, 'g2-name')
        nameField.clear()
        nameField.send_keys(faker_class.name())

        driver.find_element(By.NAME, 'g2-email')
        emailField = driver.find_element(By.ID, 'g2-email')
        emailField.clear()
        emailField.send_keys(faker_class.email())

        driver.find_element(By.ID, 'contact-form-comment-g2-message')
        textField = driver.find_element(By.ID, 'contact-form-comment-g2-message')
        textField.clear()
        textField.send_keys(faker_class.text())

        time.sleep(5)
        driver.find_element(By.CLASS_NAME, 'pushbutton-wide').click()

        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Go back')]")))

        driver.find_element(By.XPATH, "//a[contains(text(),'Go back')]").send_keys('\n')
        print(driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").get_attribute("type"))

        time.sleep(2)
        assert "California Real Estate" in driver.title
        print("Testing page has", driver.title + "as Page title. Test complete and each step done correctly.")

    def test_chrome_1920x1080(self):
        driver = self.driver
        driver.set_window_size(1920, 1080)
        driver.get("https://qasvus.wordpress.com")
        try:
            assert "California Real Estate" in driver.title
        except AssertionError:
            print("Driver title in Chrome is:", driver.title)

        try:
            driver.find_element(By.XPATH, '//*[@value="Close and accept"]').click()
        except NoSuchElementException:
            print("No 'Close and accept' appear")

        driver.find_element(By.XPATH, '//*[text()="Send Us a Message"]')
        nameField = driver.find_element(By.ID, 'g2-name')
        nameField.clear()
        nameField.send_keys(faker_class.name())

        driver.find_element(By.NAME, 'g2-email')
        emailField = driver.find_element(By.ID, 'g2-email')
        emailField.clear()
        emailField.send_keys(faker_class.email())

        driver.find_element(By.ID, 'contact-form-comment-g2-message')
        textField = driver.find_element(By.ID, 'contact-form-comment-g2-message')
        textField.clear()
        textField.send_keys(faker_class.text())

        time.sleep(5)
        driver.find_element(By.CLASS_NAME, 'pushbutton-wide').click()

        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Go back')]")))

        driver.find_element(By.XPATH, "//a[contains(text(),'Go back')]").send_keys('\n')
        print(driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").get_attribute("type"))

        time.sleep(2)
        assert "California Real Estate" in driver.title
        print("Testing page has", driver.title + "as Page title. Test complete and each step done correctly.")

    def tearDown(self):
        self.driver.quit()


class EdgeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()

    def test_edge(self):
        driver = self.driver
        driver.get("https://qasvus.wordpress.com")

        try:
            assert "California Real Estate" in driver.title
        except AssertionError:
            print("Driver title in Chrome is:", driver.title)

        try:
            driver.find_element(By.XPATH, '//*[@value="Close and accept"]').click()
        except NoSuchElementException:
            print("No 'Close and accept' appear")

        driver.find_element(By.XPATH, '//*[text()="Send Us a Message"]')
        nameField = driver.find_element(By.ID, 'g2-name')
        nameField.clear()
        nameField.send_keys(faker_class.name())

        driver.find_element(By.NAME, 'g2-email')
        emailField = driver.find_element(By.ID, 'g2-email')
        emailField.clear()
        emailField.send_keys(faker_class.email())

        driver.find_element(By.ID, 'contact-form-comment-g2-message')
        textField = driver.find_element(By.ID, 'contact-form-comment-g2-message')
        textField.clear()
        textField.send_keys(faker_class.text())

        time.sleep(5)
        driver.find_element(By.CLASS_NAME, 'pushbutton-wide').click()

        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Go back')]")))

        driver.find_element(By.XPATH, "//a[contains(text(),'Go back')]").send_keys('\n')
        print(driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").get_attribute("type"))

        time.sleep(2)
        assert "California Real Estate" in driver.title
        print("Testing page has", driver.title + "as Page title. Test complete and each step done correctly.")

    def test_edge_1820x1050(self):
        driver = self.driver
        driver.set_window_size(1820, 1050)
        driver.get("https://qasvus.wordpress.com")
        try:
            assert "California Real Estate" in driver.title
        except AssertionError:
            print("Driver title in Chrome is:", driver.title)

        try:
            driver.find_element(By.XPATH, '//*[@value="Close and accept"]').click()
        except NoSuchElementException:
            print("No 'Close and accept' appear")

        driver.find_element(By.XPATH, '//*[text()="Send Us a Message"]')
        nameField = driver.find_element(By.ID, 'g2-name')
        nameField.clear()
        nameField.send_keys(faker_class.name())

        driver.find_element(By.NAME, 'g2-email')
        emailField = driver.find_element(By.ID, 'g2-email')
        emailField.clear()
        emailField.send_keys(faker_class.email())

        driver.find_element(By.ID, 'contact-form-comment-g2-message')
        textField = driver.find_element(By.ID, 'contact-form-comment-g2-message')
        textField.clear()
        textField.send_keys(faker_class.text())

        time.sleep(5)
        driver.find_element(By.CLASS_NAME, 'pushbutton-wide').click()

        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Go back')]")))

        driver.find_element(By.XPATH, "//a[contains(text(),'Go back')]").send_keys('\n')
        print(driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").get_attribute("type"))

        time.sleep(2)
        assert "California Real Estate" in driver.title
        print("Testing page has", driver.title + "as Page title. Test complete and each step done correctly.")

    def test_edge_2560x1440(self):
        driver = self.driver
        driver.set_window_size(2560, 1440)
        driver.get("https://qasvus.wordpress.com")
        try:
            assert "California Real Estate" in driver.title
        except AssertionError:
            print("Driver title in Chrome is:", driver.title)

        try:
            driver.find_element(By.XPATH, '//*[@value="Close and accept"]').click()
        except NoSuchElementException:
            print("No 'Close and accept' appear")

        driver.find_element(By.XPATH, '//*[text()="Send Us a Message"]')
        nameField = driver.find_element(By.ID, 'g2-name')
        nameField.clear()
        nameField.send_keys(faker_class.name())

        driver.find_element(By.NAME, 'g2-email')
        emailField = driver.find_element(By.ID, 'g2-email')
        emailField.clear()
        emailField.send_keys(faker_class.email())

        driver.find_element(By.ID, 'contact-form-comment-g2-message')
        textField = driver.find_element(By.ID, 'contact-form-comment-g2-message')
        textField.clear()
        textField.send_keys(faker_class.text())

        time.sleep(5)
        driver.find_element(By.CLASS_NAME, 'pushbutton-wide').click()

        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Go back')]")))

        driver.find_element(By.XPATH, "//a[contains(text(),'Go back')]").send_keys('\n')
        print(driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").get_attribute("type"))

        time.sleep(2)
        assert "California Real Estate" in driver.title
        print("Testing page has", driver.title + "as Page title. Test complete and each step done correctly.")

    def test_edge_1920x1080(self):
        driver = self.driver
        driver.set_window_size(1920, 1080)
        driver.get("https://qasvus.wordpress.com")
        try:
            assert "California Real Estate" in driver.title
        except AssertionError:
            print("Driver title in Chrome is:", driver.title)

        try:
            driver.find_element(By.XPATH, '//*[@value="Close and accept"]').click()
        except NoSuchElementException:
            print("No 'Close and accept' appear")

        driver.find_element(By.XPATH, '//*[text()="Send Us a Message"]')
        nameField = driver.find_element(By.ID, 'g2-name')
        nameField.clear()
        nameField.send_keys(faker_class.name())

        driver.find_element(By.NAME, 'g2-email')
        emailField = driver.find_element(By.ID, 'g2-email')
        emailField.clear()
        emailField.send_keys(faker_class.email())

        driver.find_element(By.ID, 'contact-form-comment-g2-message')
        textField = driver.find_element(By.ID, 'contact-form-comment-g2-message')
        textField.clear()
        textField.send_keys(faker_class.text())

        time.sleep(5)
        driver.find_element(By.CLASS_NAME, 'pushbutton-wide').click()

        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Go back')]")))

        driver.find_element(By.XPATH, "//a[contains(text(),'Go back')]").send_keys('\n')
        print(driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").get_attribute("type"))

        time.sleep(2)
        assert "California Real Estate" in driver.title
        print("Testing page has", driver.title + "as Page title. Test complete and each step done correctly.")

    def tearDown(self):
        self.driver.quit()