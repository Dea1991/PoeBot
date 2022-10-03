import requests


def check_price_div():
    url = "https://poe.ninja/challenge/currency/divine-orb/html/body/div[3]/section/div/main/section/div/div/div[2]/div[1]/div[1]/div/span[3]/div/span"
    r = requests.get(url)
    price_div = str(r)[11:14]
    return price_div



