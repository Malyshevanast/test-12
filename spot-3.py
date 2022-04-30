from selenium import webdriver
from selenium.webdriver.common.by import By

browser=webdriver.Chrome()

# Переходим на страницу, на которой находится форма для авторизации
browser.get('https://accounts.spotify.com/ru/login?continue=https%3A%2F%2Fopen.spotify.com%2Fcollection%2Fplaylists')

# заходим посредством Facebook
button=browser.find_element(by=By.CLASS_NAME, value='Button-y0gtbx-0.hpTULc.sc-fFeiMQ.kiLgbd')

#Нажимаем на кнопку Facebook
button.click()

browser.close()