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


class PrimarySchool(School):
    def __init__(self, name, num_students, pickup_policy):
        super().__init__(name, "Primary", num_students)
        self.pickup_policy = pickup_policy

    # Getters
    def get_pickup_policy(self):
        return self.pickup_policy
    
    # __repr__ method
    def __repr__(self):
        return super().__repr__() + "\n" + f"Pickup Policy: {self.pickup_policy}"


class HighSchool(School):
    def __init__(self, name, num_students, sports_teams):
        super().__init__(name, "High", num_students)
        self.sports_teams = sports_teams
    
    # Getters
    def get_sports_teams(self):
        return self.sports_teams

    # __repr__ method
    def __repr__(self):
        repr_string = super().__repr__() + "\n" + "\nSports Teams:\n"
        
        for team in self.sports_teams:
            repr_string += team + "\n"
        return repr_string

