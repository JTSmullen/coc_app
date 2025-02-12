# heroes_utils.py
# Author = Joshua Smullen
# Date = 02-11-2025
# Last Edit = 02-11-2025
# Description = This module contains functions for getting achievements information.
# Conjunction = get_player_info.py

'''Create the class to hold the heroes equipment information'''
class HeroEquipment:
    '''Initailize the private variables, these cannot be changed once set.'''
    def __init__(self, data):
        self._name = data['name']
        self._level = data['level']
        self._maxLevel = data.get('maxLevel', None)
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
        return f"  - {self.get_name()}: Level {self.get_level()}"
    # End of HeroEquipment class

'''Create the class to hold all hero information'''
class Hero:
    '''Initailize the private variables, these cannot be changed once set.'''
    def __init__(self, data):
        self._name = data['name']
        self._level = data['level']
        self._maxLevel = data['maxLevel']
        self._village = data['village']
        self._equipment = self._process_equipment(data.get('equipment', []))

    '''Getter methods to access private variables'''
    def get_name(self):
        return self._name

    def get_level(self):
        return self._level

    def get_maxLevel(self):
        return self._maxLevel

    def get_village(self):
        return self._village

    def get_equipment(self):
        return self._equipment
    '''End of getter methods'''

    '''Method to create the equipment instances to hold the equipment information for each hero'''
    def _process_equipment(self, equipment_data):
        equipment = []
        for equip_data in equipment_data:
            equip = HeroEquipment(equip_data)
            equipment.append(equip)
        return equipment

    '''__str__ function to clearly print all information withheld in the class'''
    def __str__(self):
        equipment_str = "\n".join(str(equip) for equip in self.get_equipment())
        return (
            f"Hero: {self.get_name()}\n"
            f"  Level: {self.get_level()}\n"
            f"  Max Level: {self.get_maxLevel()}\n"
            f"  Village: {self.get_village()}\n"
            f"  Equipment:\n{equipment_str}"
        )
    # End of Hero class
# End of heroes_utils.py