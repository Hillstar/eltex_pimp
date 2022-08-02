import requests
import random
from bs4 import BeautifulSoup

MAX_TRY_NUM = 100
ERROR_RESPONSE = 404
OK_RESPONSE = 200

#target_url = "https://oda.sibirki.su/id_8343.html"
SLUT_PAGE_TEMPLATE = "https://oda.sibirki.su/id_"

def Download():
    try_num = 0
    while try_num < MAX_TRY_NUM:
        slut_id = str(random.randint(7000, 9000))
        target_url = SLUT_PAGE_TEMPLATE + slut_id + ".html"
        response = requests.get(target_url)
        if response.status_code == OK_RESPONSE:
            html_page = BeautifulSoup(response.text, 'html.parser')
            description = html_page.find("div", {"class": "textaboutcard"}).contents[0]
            if "не указано" not in description:
                return description
        try_num += 1

    else:
        return ""