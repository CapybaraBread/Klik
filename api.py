import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()

token = os.environ['TOKEN']


def shorten_link(token, url_from_user):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    headers ={
    "Authorization": f"Bearer {token}"
}
    data = { "long_url": url_from_user}
    data=json.dumps(data)
    response = requests.post(url, headers=headers, data=data)
    data = json.loads(response.text)

    if response.status_code / 100!=2:
         print("Перепроверьте правильность ссылки")
    return data["link"]

def count_clicks(token, url_from_user):
    url_from_user_2 = url_from_user.strip('https://')
    print(url_from_user_2)
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{url_from_user_2}/clicks'
    headers ={
    "Authorization": f"Bearer {token}"
}
    data = { "units": 1}
    data=json.dumps(data)
    response = requests.get(url, headers=headers, params=data)
    data = json.loads(response.text)
    clicks_count = 0
    for cliks in data["link_clicks"]:
        if cliks["clicks"] == 1:
            clicks_count = +1
    return clicks_count


def is_bitlink(url_long):
    if url_from_user.split('/')[2] == "bit.ly":
        clicks = count_clicks(token, url_from_user)
        return clicks
    else:
        short_link = shorten_link(token,url_long)
        return short_link

if __name__ == "__main__":
    url_from_user=input("Введите текст: ")
    print(is_bitlink(url_from_user))