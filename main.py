import datetime
import argparse
import json
from pathlib import Path

TASKS_PATH = Path('tasks.json')

class TaskManager:
    """
    Model a task manager app
    """
    def __init__(self):
        """
        Initializes the class
        """
        try:
            json_tasks = open(TASKS_PATH, 'r')
            self.tasks = json.load(json_tasks)

        except FileNotFoundError:
            with open(TASKS_PATH, 'w') as f:
                f.write('')
            self.tasks = {}

    def add_task(self, task):
        """
        Adds a task to the tasks dictionary
        :param task: Task to be added
        :return: self.tasks
        """
        task_id = str(len(self.tasks) + 1)
        date_time = datetime.datetime.now()
        self.tasks[task_id] = {'Description': task, 'Status': 'To-do',
                               'createdAt': date_time.strftime('%c'),
                               'updatedAt': None,}

        tasks_json = json.dumps(self.tasks)
        with open(TASKS_PATH, 'w') as f:
            f.write(tasks_json)

        return self.tasks

    def update_task(self, task_id, updated_task):
        """

        :param task_id:
        :param updated_task:
        :return:
        """
        if task_id in self.tasks:
            date_time = datetime.datetime.now()
            self.tasks[task_id].update({'Description': updated_task,
                                        'updatedAt': date_time.strftime('%c')})
            return self.tasks[task_id]
        else:
            print("Task ID does not exist")
            return None

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            return self.tasks
        else:
            print("Task ID does not exist")
            return None

tmanager = TaskManager()
tmanager.add_task('Estudiar')