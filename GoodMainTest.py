import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker

fake = Faker()
# Open URL qasvus.wordpress.com in Crome
driver = webdriver.Chrome()
driver.get("https://qasvus.wordpress.com/")
driver.maximize_window()
# wait 2 sec, then proceed with script
time.sleep(2)
assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
print("Title is Correct. Current Title is:", driver.title)
# Find "Send Us a Message" text on the webpage
driver.find_element(By.ID, "send-us-a-message").is_displayed()
# Close some ad
driver.find_element(By.XPATH, '//*[@id="bottom-sticky__ad-container"]/div[1]').click()
# Fill out and send the message form
driver.find_element(By.ID, "g2-name").send_keys(fake.name())
driver.find_element(By.ID, "g2-email").send_keys(fake.email())
driver.find_element(By.XPATH, "//*[@name='g2-message']").send_keys(fake.text())
submit = driver.find_element(By.XPATH, "//button[contains(.,'Submit')]")
submit.click()
# Find "go back" button (link) and go back to the Main page.
driver.find_element(By.LINK_TEXT, "Go back").click()
time.sleep(2)
# Once you'll get the Main page, verify it by finding and print "type" for "Submit" button
print(type(submit))
# quit from Chrome browser
driver.quit()