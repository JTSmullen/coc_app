# basic_player_info_utils.py
# Author = Joshua Smullen
# Date = 02-11-2025
# Last Edit = 02-11-2025
# Description = This module contains functions for getting basic player information.
# Conjunction = get_player_info.py

'''Create the class to hold users basic info.'''
class Basic_Player_Info():
    '''Initialize the private variables, these cannot be changed once set.'''
    def __init__(self, data):
        self._tag = data['tag']
        self._name = data['name']
        self._townHallLevel = data['townHallLevel']
        self._townHallWeaponLevel = data['townHallWeaponLevel']
        self._expLevel = data['expLevel']
        self._trophies = data['trophies']
        self._bestTrophies = data['bestTrophies']
        self._warStars = data['warStars']
        self._attackWins = data['attackWins']
        self._defenseWins = data['defenseWins']
        self._builderHallLevel = data['builderHallLevel']
        self._builderBaseTrophies = data['builderBaseTrophies']
        self._bestBuilderBaseTrophies = data['bestBuilderBaseTrophies']
        self._role = data['role']
        self._warPreference = data['warPreference']
        self._donations = data['donations']
        self._donationsReceived = data['donationsReceived']
        self._clanCapitalContributions = data['clanCapitalContributions']

    '''Getter methods to access private variables'''
    def get_tag(self):
        return self._tag

    def get_name(self):
        return self._name

    def get_townHallLevel(self):
        return self._townHallLevel

    def get_townHallWeaponLevel(self):
        return self._townHallWeaponLevel

    def get_expLevel(self):
        return self._expLevel

    def get_trophies(self):
        return self._trophies

    def get_bestTrophies(self):
        return self._bestTrophies

    def get_warStars(self):
        return self._warStars

    def get_attackWins(self):
        return self._attackWins

    def get_defenseWins(self):
        return self._defenseWins

    def get_builderHallLevel(self):
        return self._builderHallLevel

    def get_builderBaseTrophies(self):
        return self._builderBaseTrophies

    def get_bestBuilderBaseTrophies(self):
        return self._bestBuilderBaseTrophies

    def get_role(self):
        return self._role

    def get_warPreference(self):
        return self._warPreference

    def get_donations(self):
        return self._donations

    def get_donationsReceived(self):
        return self._donationsReceived

    def get_clanCapitalContributions(self):
        return self._clanCapitalContributions
    '''End of getter methods'''

    '''__str__ function to cleanly print all information withheld in the class'''
    def __str__(self):
        return (
            f"Player Information:\n"
            f"  Tag: {self.get_tag()}\n"
            f"  Name: {self.get_name()}\n"
            f"  Town Hall Level: {self.get_townHallLevel()}\n"
            f"  Town Hall Weapon Level: {self.get_townHallWeaponLevel()}\n"
            f"  Experience Level: {self.get_expLevel()}\n"
            f"  Trophies: {self.get_trophies()}\n"
            f"  Best Trophies: {self.get_bestTrophies()}\n"
            f"  War Stars: {self.get_warStars()}\n"
            f"  Attack Wins: {self.get_attackWins()}\n"
            f"  Defense Wins: {self.get_defenseWins()}\n"
            f"  Builder Hall Level: {self.get_builderHallLevel()}\n"
            f"  Builder Base Trophies: {self.get_builderBaseTrophies()}\n"
            f"  Best Builder Base Trophies: {self.get_bestBuilderBaseTrophies()}\n"
            f"  Role: {self.get_role()}\n"
            f"  War Preference: {self.get_warPreference()}\n"
            f"  Donations: {self.get_donations()}\n"
            f"  Donations Received: {self.get_donationsReceived()}\n"
            f"  Clan Capital Contributions: {self.get_clanCapitalContributions()}"
        )
# End of basic_player_info_utils.py