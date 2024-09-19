from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pickle

options = Options()
# options.add_argument("--headless")
driver_path = 'belajar_python/tarik_data_adzan/chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=Service(), options=options)
# driver.get('https://web.whatsapp.com')

# Tunggu beberapa detik untuk pemindaian barcode
time.sleep(15)  # Waktu untuk scan barcode

CONTACT_NAME = 'Muhammad Nur Joharis'

def kirim_wa(args):
    contact_name, message = args
    pickle.dump(driver.get_cookies(), open("whatsapp_cookies.pkl", "wb"))
    driver.get('https://web.whatsapp.com')
    cookies = pickle.load(open("whatsapp_cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    # Temukan elemen input chat dan kirim pesan
    
    driver.refresh()
    try:
        # Cari dan klik pada nama kontak
        search_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p')
        search_box.click()
        search_box.send_keys(contact_name)
        search_box.send_keys(Keys.RETURN)
        
        # Tunggu beberapa detik agar chat terbuka
        time.sleep(2)
        
        # Temukan dan klik elemen input pesan
        message_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="6"]')
        message_box.click()
        message_box.send_keys(message)
        message_box.send_keys(Keys.RETURN)
        
        print("Message sent successfully!")
    finally:
        # Tutup browser setelah beberapa detik
        time.sleep(5)
        driver.quit()


message = 'test'
kirim_wa((CONTACT_NAME, message))