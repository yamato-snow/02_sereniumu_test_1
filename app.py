import time                            # スリープを使うために必要
import os
import signal
from selenium import webdriver         # Webブラウザを自動操作する（python -m pip install selenium)
 
driver = webdriver.Chrome()            # Chromeを準備

try:
    driver.get('https://www.google.com/')  # Googleを開く
    time.sleep(5)                          # 5秒間待機
finally:
    os.kill(driver.service.process.pid,signal.SIGTERM)