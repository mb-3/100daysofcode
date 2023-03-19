import requests
from bs4 import BeautifulSoup


class BBDataManager:

    def get_data(self, date):

        url = f"https://www.billboard.com/charts/hot-100/{date}/"
        response = requests.get(url)
        webpage_text = response.text
        soup = BeautifulSoup(webpage_text, 'html.parser')
        song_list = soup.findAll(name="li", class_="lrv-u-padding-l-1@mobile-max")
        track_list = [i.find("h3").getText().strip() for i in song_list]
        return track_list
