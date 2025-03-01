#Задача: Создай класс `Task`, который позволяет управлять задачами (делами).
#У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
#Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

from datetime import datetime

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.due_date}, Статус: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)
        print(f"Задача добавлена: {description}")

    def mark_task_as_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_as_completed()
                print(f"Задача '{description}' отмечена как выполненная.")
                return
        print(f"Задача '{description}' не найдена.")

    def show_current_tasks(self):
        print("Текущие задачи (не выполненные):")
        for task in self.tasks:
            if not task.completed:
                print(task)

task_manager = TaskManager()

task_manager.add_task("Купить молоко", "2025-03-01")
task_manager.add_task("Позвонить другу", "2025-02-28")
task_manager.add_task("Поздравить тещу", "2025-01-08")

task_manager.show_current_tasks()

task_manager.mark_task_as_completed("Купить молоко")

task_manager.show_current_tasks()