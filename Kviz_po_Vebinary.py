class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course):
        self.finished_courses.append(course)

    def rate_lp(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_rate(self):
        all_grades = sum(self.grades.values(), [])
        average = round(sum(all_grades) / len(all_grades), 2)
        return average

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Студентов можно сравнивать только со студентами')
            return
        return self._average_rate() < other._average_rate()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания:{self._average_rate()}\n' \
               f'Курсы в процессе изучения:{", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы:{", ".join(self.finished_courses)}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_rate(self):
        all_grades = sum(self.grades.values(), [])
        average = round(sum(all_grades) / len(all_grades), 2)
        return average

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Лекторов можно сравнивать только с лекторами')
            return
        return self._average_rate() < other._average_rate()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за лекции:{self._average_rate()}'


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
        return f'Имя: {self.name}\nФамилия: {self.surname}'


student_1 = Student('Artem', 'Volkov', 'Female')
student_2 = Student('Alina', 'Lisina', 'Female')

lecturer_1 = Lecturer('Nisha', 'Grishina')
lecturer_2 = Lecturer('Robo', 'Cop')

reviewer_1 = Reviewer('Spider', 'Man')
reviewer_1.courses_attached += ['JS', 'Phyton']
reviewer_2 = Reviewer('Loki', 'Odinson')
reviewer_2.courses_attached += ['Java', 'Phyton']

student_1.add_courses('Английский для начинающих с нуля')
student_2.add_courses('Программирования для чайникоФФФ')

lecturer_1.courses_attached = ['Java', 'Phyton']
lecturer_2.courses_attached = ['JS', 'Phyton']

student_1.courses_in_progress = ['JS', 'Phyton']
student_2.courses_in_progress = ['Java', 'Phyton']

student_1.rate_lp(lecturer_1, 'Phyton', 7)
student_2.rate_lp(lecturer_1, 'Java', 6)
student_2.rate_lp(lecturer_1, 'Phyton', 10)

student_1.rate_lp(lecturer_2, 'JS', 9)
student_1.rate_lp(lecturer_2, 'Phyton', 7)
student_2.rate_lp(lecturer_2, 'Phyton', 8)

reviewer_1.rate_hw(student_1, 'JS', 2)
reviewer_1.rate_hw(student_1, 'Phyton', 8)
reviewer_1.rate_hw(student_2, 'Phyton', 7)

reviewer_2.rate_hw(student_1, 'Phyton', 10)
reviewer_2.rate_hw(student_2, 'Java', 6)
reviewer_2.rate_hw(student_2, 'Phyton', 9)

print(student_1)
print(lecturer_2)
print(reviewer_1)
print(student_2.__lt__(student_1))
print(lecturer_1.__lt__(lecturer_2))

student_list = []
student_list += student_1, student_2
lecturer_list = []
lecturer_list += lecturer_1, lecturer_2


def students_grades(students, course):
    all_grades_students = []
    for student in students:
        all_grades_students += student.grades.get(course, [])
    mean_grade = round(sum(all_grades_students) / len(all_grades_students), 2)
    return mean_grade


def lecturers_grades(lecturers, course):
    all_grades_lecturers = []
    for lecture in lecturers:
        all_grades_lecturers += lecture.grades.get(course, [])
    mean_grades = round(sum(all_grades_lecturers) / len(all_grades_lecturers), 2)
    return mean_grades


print(lecturers_grades(lecturer_list, 'Phyton'))
print(students_grades(student_list, 'Phyton'))
