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
    
    # Setter
    def set_num_students(self, students):
        self.num_students = students

    # __repr__() method
    def __repr__(self):
        return (f"{self.name} is for gifted {self.level} school students. We boast a student body of {self.num_students}!")


