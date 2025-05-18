from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []  # Initialize knowledge as an empty list
    
    def learn(self, skill):
        self.knowledge.append(skill)
        return self.knowledge

# Sample Student instance to test
student1 = Student("juma", "Isaiah")
print(student1.first_name, student1.last_name)
print(student1.learn("JavaScript"))
