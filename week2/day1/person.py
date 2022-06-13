
# class Person():
#     def __unit__(self, person_name, person_age, person_height, person_profession):
#         self.name = person_name
#         self.age = person_age
#         self.height = person_height
#         self.profession = person_profession
#         # self.hobbies = []

# person_x = Person("Will", 31, "Instructor", "6'0'")

# print(person_x.profession)

class Person():
    def __init__(self, person_name):
        self.name = person_name

    def set_hair(self, person_hair):
        self.hair = person_hair

# this is a getter
    def get_hair(self):
        print(self.hair)

# class Person():
#     def __init__(self, name):
#         # the constructor method
#         self.name = name
#         self.age = None
#         self.profession = None
#         self.height = None
#         self.hobbies = []

# new_person = Person("Will")
# new_person.age = 31
# print (new_person.age)
# jay_person = Person("Mister Person")

# jay_person.age = 31
# jay_person.profession = "Instructor & Developer"

# print (jay_person.profession)

# # variable_dec

# # class


# # what is constants

# db = SQLAlchemy


# class User(db.Model):
#     id = db.Column(db.integer, nullable = False)
# name = db.Column(db.String(length=200))


