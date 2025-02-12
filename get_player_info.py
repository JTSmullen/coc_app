import requests
import os

from player_utils import heroes_utils
from player_utils import troops_utils
from player_utils import spells_utils
from player_utils import basic_player_info_utils
from player_utils import achievements_utils
from player_utils import clan_utils

API_TOKEN = os.environ.get("grove_city_coc_key")

class get_player_info():
    def __init__(self, player_tag):
        self.data = self.get_info(player_tag)
        if self.data:
            self.player = basic_player_info_utils.Basic_Player_Info(self.data)
            self.achievements = self.process_achievements()
            self.heroes = self.process_heroes()
            self.troops = self.process_troops()
            self.spells = self.process_spells()
            self.clan = self.process_clan()
        else:
            self.player = None
            self.achievements = None
            self.heroes = None
            self.troops = None
            self.spells = None
            self.clan = None

    def get_info(self, player_tag):
        headers = {
            "Authorization": f"Bearer {API_TOKEN}"
        }

        url = f"https://api.clashofclans.com/v1/players/{player_tag.replace('#', '%23')}"

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()

            if data:
                return data

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    def process_achievements(self):
        if self.data is None:
            return None

        achievement_data_list = self.data.get('achievements', [])

        achievements = []
        for achievement_data in achievement_data_list:
            achievement = achievements_utils.Achievements(achievement_data)
            achievements.append(achievement)
        return achievements

    def process_heroes(self):
        if self.data is None:
            return None

        hero_data_list = self.data.get('heroes', [])
        heroes = []
        for hero_data in hero_data_list:
            hero = heroes_utils.Hero(hero_data)
            heroes.append(hero)
        return heroes

    def process_troops(self):
        if self.data is None:
            return None

        troop_data_list = self.data.get('troops', [])

        troops = []

        for troop_data in troop_data_list:
            troop = troops_utils.Troop(troop_data)
            troops.append(troop)
        return troops

    def process_spells(self):
        if self.data is None:
            return None

        spell_data_list = self.data.get('spells', [])

        spells = []

        for spell_data in spell_data_list:
            spell = spells_utils.Spell(spell_data)
            spells.append(spell)
        return spells

    def process_clan(self):
        if self.data is None:
            return None

        clan_data = self.data.get('clan', [])

        clan = clan_utils.Clan(clan_data)
        return clan