from get_clan_info import get_clan_info

def main():
    clan_id = input("Enter Clan ID: ")

    clan = get_clan_info(clan_id)

    if clan.clan:
        print(clan.clan)
        print("-" * 20)

    if clan.warlog:
        for war in clan.warlog:
            print(war)
            print("-" * 20)

if __name__ == "__main__":
    main()