class Person():
  def __init__(self, name):
    self.__name = name

  def introduce(self):
    print("Hello.")
    print("My name is " + self.__name + ".")

  @property
  def name(self):
    print("name getter")
    return self.__name

  @name.setter
  def name(self, name):
    print("name setter")
    self.__name = name
  

class Student(Person):
  def __init__(self, name, school):
    super().__init__(name)
    self.__school = school
	  
  def introduce(self):
    super().introduce()
    print("My school is " +  self.__school + ".")

  @property
  def school(self):
    print("school getter")
    return self.__school

  @school.setter
  def school(self, school):
    print("school setter")
    self.__school = school

hiroki = Student("hiroki", "junior school")
hiroki.introduce()

print(hiroki.name)
hiroki.name = "new hiroki"
hiroki.introduce()

print(hiroki.school)
hiroki.school = "new school"
hiroki.introduce()

print(vars(hiroki))

