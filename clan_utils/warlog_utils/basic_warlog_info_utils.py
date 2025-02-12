from datetime import datetime

class Basic_Warlog_Info():
    def __init__(self, data):
        self._teamSize = data['teamSize']
        self._attacksPerMember = data['attacksPerMember']
        self._battleModifier = data['battleModifier']
        self._endTime = data['endTime']
        self._result = data['result']

        self._set_end_time()

    def get_teamSize(self):
        return self._teamSize
    
    def get_attackPerMember(self):
        return self._attacksPerMember
    
    def get_battleModifier(self):
        return self._battleModifier
    
    def get_endTime(self):
        return self._endTime
    
    def get_result(self):
        return self._result
    
    def _set_end_time(self):
        self._endTime = datetime.fromisoformat(self._endTime.replace('Z', '+00:00'))
        self._endTime = self._endTime.date()
    
    def __str__(self):
        return (
            f"Team Size: {self.get_teamSize()}\n"
            f"Attacks Per Member: {self.get_attackPerMember()}\n"
            f"Battle Modifier: {self.get_battleModifier()}\n"
            f"End Time: {self.get_endTime()}\n"
            f"Result: {self.get_result()}"
        )