#school dashboard exercise
class School():
  def display(self):
    print("school name is 'model school'")
class Teacher (School):
  def __init__(self, name, subject, age):
    self.name=name
    self.subject=subject
    self.age=age
  
  def about_teacher(self):
    print(f'{self.name} teacher, teaches {self.subject} and {self.age} years old')

class Student (School):
  def __init__(self, name1, standard):
    self.name1=name1
    self.standard=standard
  
  def about_student(self):
    print(f'the student is {self.name1} is studying {self.standard} class')

class Statement(Teacher,Student):
  def __init__(self,name,subject,age,name1,standard):
    Teacher.__init__(self,name,subject,age)
    Student.__init__(self,name1,standard)

  def merge(self):
    print(f'{self.name} is a teacher, teaches {self.subject} and {self.name1} is a student, studying {self.standard} class')
    

#teacher1= Teacher ('shiva kumar','physics',45)
#teacher1.about_teacher()
#student1= Student('kumar', 5)
#student1.about_student()
statement1=Statement('shiva kumar','physics',45, 'kumar',5)
statement1.display()
statement1.merge()
statement1.about_student()
statement1.about_teacher()

