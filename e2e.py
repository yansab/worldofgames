from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


def test_scores_service(app_url):
    res = False
    driver = webdriver.Chrome()  # (service=ChromeService(ChromeDriverManager().install()))
    driver.get(app_url)
    score_element = driver.find_element(By.XPATH, '//*[@id="score"]')
    print(score_element.text)
    if score_element.text == 'ERROR':
        return res
    if 0 < int(score_element.text) < 1001:
        res = True
        print(f'The score is between 1 - 1000, the current score is :{score_element.text}')
    else:
        print(f'The score IS NOT between 1 - 1000, the current score is :{score_element.text}')
    return res


def main_function():
    test_res = -1
    res = test_scores_service('http://127.0.0.1:5000')
    if res:
        test_res = 0
    return test_res


test_res = main_function()
if test_res == 0 :
    print('Test passed successfully -:)')
else:
    print('Test Failed :-(')

