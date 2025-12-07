# student.py
from user import User  # ensure the User class exists in user.py

class Student(User):  # inherit from User
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)  # call User's __init__
        self.knowledge = []  # start with empty knowledge list

    def learn(self, info):
        self.knowledge.append(info)  # add knowledge

    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        print("Pick me!")


class ChattyStudent(Student):
    def hello(self):
        super().hello()
        print(
            "How are you doing today? I'm okay, but I'm kind of tired. "
            "Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! "
            "What, you don't want any spoilers? Okay well let me just tell you who died..."
        )

    def raise_hand(self):
        for _ in range(10):
            super().raise_hand()
