from get_clan_info import get_clan_info
from get_player_info import get_player_info

import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import seaborn as sns
from matplotlib.colors import Normalize

hero_max_levels = {
    'Barbarian King': 100,
    'Archer Queen': 100,
    'Grand Warden': 75,
    'Royal Champion': 50,
    'Minion Prince': 90
}

def create_townhall_histogram(our_clan_th_levels, enemy_clan_th_levels, clan_tag, png_directory = 'png'):

    plt.figure(figsize=(12, 6))

    townhall_levels = range(1, 18)

    our_th_counts = {level: our_clan_th_levels.count(level) for level in townhall_levels}
    enemy_th_counts = {level: enemy_clan_th_levels.count(level) for level in townhall_levels}

    bar_width = 0.35
    x = np.arange(len(townhall_levels))

    plt.bar(x - bar_width/2, our_th_counts.values(), color='red', width=bar_width, label='Our Clan')
    plt.bar(x + bar_width/2, enemy_th_counts.values(), color='blue', width=bar_width, label='Enemy Clan')

    plt.xlabel("Townhall Level")
    plt.ylabel("Number of Members")
    plt.title(f"Townhall Level Distribution - Our Clan vs. Enemy Clan ({clan_tag})")

    plt.xticks(x, townhall_levels)
    plt.xlim(x[0] - 1, x[-1] + 1)

    plt.legend()
    plt.tight_layout()

    image_path = os.path.join(png_directory, f"townhall_histogram_{clan_tag}_comparison.png")
    plt.savefig(image_path)

    print(f"Image saved to {image_path}")

    plt.close()

def create_hero_heatmap(clan_relatives, clan_tag, is_opponent=False, png_directory = 'png'):
    hero_data = []
    member_names = []
    for player_data in clan_relatives:
        member_name = player_data.get('player_name')
        member_names.append(member_name)
        hero_info = {k: v for k, v in player_data.items() if k != 'player_name'}
        hero_data.append(hero_info)

    hero_df = pd.DataFrame(hero_data, index=member_names)

    if not hero_df.empty:
        norm = Normalize(vmin=0, vmax=1)
        plt.figure(figsize = (12, 8))
        sns.heatmap(hero_df, annot=True, cmap="YlGnBu", fmt=".2f", vmin=0,vmax=1,norm=norm)
        plt.title(f"Relative Hero Levels Heatmap - {clan_tag} ({'opponent' if is_opponent else 'Clan'})")
        plt.xlabel("Hero")
        plt.ylabel("Player")

        image_path = os.path.join(png_directory, f"relative_hero_heatmap_{clan_tag}_{'opponent' if is_opponent else 'clan'}.png")
        plt.savefig(image_path)

        print(f"Image save to {image_path}")

        plt.close

    else:
        print(f"No hero data found for clan {clan_tag} to create hero heatmap.")

def calculate_relative_hero_levels(player_hero_data):
    player_name = player_hero_data.get('player_name', 'Unknown Player')
    relative_hero_levels = {'player_name': player_name}

    for hero_name, hero_level in player_hero_data.items():
        if hero_name != 'player_name':
            max_level = hero_max_levels.get(hero_name)
            if max_level:
                relative_level = hero_level / max_level
                relative_hero_levels[hero_name] = relative_level

    return relative_hero_levels

def main():
    clan_id = input("Enter Clan ID: ")

    clan = get_clan_info(clan_id)

    if clan.currentwar:
        our_clan = clan.currentwar.clan.clan_members_data
        enemy_clan = clan.currentwar.opponent.clan_members_data

        opponent_clan_tag = clan.currentwar.opponent.get_tag()

        our_clan_heroes = []
        our_clan_th_levels = []

        enemy_clan_heroes = []
        enemy_clan_th_levels = []

        for member in our_clan:
            player = get_player_info(member.get_tag())
            if player.heroes:
                player_hero_info = {"player_name": member.get_name()}
                player_th_level = member.get_townhallLevel()
                if player_th_level:
                    our_clan_th_levels.append(player_th_level)
                for hero in player.heroes:
                    if hero.get_village() == 'home':
                        hero_name = hero.get_name()
                        hero_level = hero.get_level()
                        player_hero_info[hero_name] = hero_level

                our_clan_heroes.append(calculate_relative_hero_levels(player_hero_info))

        for member in enemy_clan:
            player = get_player_info(member.get_tag())
            if player.heroes:
                player_hero_info = {"player_name": member.get_name()}
                player_th_level = member.get_townhallLevel()
                if player_th_level:
                    enemy_clan_th_levels.append(player_th_level)
                for hero in player.heroes:
                    if hero.get_village() == 'home':
                        hero_name = hero.get_name()
                        hero_level = hero.get_level()
                        player_hero_info[hero_name] = hero_level

                enemy_clan_heroes.append(calculate_relative_hero_levels(player_hero_info))

        create_townhall_histogram(our_clan_th_levels, enemy_clan_th_levels, opponent_clan_tag)

        create_hero_heatmap(our_clan_heroes, clan_id)
        create_hero_heatmap(enemy_clan_heroes, opponent_clan_tag, is_opponent=True)

if __name__ == "__main__":
    main()