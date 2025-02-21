from datetime import datetime, timezone, timedelta

class basic_war_info():
    def __init__(self, data):
        self._state = data['state']
        self._teamSize = data['teamSize']
        self._attacksPerMember = data['attacksPerMember']
        self._battleModifier = data['battleModifier']
        self._preparationStartTime = self._set_times(data['preparationStartTime'])
        self._startTime = self._set_times(data['startTime'])
        self._endTime = self._set_times(data['endTime'])

        clan_data = data.get('clan')
        opponent_data = data.get('opponent')

        self.clan = clan_info(clan_data)
        self.opponent = clan_info(opponent_data)

    def get_state(self):
        return self._state

    def get_teamSize(self):
        return self._teamSize

    def get_attacksPerMember(self):
        return self._attacksPerMember

    def get_battleModifier(self):
        return self._battleModifier

    def get_preparationStartTime(self):
        return self._preparationStartTime

    def get_startTime(self):
        return self._startTime

    def get_endTime(self):
        return self._endTime
    
    def _set_times(self, time):
        new_time = datetime.fromisoformat(time.replace('Z', '+00:00')).astimezone(timezone(timedelta(hours=-5)))
        return new_time.strftime("%Y-%m-%d %H")

    def __str__(self):
        return (
            f"State: {self.get_state()}\n"
            f"Team Size: {self.get_teamSize()}\n"
            f"Attacks Per Member: {self.get_attacksPerMember()}\n"
            f"Battle Modifier: {self.get_battleModifier()}\n"
            f"Preparation Start Time: {self.get_preparationStartTime()}\n"
            f"Start Time: {self.get_startTime()}\n"
            f"End Time: {self.get_endTime()}\n"
            f"Clan: \n{self.clan}\n"
            f"Opponent: \n{self.opponent}"
        )

class clan_info():
    def __init__(self, data):
        self._tag = data['tag']
        self._name = data['name']
        self._clanLevel = data['clanLevel']
        self._attacks = data['attacks']
        self._stars = data['stars']
        self._destructionPercentage = data['destructionPercentage']

        self.clan_members_data = self.process_members(data)

    def get_tag(self):
        return self._tag

    def get_name(self):
        return self._name

    def get_clanLevel(self):
        return self._clanLevel

    def get_attacks(self):
        return self._attacks

    def get_stars(self):
        return self._stars

    def get_destructionPercentage(self):
        return self._destructionPercentage

    def process_members(self, data):
        if data is None:
            return None

        war_member_list = data.get('members', [])

        war_member_info_list = []

        for war_member in war_member_list:
            war_member_info = war_members_info(war_member)
            war_member_info_list.append(war_member_info)

        war_member_info_list.sort(key=lambda member: member.get_mapPosition())

        return war_member_info_list
    
    def __str__(self):
         member_info = "\n" + ("\n" + "-" * 20 + "\n").join(str(member) for member in self.clan_members_data)
         return (
            f"  Tag: {self.get_tag()}\n"
            f"  Name: {self.get_name()}\n"
            f"  Clan Level: {self.get_clanLevel()}\n"
            f"  Attacks: {self.get_attacks()}\n"
            f"  Stars: {self.get_stars()}\n"
            f"  Destruction Percentage: {self.get_destructionPercentage()}\n"
            f"    Members: \n{member_info}"
         )

class war_members_info():
    def __init__(self, data):
        self._tag = data['tag']
        self._name = data['name']
        self._townhallLevel = data['townhallLevel']
        self._mapPosition = data['mapPosition']
        self._opponentAttacks = data['opponentAttacks']

    def get_tag(self):
        return self._tag

    def get_name(self):
        return self._name

    def get_townhallLevel(self):
        return self._townhallLevel

    def get_mapPosition(self):
        return self._mapPosition

    def get_opponentAttacks(self):
        return self._opponentAttacks
    
    def __str__(self):
        return (
            f"      Tag: {self.get_tag()}\n"
            f"      Name: {self.get_name()}\n"
            f"      Townhall Level: {self.get_townhallLevel()}\n"
            f"      Map Position: {self.get_mapPosition()}\n"
            f"      Opponent Attacks: {self.get_opponentAttacks()}"
        )