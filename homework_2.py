class Person:
    def __init__(self, name, birth_date, occupation, higher_education=False):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        edu_status = "имеет высшее образование" if self.higher_education else "не имеет высшего образования"
        print(f"Привет меня зовут {self.name}. Я родился(ась) {self.birth_date}. "
              f"Я работаю как {self.occupation}, и я {edu_status}.")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, hobby, higher_education=True):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я друг Акбара. "
              f"Я родился {self.birth_date}, работа: {self.occupation}, моё хобби — {self.hobby}.")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, group_name, higher_education=True):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я одноклассник Акбара. "
              f"Учились вместе в {self.group_name}, я родился {self.birth_date}, работа: {self.occupation}.")

friend1 = Friend(name="Нурсултан", birth_date="5.12.2000", occupation="Программист", hobby="баскетбол")
friend2 = Friend(name="Байэл", birth_date="1.01.2001", occupation="Бизнесмен", hobby="бокс")

classmate1 = Classmate(name="Искендер", birth_date="12.12.2001", occupation="Программист", group_name="11 В")
classmate2 = Classmate(name="Айбек", birth_date="22.11.2000", occupation="Инженер", group_name="9 Б")

people = [friend1, friend2, classmate1, classmate2]

for person in people:
    person.introduce()
