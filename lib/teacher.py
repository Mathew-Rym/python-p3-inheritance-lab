from user import User
import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)  # Make sure we call the parent constructor
        # Initialize knowledge as a list of strings (non-empty)
        self.knowledge = [
            "str is a data type in Python",
            "programming is hard, but it's worth it",
            "JavaScript async web request",
            "Python function call definition",
            "object-oriented teacher instance",
            "programming computers hacking learning terminal",
            "pipenv install pipenv shell",
            "pytest -x flag to fail fast",
        ]

    def teach(self):
        # Return a random knowledge from the list
        return self.knowledge[random.randint(0, len(self.knowledge) - 1)]


# Sample instance to verify
teacher1 = Teacher("Julius", "Mwangi")
print(teacher1.first_name, teacher1.last_name)  # Prints the teacher's name
print(teacher1.teach())  # Should print a random knowledge string from the list
