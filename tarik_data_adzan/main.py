import requests
from http.cookies import SimpleCookie
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

bot_token = '7411994949:AAF4SUEzuLTyyf_qS4eTSUDBJsvK6p3G2D0'
chat_id = ''

def kirim_telegram(bot_token, chat_id):
    url = f'https://api.telegram.org/bot{bot_token}/getUpdates'
    response = requests.get(url)
    # Print status code and response
    # print('Status Code:', response.status_code)
    # print('Response:', response.json())

    response = requests.get(url)
    data = response.json()

    # Cek apakah respons OK dan ada hasil
    if data['ok'] and data['result']:
        # Ambil data id dari respons
        chat_id = data['result'][0]['message']['chat']['id']

    
    # URL API Telegram
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'


    # Pesan yang akan dikirim
    message = f"""
    *JADWAL SHALAT*
    *Wilayah DKI Jakarta & Sekitarnya*
    *{times['tanggal']} M*
    
    SUBUH     : {times['subuh']}
    TERBIT      : {times['terbit']}
    DHUHA    : {times['dhuha']}
    DZUHUR   : {times['dzuhur']}
    ASAR        : {times['ashar']}
    MAGHRIB : {times['maghrib']}
    ISYA          : {times['isya']}
    """

    # Parameter yang dikirim ke API
    params = {
        'chat_id': chat_id,
        'text': message
    }

    # Mengirim permintaan POST
    response = requests.post(url, params=params)

    # Mengecek status respons
    if response.status_code == 200:
        print('Message sent successfully!')
    else:
        print('Failed to send message:', response.text)


def kirim_wa():
    # Path ke chromedriver
    driver_path = 'path/to/chromedriver'

    # Inisialisasi WebDriver
    driver = webdriver.Chrome(driver_path)

    # Buka WhatsApp Web
    driver.get('https://web.whatsapp.com')

    # Tunggu beberapa detik agar QR Code muncul dan bisa dipindai
    input("Scan QR Code and press Enter here...")

    # Temukan kontak
    contact_name = 'Nama Kontak'  # Ganti dengan nama kontak atau grup
    message = 'Hello, this is a message from Python!'  # Pesan yang ingin dikirim

    # Temukan elemen input chat dan kirim pesan
    try:
        # Cari dan klik pada nama kontak
        search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
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



# Function to get PHPSESSID from the header of the response
def get_session() -> str:
    url = 'https://bimasislam.kemenag.go.id/jadwalshalat'
    
    # Sending a HEAD request to fetch only headers
    response = requests.head(url)
    
    # Extract cookies from headers
    cookies = response.headers.get('Set-Cookie')
    
    # Parse the cookies using SimpleCookie
    cookie = SimpleCookie()
    cookie.load(cookies)
    
    # Return the PHPSESSID value
    return cookie['PHPSESSID'].value

# Function to search for cities based on the province ID
def search_city(province_id: str) -> list:
    php_session_id = get_session()
    url = 'https://bimasislam.kemenag.go.id/ajax/getKabkoshalat'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': f'PHPSESSID={php_session_id}'
    }
    data = {
        'x': province_id
    }
    
    response = requests.post(url, data=data, headers=headers)
    result = []
    
    # Regex pattern to extract option values and names
    import re
    regex = r'(<option value="(.*?)">(.*?)<\/option>)'
    matches = re.finditer(regex, response.text)
    
    for match in matches:
        temp = {'id': match.group(2), 'name': match.group(3).lower()}
        result.append(temp)
    
    return result

# Function to search for prayer times
def search_pray_time(province_id: str, city_id: str, month: str, year: str) -> list:
    php_session_id = get_session()
    url = 'https://bimasislam.kemenag.go.id/ajax/getShalatbln'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': f'PHPSESSID={php_session_id}'
    }
    data = {
        'x': province_id,
        'y': city_id,
        'bln': month,
        'thn': year
    }
    
    response = requests.post(url, data=data, headers=headers)
    
    result = []
    
    if 'data' not in response.json():
        return result
    
    data_keys = response.json()['data'].keys()
    
    for key in data_keys:
        pray_time = {'key': key, **response.json()['data'][key]}
        result.append(pray_time)
    
    return result

# Example usage
province_id = "c51ce410c124a10e0db5e4b97fc2af39"
city_id = "58a2fc6ed39fd083f55d4182bf88826d"
month = 9  # September
year = 2024

# cities = search_city(province_id)
# print(cities)

pray_times = search_pray_time(province_id, city_id, month, year)

for times in pray_times:
    now = datetime.datetime.now()
    date_today = f"{now.year}-{str(now.month).zfill(2)}-{str(now.day).zfill(2)}"
    # print(times['key'], date_today)
    if times['key'] == date_today:
        print("*JADWAL SHALAT*")
        print("*Wilayah DKI Jakarta & Sekitarnya*")
        print(f"*{times['tanggal']} M*")
        print("")
        print(f"SUBUH     : {times['subuh']}")
        print(f"TERBIT      : {times['terbit']}")
        print(f"DHUHA    : {times['dhuha']}")
        print(f"DZUHUR   : {times['dzuhur']}")
        print(f"ASAR        : {times['ashar']}")
        print(f"MAGHRIB : {times['maghrib']}")
        print(f"ISYA          : {times['isya']}")
        kirim_telegram(bot_token, chat_id)