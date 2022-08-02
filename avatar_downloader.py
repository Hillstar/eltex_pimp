import requests
from bs4 import BeautifulSoup
import random_person as RP

# target_url = "http://eltex.loc/index.php?option=com_qcontacts&view=contact&id=1740%3A2019-11-06-09-44-26&catid=12%3A-4-xpon&Itemid=15"
ELTEX_URL = "http://eltex.loc/"


def Download():
    person_url = RP.Download()
    target_url = ELTEX_URL + person_url
    response = requests.get(target_url)
    html_page = BeautifulSoup(response.text, 'html.parser')
    images = html_page.find_all('img')

    for image in enumerate(images):
        image_url = image[1].get("src")      # img src value

        if "stories" not in image_url:    # avatar url contains 'stories'
            continue
        
        image_extension = image_url.split(".")[-1]       # get image extension
        image_url = ELTEX_URL + image_url

        # get image data
        image_bytes = requests.get(image_url).content
        
        if image_bytes:
            # write the image data
            file_name = f"avatar.{image_extension}"
            with open(file_name, "wb") as file:
                file.write(image_bytes)
            return file_name