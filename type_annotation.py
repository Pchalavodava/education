import doctest
from dataclasses import dataclass
from typing import Any
from enum import Enum


class Major(Enum):
    COMPUTER_SCIENCE = 'Информатика'
    ENGINEERING = 'Инженерия'
    MATHEMATICS = 'Математика'
    PHYSICS = 'Физика'
    BIOLOGY = 'Биология'


@dataclass
class Age:
    """
    Класс, представляющий возраст студента
    """
    value: int

    def __post_init__(self) -> None:
        """
        Проверка на возраст студента
        :return: None
        """
        if 15 > self.value or self.value > 99:
            raise ValueError(f'В таком возрасте {self.value} {'еще' if 15 > self.value else 'уже'} не учатся в '
                             f'университете')


@dataclass
class Grade:
    """
    Класс, представляющий средний балл
    """
    value: int | float

    def __post_init__(self) -> None:
        """
        Проверка среднего балла на корректность
        :return: None
        """
        if 1 > self.value or self.value > 5:
            raise ValueError(f'В пятибалльной системе невозможно получить такой балл')


@dataclass
class Student:
    """
    Класс, представляющий студента
    """

    def __init__(self, name: str, age: Age, major: Major, gpa: Grade) -> None:
        """
        Создание объекта класса Student
        :param name: str: Имя студента
        :param age: Age: Возраст студента
        :param major: Major: Специальность
        :param gpa: Grade: Средний балл
        """
        self.name: str = name
        self.age: Age = age
        self.major: Major = major
        self.gpa: Grade = gpa

    def display_info(self) -> str:
        """
        Вывод строковой информации объекта класса Student
        :return: str: Строковое представление имени, возраста, специальности и среднего балла объекта
        >>> student0 = Student('Иван', Age(30), Major.BIOLOGY, Grade(4.4))
        >>> student0.display_info()
        'Студент Иван, возраст 30 лет, специальность Биология, средний балл 4.4'

        >>> student1 = Student('Иван', Age(13), Major.BIOLOGY, Grade(4.4))
        Traceback (most recent call last):
        ...
        ValueError: В таком возрасте 13 еще не учатся в университете

        >>> student2 = Student('Иван', Age(30), Major.BIOLOGY, Grade(7.3))
        Traceback (most recent call last):
        ...
        ValueError: В пятибалльной системе невозможно получить такой балл
        """
        return (f'Студент {self.name}, возраст {self.age.value} лет, специальность {self.major.value}, '
                f'средний балл {self.gpa.value}')

    def calculate_grade(self) -> str:
        """
        Вывод строкового представления среднего балла
        :return: str: Строковое представление среднего балла
        """
        grade_dict: dict[int, str] = {
            5: 'Отлично',
            4: 'Хорошо',
            3: 'Удовлетворительно',
            2: 'Неудовлетворительно',
            1: 'Неудовлетворительно'
        }
        grade = int(round(self.gpa.value))
        return grade_dict[grade]

    def __eq__(self, other: Any) -> bool:
        """
        Сравнение объектов класса Student
        :param other: объект класса Student
        :return: bool: True, если объекты идентичны по всем полям
        """
        if isinstance(other, Student):
            return (
                    self.name == other.name and
                    self.age == other.age and
                    self.major.name == other.major.name and
                    self.gpa.value == other.gpa.value
            )
        return False

    def __gt__(self, other: Any) -> bool:
        """
        Сравнение объектов класса Student для дальнейшей сортировки
        :param other: Any: сравниваемый объект класса Student
        :return: bool: True, если условие выполнено
        """
        return self.gpa.value > other.gpa.value


# Создание списка студентов
students: list[Any] = [
    Student("Alice", Age(20), Major.COMPUTER_SCIENCE, Grade(3.8)),
    Student("Bob", Age(22), Major.ENGINEERING, Grade(3.2)),
    Student("Charlie", Age(21), Major.MATHEMATICS, Grade(4.5)),
    Student("David", Age(23), Major.PHYSICS, Grade(2.7)),
    Student("Eve", Age(19), Major.BIOLOGY, Grade(3.9)),
    Student("Eve", Age(19), Major.BIOLOGY, Grade(3.9))
]

# Отображение информации о студентах
for student in students:
    print(student.display_info())
print(50 * '-')

# Сравнение студентов
print("Are Alice and Bob the same student?", students[0] == students[1])
print("Are Alice and Eve the same student?", students[0] == students[4])
print("Are Eve and Eve the same student?", students[4] == students[5])
print(50 * '-')

# Расчет и вывод оценок
for student in students:
    print(f"{student.name} - Grade: {student.calculate_grade()}")
print(50 * '-')

# Сортировка по убыванию
students.sort(reverse=True)
for student in students:
    print(student.display_info())

print(students[1] < students[3])


if __name__ == '__main__':
    import doctest
    doctest.testmod()