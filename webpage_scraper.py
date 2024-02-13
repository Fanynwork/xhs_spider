import requests
from utils import *


def get_headers():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"    }

    return headers


def get_html(url, headers, method="get"):
    if method == "get":
        html = requests.get(url, headers=headers).content.decode("utf-8")
    else:
        html = requests.post(url, headers=headers).content.decode("utf-8")
    return html
