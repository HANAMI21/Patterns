from abc import ABC, abstractmethod


class Worker(ABC):
    """
    Базовый интерфейс Worker определяет поведение,
    которое изменяется декораторами"""

    @abstractmethod
    def get_salary(self):
        pass


class SimpleTeacher(Worker):
    """Конкретный Worker предоставляет реализацию поведения по умолчанию.
    Данный класс будем декорировать"""

    def __init__(self, salary: int):
        self.salary = salary

    def get_salary(self):
        return self.salary


class BaseDecorator(Worker):
    @abstractmethod
    def get_category(self):
        pass


class FirstCategoryTeacher(BaseDecorator):
    def __init__(self, wrapped: Worker, coefficient: float):
        self.wrapped = wrapped
        self.coefficient = coefficient
        self.category = "Первая"

    def get_salary(self):
        return self.wrapped.get_salary() * self.coefficient

    def get_category(self):
        return self.category


class HighestCategoryTeacher(BaseDecorator):
    def __init__(self, wrapped: Worker, coefficient: float):
        self.wrapped = wrapped
        self.coefficient = coefficient
        self.category = "Высшая"

    def get_salary(self):
        return self.wrapped.get_salary() * self.coefficient

    def get_category(self):
        return self.category


if __name__ == '__main__':
    def info(teacher: BaseDecorator):
        print(f"Зарплата учителя, у которого категория '{teacher.get_category()}' = {teacher.get_salary()}")
        print()


    simple_teacher1 = SimpleTeacher(5000)
    first_category_teacher = FirstCategoryTeacher(simple_teacher1, 2.27)
    info(first_category_teacher)

    simple_teacher2 = SimpleTeacher(5000)
    highest_category_teacher = HighestCategoryTeacher(simple_teacher2, 2.42)
    info(highest_category_teacher)
