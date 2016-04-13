class Teacher(object):
    
    grades = {1 : 'First', 2 : "Second", 3 : "Third", 4 : "Fourth", 5 : "Fifth"}
    
    def __init__(self, firstName, lastName, age, classes, grade):
        self._firstName = firstName
        self._lastName = lastName
        self.age = age
        self._classes = classes
        self._grade = grade
    
    @property
    def firstName(self):
        return self._firstName.capitalize()
    
    @property
    def lastName(self):
        return self._lastName.capitalize()
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        self._age = int(value)
   
    @property
    def classes(self):
        return sorted(self._classes)
    
    @property
    def grade(self):
        return self.grades[self._grade]
    
    @grade.setter
    def grade(self, value):
        self.grades[value] # throw error if value != a key
        self._grade = value
    
    @grade.deleter
    def grade(self):
        self.age += 1
        del self._grade

class Prof(Teacher):
    grades = {1: "Freshman", 2 : "Sophomore", 3 : "Junior", 4 : "Senior",  5 : "Masters"}

if __name__ == "__main__":
    foo =  Prof("steve", "holden", "63",
                   ["Python 3-1", "Python 3-2", "Python 3-3"],
                   5)
    print(foo.firstName, foo.lastName)
    print(foo.grade)
        