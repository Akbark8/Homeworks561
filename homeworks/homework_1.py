class Person:
    def __init__(self, name, birth_date, occupation):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = False

    def introduce(self):
        edu_status = "имеет высшее образование" if self.higher_education else "не имеет высшего образования"
        print(f"Привет! Меня зовут {self.name}. Я родился(ась) {self.birth_date}. "
              f"Я работаю как {self.occupation}, и я {edu_status}.")

person1 = Person("Криштиану Роналду", "05.02.1985", "Шиноби")
person1.higher_education = True

person2 = Person("Лев Толстой", "09.09.1828", "Писатель")

person3 = Person("Леброн Джеймс", "30.12.1984", "Программист")
person3.higher_education = True

for person in [person1, person2, person3]:
    print("\nАтрибуты объекта:")
    print("Имя:", person.name)
    print("Дата рождения:", person.birth_date)
    print("Профессия:", person.occupation)
    print("Высшее образование:", person.higher_education)
    print("\nПредставление:")
    person.introduce()
