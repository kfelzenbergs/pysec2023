
class Person(object):
    firstname = ''
    lastname = ''
    age = ''

    def __init__(self, firstname, lastname, age) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


class Teacher(Person):
    teaching_subjects = []

    def __init__(self, firstname, lastname, age) -> None:
        super().__init__(firstname, lastname, age)


    def assignSubject(self, subject):
        self.teaching_subjects.append(subject)

    def printInfo(self):
        print('''
          Name: {} {}
          Age: {}
          Subjects: {}
        '''.format(self.firstname, self.lastname, self.age, self.teaching_subjects))


kristaps = Teacher('Kristaps', 'Felzenbergs', 32)
kristaps.assignSubject('Python for Security Engineers')
kristaps.assignSubject('Information Security Policy')
kristaps.printInfo()
