from get_player_info import get_player_info

def main():
    player_id = input("Enter Player ID: ")

    player = get_player_info(player_id)

    if player.player:
        print(player.player)
        print("-" * 20)
    # if player.achievements:
    #     for achievement in player.achievements:
    #         print(achievement)
    #         print("-" * 20)
    if player.heroes:
        for hero in player.heroes:
            print(hero)
            print("-" * 20)
    if player.troops:
        for troop in player.troops:
            print(troop)
            print("-" * 20)
    if player.spells:
        for spell in player.spells:
            print(spell)
            print("-" * 20)
    if player.clan:
        print(player.clan)
        print("-" * 20)

if __name__ == "__main__":
    main()