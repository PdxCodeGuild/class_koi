'''
- start_zoom.py opens the class_koi zoom web link and
  clicks the button that initializes zoom

Selenium Resources:
- https://www.selenium.dev/documentation/webdriver/getting_started/
- https://pypi.org/project/selenium/

'''

from selenium import webdriver # had to pip install selenium
import time

zoom_driver = webdriver.Safari() # establish a second driver for zoom
zoom_driver.get('https://us06web.zoom.us/j/88298957445')

time.sleep(3)

zoom_driver.switch_to.alert.accept()

# zoom will start and you can click Join With Video
