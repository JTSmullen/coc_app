# clan_utils.py
# Author = Joshua Smullen
# Date = 02-11-2025
# Last Edit = 02-11-2025
# Description = This module contains functions for clan related operations.
# Conjunction = get_player_info.py

'''Create the class to hold the clan information'''
class Clan:
    '''Initialize the private variables, these cannot be changed once set.'''
    def __init__(self, data):
        self._name = data['name']
        self._level = data['clanLevel']
        self._tag = data['tag']

    '''Getter methods to access private variables'''
    def get_name(self):
        return self._name

    def get_level(self):
        return self._level

    def get_tag(self):
        return self._tag
    '''End of getter methods'''

    '''__str__ function to clearly print all information withheld in the class'''
    def __str__(self):
        return (
            f"Clan Name: {self.get_name()}\n"
            f"  Clan Level: {self.get_level()}\n"
            f"  Clan Tag: {self.get_tag()}"
        )
    # End of Clan
# End of clan_utils.py