# Последнее задание модуля ООП - АННОТАЦИЯ ТИПОВ


> [Аннотации типов](https://code-basics.com/ru/languages/python/lessons/type-annotations#:~:text=%D0%90%D0%BD%D0%BD%D0%BE%D1%82%D0%B0%D1%86%D0%B8%D0%B8%20%D1%82%D0%B8%D0%BF%D0%BE%D0%B2%20%E2%80%94%20%D1%8D%D1%82%D0%BE%20%D0%B2%D0%BE%D0%B7%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D1%83%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D1%8C,%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D1%83%20%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8%20%D0%B2%20Python 
> "Python: Аннотации типов - Code Basics") — это возможность указать типы параметров и возвращаемое значение у функции в Python.

*Задачей было оформить любой, ранее написанный код, по правилам аннотации.<br> По итогу, был выбран код "Создание класса для 
хранения и управления студентами"*

**Данный скрипт содержит в себе классы:**
- Major (специальность)
- Age (возраст)
- Grade (средний балл)
- Student (класс, представляющий непосредственно объект - Студент)

Класс Major, являющийся наследником базового класса для создания перечислений Enum, 
хранит в себе специальности, доступные для обучения, такие как:
- Computer science (Информатика)
- Engineering (Инженерия)
- Mathematics (Математика)
- Physics (Физика)
- Biology (Биология)

Класс Age проверяет значение возраста на корректность: Студентом может являться человек в возрасте от 15 до 99 лет.<br>
Иначе выбрасывается исключение *ValueError*

Класс Grade проверят на корректность, введенный балл. Если балл больше пяти или меньше единицы, тогда исключение *Value
Error*

Класс Student инициализирует объект Студент и содержит поля:
- Name (Имя студента)
- Age (Возраст студента), который является объектом класса Age
- Major (Специальность), которая является объектом класса Major
- Grade (Средний балл), который является объектом класса Grade

Также класс студент имеет свои методы:

- display_info (Выводит строковую информацию об объекте класса)
- calculate_grade (Выводит строковое представление балла)
- `__eq__` (Сравнение объектов класса)
- `__gt__` (Сравнение объектов класса для дальнейшей сортировки)
