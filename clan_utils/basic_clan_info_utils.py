class Basic_Clan_Info():
    def __init__(self, data):
        self._tag = data['tag']
        self._warTies = data['warTies']
        self._warLosses = data['warLosses']
        self._clanPoints = data['clanPoints']
        self._isFamilyFriendly = data['isFamilyFriendly']
        self._isWarLogPublic = data['isWarLogPublic']
        self._warFrequency = data['warFrequency']
        self._clanLevel = data['clanLevel']
        self._clanCapitalPoints = data['clanCapitalPoints']
        self._requiredTrophies = data['requiredTrophies']
        self._requiredBuilderBaseTrophies = data['requiredBuilderBaseTrophies']
        self._requiredTownhallLevel = data['requiredTownhallLevel']
        self._warWinStreak = data['warWinStreak']
        self._warWins = data['warWins']
        self._clanBuilderBasePoints = data['clanBuilderBasePoints']
        self._name = data['name']
        self._type = data['type']
        self._members = data['members']
        self._description = data['description']
        self._location = data['location']

    def get_tag(self):
        return self._tag

    def get_warTies(self):
        return self._warTies

    def get_warLosses(self):
        return self._warLosses

    def get_clanPoints(self):
        return self._clanPoints

    def get_isFamilyFriendly(self):
        return self._isFamilyFriendly

    def get_isWarLogPublic(self):
        return self._isWarLogPublic

    def get_warFrequency(self):
        return self._warFrequency

    def get_clanLevel(self):
        return self._clanLevel

    def get_clanCapitalPoints(self):
        return self._clanCapitalPoints

    def get_requiredTrophies(self):
        return self._requiredTrophies

    def get_requiredBuilderBaseTrophies(self):
        return self._requiredBuilderBaseTrophies

    def get_requiredTownhallLevel(self):
        return self._requiredTownhallLevel

    def get_warWinStreak(self):
        return self._warWinStreak

    def get_warWins(self):
        return self._warWins

    def get_clanBuilderBasePoints(self):
        return self._clanBuilderBasePoints

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

    def get_members(self):
        return self._members

    def get_description(self):
        return self._description

    def get_location(self):
        return self._location

    def __str__(self):
        return (
            f"- Clan Name: {self.get_name()}\n"
            f"  - Tag: {self.get_tag()}\n"
            f"  - Type: {self.get_type()}\n"
            f"  - Description: {self.get_description()}\n"
            f"  - Members: {self.get_members()}\n"
            f"  - Clan Level: {self.get_clanLevel()}\n"
            f"  - Clan Points: {self.get_clanPoints()}\n"
            f"  - Clan Builder Base Points: {self.get_clanBuilderBasePoints()}\n"
            f"  - Clan Capital Points: {self.get_clanCapitalPoints()}\n"
            f"  - Required Trophies: {self.get_requiredTrophies()}\n"
            f"  - Required Builder Base Trophies: {self.get_requiredBuilderBaseTrophies()}\n"
            f"  - Required Townhall Level: {self.get_requiredTownhallLevel()}\n"
            f"  - Location: {self.get_location()}\n"
            f"  - War Frequency: {self.get_warFrequency()}\n"
            f"  - War Win Streak: {self.get_warWinStreak()}\n"
            f"  - War Wins: {self.get_warWins()}\n"
            f"  - War Ties: {self.get_warTies()}\n"
            f"  - War Losses: {self.get_warLosses()}\n"
            f"  - Is Family Friendly: {self.get_isFamilyFriendly()}\n"
            f"  - Is War Log Public: {self.get_isWarLogPublic()}"
        )