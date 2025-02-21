import requests
import os

from clan_utils import basic_clan_info_utils
from clan_utils.warlog_utils import basic_warlog_info_utils
from clan_utils.war_utils import basic_war_info

API_TOKEN = os.environ.get("grove_city_coc_key")

class get_clan_info():
    def __init__(self, clan_tag):
        self.data = self.get_info(clan_tag)
        self.currentwar_data = self.get_currentwar_info(clan_tag)
        if self.data:
            self.clan = basic_clan_info_utils.Basic_Clan_Info(self.data)
            if self.clan.get_isWarLogPublic():
                self.warlog_data = self.get_warlog_info(clan_tag)
                if self.warlog_data:
                    self.warlog = self.process_warlog_basic()
        else:
            self.clan = None
        if self.currentwar_data:
            self.currentwar = basic_war_info.basic_war_info(self.currentwar_data)

    def save_war_to_db(self):
        if self.currentwar:
            self.currentwar.save_to_db()

    def get_info(self, clan_tag):
        headers = {
            "Authorization": f"Bearer {API_TOKEN}"
        }

        url = f"https://api.clashofclans.com/v1/clans/{clan_tag.replace('#', '%23')}"

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()

            if data:
                return data
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    def get_warlog_info(self, clan_tag):
        headers = {
            "Authorization": f"Bearer {API_TOKEN}"
        }

        url = f"https://api.clashofclans.com/v1/clans/{clan_tag.replace('#', '%23')}/warlog"

        try:
            response = requests.get(url, headers = headers)
            response.raise_for_status()
            data = response.json()

            if data:
                return data
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None
        
    def get_currentwar_info(self, clan_tag):
        headers = {
            "Authorization": f"Bearer {API_TOKEN}"
        }

        url = f"https://api.clashofclans.com/v1/clans/{clan_tag.replace('#', '%23')}/currentwar"

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()

            if data:
                return data

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    def process_warlog_basic(self):
        if self.warlog_data is None:
            return None

        warlog_list = self.warlog_data.get('items', [])

        warlog_info_list = []

        for warlog_entry in warlog_list:
            warlog_info = basic_warlog_info_utils.Basic_Warlog_Info(warlog_entry)
            warlog_info_list.append(warlog_info)

        return warlog_info_list