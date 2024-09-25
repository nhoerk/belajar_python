import requests


def kirim_telegram(bot_token, chat_id, message):
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