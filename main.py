class School:
    def __init__(self, name, level, num_students):
        self.name = name
        self.level = level
        self.num_students = num_students
    
    # Getters
    def get_name(self):
        return self.name
    
    def get_level(self):
        return self.level
    
    def get_num_students(self):
        return self.num_students