# achievements_utils.py
# Author = Joshua Smullen
# Date = 02-11-2025
# Last Edit = 02-11-2025
# Description = This module contains functions for getting achievement information.
# Conjunction = get_player_info.py

'''Create the class to hold an achievements info'''
class Achievements:
    '''Initailize the private variables, these cannot be changed once set.'''
    def __init__(self, data):
        self._name = data['name']
        self._stars = data['stars']
        self._value = data['value']
        self._target = data['target']
        self._info = data['info']
        self._completionInfo = data.get('completionInfo')
        self._village = data['village']

    '''Getter methods to access private variables'''
    def get_name(self):
        return self._name

    def get_stars(self):
        return self._stars

    def get_value(self):
        return self._value

    def get_target(self):
        return self._target

    def get_info(self):
        return self._info

    def get_completionInfo(self):
        return self._completionInfo

    def get_village(self):
        return self._village
    '''End of getter methods'''

    '''__str__ function to clearly print all information withheld in the class'''
    def __str__(self):
        return (
            f"Achievement:\n"
            f"  Name: {self.get_name()}\n"
            f"  Stars: {self.get_stars()}\n"
            f"  Value: {self.get_value()}\n"
            f"  Target: {self.get_target()}\n"
            f"  Info: {self.get_info()}\n"
            f"  Completion Info: {self.get_completionInfo()}\n"
            f"  Village: {self.get_village()}"
        )
# End of achievements_utils.py