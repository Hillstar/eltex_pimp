import requests
import random
from bs4 import BeautifulSoup

MAX_TRY_NUM = 100

ELTEX_XPON_URL = "http://eltex.loc/index.php?option=com_qcontacts&view=category&catid=12&Itemid=15"

def Download():
    try_num = 0
    while try_num < 100:
        response = requests.get(ELTEX_XPON_URL)
        html_page = BeautifulSoup(response.text, 'html.parser')
        elems = html_page.find_all("a", {"class": "category"})
        elem = random.choice(elems)
        if "ОТДЕЛ" not in elem.text and "Группа" not in elem.text:
            return elem.attrs['href']
        else:
            try_num += 1
    return ""