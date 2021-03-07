# Note that you can also hardcode the values for personal use.
u = input("Username bataiye: ") #username
p = input("Password bataiye: ") #password

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://moodle.iitd.ac.in/")
text = driver.find_element_by_id("login").text

#'a' is used to store the type captcha 
a = 0
if text[51:58] == "enter f":
    a = 1
if text[51:58] == "enter s":
    a = 2
if text[51] == "a":
    a = 3
if text[51] == "s":
    a = 4

# 'b' will store the answer to the captcha
b = 0

if a == 1:
    text = text[69:]
    index = text.index(" ")
    b = int(text[:index])
    
if a == 2:
    index = text.index(",")
    text = text[index + 2:]
    index = text.index(" ")
    b = int(text[:index])

if a == 3:
    text = text[55:]
    index = text.index(" ")
    b = int(text[:index])
    text = text[index+3:]
    index = text.index(" ")
    b += int(text[:index])

if a == 4:
    text = text[60:]
    index = text.index(" ")
    b = int(text[:index])
    text = text[index+3:]
    index = text.index(" ")
    b -= int(text[:index])

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
captcha = driver.find_element_by_id("valuepkg3")

username.send_keys(u)
password.send_keys(p)
captcha.clear()
captcha.send_keys(b)
captcha.send_keys(Keys.RETURN)

print(a)
print(b)
