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
password.send_keys('NA498bli')


#Получаем указатель на кнопку "Войти", привязываемся к элементу через его css_selector
button=browser.find_element(by=By.CSS_SELECTOR, value='#login-button')
#Нажимаем на кнопку входа
button.click()

# Проверка результата
try:
    # Проверка что пользователь находится на странице авторизации
    assert 'Spotify' in browser.title
    errormessage=browser.find_element(by=By.CSS_SELECTOR(".Wrapper-sc-62m9tu-0.dupjdh.encore-negative-set.sc-bqiRlB.hdPVpG"))
    # Проверка сообщения об ошибке на странице
    assert 'Неправильное имя пользователя или пароль.' in errormessage.accessible_name
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')


browser.close()