from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver.exe')

chrome_browser.maximize_browser()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')


