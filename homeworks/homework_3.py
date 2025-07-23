class Person:
    def __init__(self, name, birth_date, occupation, higher_education=False):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    def get_occupation(self):
        return self.__occupation

    def has_higher_education(self):
        return self.__higher_education

    def introduce(self):
        edu_status = "есть среднее образование" if self.__higher_education else "нет среднего образования"
        print(f"Привет, меня зовут {self.name}. Я — {self.__occupation}. У меня {edu_status}.")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, hobby, higher_education=True):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        edu_status = "есть среднее образование" if self.has_higher_education() else "нет среднего образования"
        print(f"Привет, меня зовут {self.name}. Я — {self.get_occupation()}. "
              f"Мое хобби — {self.hobby}. У меня {edu_status}.")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, group_name, higher_education=True):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        edu_status = "есть среднее образование" if self.has_higher_education() else "нет среднего образования"
        print(f"Привет, меня зовут {self.name}. Я — {self.get_occupation()}. "
              f"Я учился с Акбаром в классе {self.group_name}. У меня {edu_status}.")


cl1 = Classmate("Аслан", "20.02.2009", "школьник", "9В", True)
cl1.introduce()

fr1 = Friend("Эмиль", "20.02.2008", "школьник", "футбол", True)
fr1.introduce()
