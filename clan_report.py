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

    if clan.currentwar:
        print(clan.currentwar)
        print("-" * 20)
        yesno = input("Would you like to save war to the database?: Y | n")
        if yesno.lower() == 'y':
            clan.save_war_to_db()
        else:
            print("War not saved to database.")
    
    print("Ending Program.")

if __name__ == "__main__":
    main()