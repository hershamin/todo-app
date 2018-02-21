import os
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


# Check if test db is running
r = requests.get('http://localhost:8080/api/v1/db')
dbName = r.json()['name']
assert 'test' in dbName


# Run web driver
dirPath = os.getcwd()
driver = webdriver.Chrome(dirPath + '/tests/chromedriver-mac')
driver.implicitly_wait(5) # Retry for 5 seconds to find any element
wait = WebDriverWait(driver, 5) # Explicit wait for 5 seconds if needed
driver.get('http://localhost:8000/')
assert 'ToDo App' in driver.title
assert 'login' in driver.current_url


# Sign up account
elem = driver.find_element_by_css_selector('a[ui-sref="signup"]')
elem.click() # go to page
# Enter info
elem = driver.find_element_by_css_selector('input[ng-model="firstName"]')
elem.send_keys('First Name')
assert 'signup' in driver.current_url
elem = driver.find_element_by_css_selector('input[ng-model="lastName"]')
elem.send_keys('Last Name')
elem = driver.find_element_by_css_selector('input[ng-model="email"]')
elem.send_keys('info@example.com')
elem = driver.find_element_by_css_selector('input[ng-model="password"]')
elem.send_keys('password')
# Click create account
elem = driver.find_element_by_css_selector('button[ng-click="signup()"]')
elem.click()


# Logout from account page
elem = driver.find_element_by_css_selector('button[ng-click="logout()"]')
assert 'home' in driver.current_url
elem.click()
driver.find_element_by_css_selector('a[ui-sref="signup"]')


# Sign in to account
assert 'login' in driver.current_url
# Enter info
elem = driver.find_element_by_css_selector('input[ng-model="email"]')
elem.send_keys('info@example.com')
elem = driver.find_element_by_css_selector('input[ng-model="password"]')
elem.send_keys('password')
# Click Sign in
elem = driver.find_element_by_css_selector('button[ng-click="login()"]')
elem.click()


# Create Task in account page
taskTitle = 'Task title for test'
taskDesc = 'Task description, pretty long odescription, as muchas your heart desires, cat typing...'
driver.find_element_by_css_selector('button[ng-click="logout()"]')
assert 'home' in driver.current_url
# Open create task modal
elem = driver.find_element_by_css_selector('button[ng-click="addDialog()"]')
elem.click()
# Enter task information
elem = driver.find_element_by_css_selector('input[ng-model="currentTask.title"]')
elem.send_keys(taskTitle)
time.sleep(3)
elem = driver.find_element_by_css_selector('input[ng-model="currentTask.description"]')
elem.send_keys(taskDesc)
time.sleep(3)
# Select priority
elem = driver.find_element_by_css_selector('md-select[ng-model="currentTask.priority"]')
elem.click()
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'md-option[ng-repeat="priorityOption in priorityOptions"]')))
elems = driver.find_elements_by_css_selector('md-option[ng-repeat="priorityOption in priorityOptions"]')
for el in elems:
    if 'Medium' in el.text:
        el.click()
# Save task
wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'md-option[ng-repeat="priorityOption in priorityOptions"]')))
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ng-click="saveTask()"]')))
elem = driver.find_element_by_css_selector('button[ng-click="saveTask()"]')
elem.click()


# Verify task exists
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'md-list-item[ng-repeat="task in tasks"]')))
elem = driver.find_element_by_css_selector('md-list-item[ng-repeat="task in tasks"]')
assert taskTitle in elem.text
assert taskDesc in elem.text
assert 'Medium' in elem.text


# Change task priority
elem = driver.find_element_by_css_selector('md-select[ng-model="task.priority"]')
elem.click()
time.sleep(3)
elems = driver.find_elements_by_css_selector('md-option[ng-repeat="priorityOption in priorityOptions"]')
for el in elems:
    if 'High' in el.text:
        el.click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'md-list-item[ng-repeat="task in tasks"]')))
elem = driver.find_element_by_css_selector('md-list-item[ng-repeat="task in tasks"]')
assert 'High' in elem.text


# Mark task as complete
elem = driver.find_element_by_css_selector('md-checkbox[ng-model="task.status"]')
elem.click()
time.sleep(3)
# Check if clickable
elem = driver.find_element_by_css_selector('md-checkbox[ng-model="task.status"]')
assert 'true' in elem.get_attribute('aria-disabled')
elem = driver.find_element_by_css_selector('md-select[ng-model="task.priority"]')
assert 'true' in elem.get_attribute('aria-disabled')


# Delete task
elem = driver.find_element_by_css_selector('button[ng-click="deleteTask(task.id, task.title)"]')
elem.click()
time.sleep(3)
elem = driver.find_element_by_css_selector('button[ng-click="dialog.hide()"]')
elem.click()
time.sleep(3)
# Make sure there are no tasks
try:
    driver.find_element_by_css_selector('md-list-item[ng-repeat="task in tasks"]')
    print 'no task should not exist'
    assert True == False
except NoSuchElementException:
    pass


# Logout from account page
elem = driver.find_element_by_css_selector('button[ng-click="logout()"]')
elem.click()
driver.find_element_by_css_selector('a[ui-sref="signup"]')
assert 'login' in driver.current_url


# Close
print '========== SUCCESS ========='
time.sleep(5)
driver.close()
