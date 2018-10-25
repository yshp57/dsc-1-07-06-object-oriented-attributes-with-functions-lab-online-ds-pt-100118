class School:
    def __init__(self, name=None):
        self.name= name
        self._roster= {}
    def roster(self):
        return self._roster 
    def add_student(self, name, grade):
        try:
            self._roster[str(grade)].append(name)
        except:
            self._roster[str(grade)] = []
            self._roster[str(grade)].append(name)
    def grade(self, grade):
        return self._roster[str(grade)]
    def sort_roster(self):
        for grade in list(self._roster.keys()):
            self._roster[str(grade)] = sorted(self._roster[str(grade)])
        return self._roster
        
            
        