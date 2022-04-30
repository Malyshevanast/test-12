from selenium import webdriver
from selenium.webdriver.common.by import By

 # Получаем в переменную browser указатель на браузер
browser=webdriver.Chrome()

# Переходим на страницу, на которой находится форма для авторизации
browser.get('https://accounts.spotify.com/ru/login?continue=https%3A%2F%2Fopen.spotify.com%2Fcollection%2Fplaylists')

# заполняем поле логин, привязываемся к элементу через его id
username=browser.find_element(by=By.ID, value='login-username')
username.send_keys('malishevant2003@mail.ru')

# заполняем поле пароля, привязываемся к элементу через его id
password=browser.find_element(by=By.ID, value='login-password')
password.send_keys('135Y79PRIVET')


#Получаем указатель на кнопку "Войти", привязываемся к элементу через его css_selector
button=browser.find_element(by=By.CSS_SELECTOR, value='#login-button')
#Нажимаем на кнопку входа
button.click()

try:
    # Проверка что пользователь находится на главной странице сайта
    assert 'Spotify: Плейлисты' in browser.title
    # Проверка что на странице присутствует имя пользователя и все его плейлисты
    assert "<Имя пользователя Плейлисты>" in browser.page_source
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')

browser.close()