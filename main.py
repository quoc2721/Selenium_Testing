# Code dùng để đăng nhập
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://pvc-ch16-deployment.herokuapp.com/")

log_in_button = driver.find_element(By.CSS_SELECTOR, 'a[href="/accounts/login/"]')
log_in_button.click()

user_input = driver.find_element(By.NAME, "username")
user_input.send_keys("demo")

password_input = driver.find_element(By.NAME, "password")
password_input.send_keys("cuongvip007")

login_button = driver.find_element(By.XPATH, "/html/body/main/div/form/button")
login_button.click()


time.sleep(2)
driver.quit()




# Code thứ 2 dùng để đăng lý và hiển thị error
# import time
# import unittest
# from selenium import webdriver
# import page
# from selenium.webdriver.common.by import By
#
#
# class GoogleSearch(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get("https://pvc-ch16-deployment.herokuapp.com/accounts/signup/")
#
#     def test_title_google(self):
#         sign_up_input = self.driver.find_element(By.NAME, "username")
#         sign_up_input.send_keys("$$$$")
#
#         password_input = self.driver.find_element(By.NAME, "password1")
#         password_input.send_keys("cuongvip007")
#
#         confirm_password_input = self.driver.find_element(By.NAME, "password2")
#         confirm_password_input.send_keys("cuongvip007")
#
#         sign_up_button = self.driver.find_element(By.XPATH, "/html/body/main/div/form/button")
#         sign_up_button.click()
#
#         time.sleep(3)
#
#         error_label = self.driver.find_element(By.ID, "error_1_id_username")
#         error_text = error_label.text
#
#         print(error_text)
#         self.assertEqual(error_text, "Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.")
#
#
#
#
#     # def test_login(self):
#     #     pass
#
#     def tearDown(self):
#         self.driver.close()
#
# if __name__ == "__main__":
#     unittest.main()