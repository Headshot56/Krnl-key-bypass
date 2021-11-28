from selenium import webdriver
import keyboard, sys
url = "https://cdn.krnl.ca/getkey.php"
browser = webdriver.Chrome()
browser.get(url)
browser.find_element_by_xpath("//*[@id='choice']/div/div/form/div/input").click()
keyboard.press_and_release("ctrl+a")
keyboard.press_and_release("ctrl+c")
browser.close()