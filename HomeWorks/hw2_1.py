class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    # metod
    def introduse_myself(self):
        marital_status = "married" if self.is_married else "single"
        print(f"Имя: {self.full_name}, Возраст: {self.age}, Семейное положение(женат/замужем): {self.is_married}")


class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    # metod
    def average_marks(self):
        if self.marks:
            return sum(self.marks.values())/len(self.marks)
        return  0

class Teacher(Person):
    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    base_salary = 30000

    def calculate_salary(self):
        bonus = 0.05 * (self.experience - 3) * self.base_salary if self.experience > 3 else 0
        return self.base_salary + bonus

teacher = Teacher("Иван Петров", 38, "Да", 11)
teacher.introduse_myself()
print(f"Зарплата:{teacher.calculate_salary()}")

def create_student():
    student1 = Student("Света", 20, "Нет", {"Алгебра": 79, "Русский": 85, "История": 82})
    student2 = Student("Анна", 19, "Нет", {"Алгебра": 76, "Русский": 90, "История": 95})
    student3 = Student("Антон", 21, "Да", {"Алгебра": 65, "Русский": 87, "История": 91})
    return [student1, student2, student3]

students = create_student()
for student in students:
    student.introduse_myself()
    print(f"Средняя оценка: {student.average_marks()}")





