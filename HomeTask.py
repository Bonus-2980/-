class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def average_grade(self):
        if not self.grades:
            return 0
        return sum(sum(g) for g in self.grades.values()) / sum(len(g) for g in self.grades.values())
        
    def __str__(self):
        avg_grade = self.average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(sum(g) for g in self.grades.values()) / sum(len(g) for g in self.grades.values())

    def __str__(self):
        avg_grade = self.average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return super().__str__()
    
def average_student_grade(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0

def average_lecturer_grade(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0
 
student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']
student1.grades = {'Python': [10, 10], 'Git': [10]}

student2 = Student('Anna', 'Frost', 'your_gender')
student2.courses_in_progress += ['Python', 'Git']
student2.finished_courses += ['Введение в программирование']
student2.grades = {'Python': [10, 10], 'Git': [10]}

lecturer1 = Lecturer('Alex', 'Bond')
lecturer1.courses_attached += ['Python']
lecturer1.grades = {'Python': [10, 10, 10]}

lecturer2 = Lecturer('John', 'Snow')
lecturer2.courses_attached += ['Git']
lecturer2.grades = {'Git': [10, 10, 10]}

reviewer1 = Reviewer('Tony', 'Soprano')
reviewer1.courses_attached += ['Python', 'Git']

reviewer2 = Reviewer('Fred', 'Jonson')
reviewer2.courses_attached += ['Python', 'Git']

students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print(reviewer1)
print()
print(reviewer2)
print()
print(lecturer1)
print()
print(lecturer2)
print()
print(student1)
print()
print(student2)
print()

print(f"Средняя оценка за домашние задания по курсу Python: {average_student_grade(students, 'Python'):.2f}")

print(f"Средняя оценка за лекции по курсу Python: {average_lecturer_grade(lecturers, 'Python'):.2f}")
