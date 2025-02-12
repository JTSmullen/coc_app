# spells_utils.py
# Author = Joshua Smullen
# Date = 02-11-2025
# Last Edit = 02-11-2025
# Description = This module contains functions for getting troops information
# Conjunction = get_player_info.py

'''Create the class to hold spells information'''
class Spell:
    '''Initialize the private variables, these cannot be changed once set.'''
    def __init__(self, data):
        self._name = data['name']
        self._level = data['level']
        self._maxLevel = data['maxLevel']
        self._village = data['village']

    '''Getter methods to access private variables'''
    def get_name(self):
        return self._name

    def get_level(self):
        return self._level

    def get_maxLevel(self):
        return self._maxLevel

    def get_village(self):
        return self._village
    '''End of getter methods'''

    '''__str__ function to clearly print all information withheld in the class'''
    def __str__(self):
        return (
            f"Spell: {self.get_name()}\n"
            f"  Level: {self.get_level()}\n"
            f"  Max Level: {self.get_maxLevel()}\n"
            f"  Village: {self.get_village()}"
        )
    # End of Spell
# End of spells_utils.py