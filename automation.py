# from selenium import webdriver

# chrome_browser = webdriver.Chrome('./chromedriver')

# print(chrome_browser)


import os
resp =os.walk("C:\\Desktop\\python\\hydra.py")
d1= {}
for r,d,f in resp:
  for file in f:
    d1[file]= r
#print (d1)
file_name = input("Enter the file name ")
for k,v in d1.items():
  if file_name.lower() in k.lower() :
    print (k,":", v)