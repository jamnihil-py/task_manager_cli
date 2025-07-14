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

        self.tasks[task_id] = {'Description': task, 'Status': 'Todo',
                               'createdAt': date_time.strftime('%c'),
                               'updatedAt': None,}
        self.save_json()
        return self.tasks

    def update_task(self, task_id, updated_task):
        """

        :param task_id:
        :param updated_task:
        :return:
        """
        task_id = str(task_id)

        if task_id in self.tasks:
            date_time = datetime.datetime.now()
            self.tasks[task_id].update({'Description': updated_task,
                                        'updatedAt': date_time.strftime('%c')})
            return self.tasks[task_id]
        else:
            print("Task ID does not exist")
            return None

    def delete_task(self, task_id):
        task_id = str(task_id)

        if task_id in self.tasks:
            del self.tasks[task_id]
            return self.tasks
        else:
            print("Task ID does not exist")
            return None

    def change_task_status(self, task_id, actual_status):
        """

        :param task_id:
        :param actual_status:
        :return:
        """
        actual_status = actual_status.strip().title()
        task_id = str(task_id)

        if task_id in self.tasks:

            if actual_status == 'In-progress' or 'Done' or 'Todo':
                date_time = datetime.datetime.now()
                self.tasks[task_id].update({'Status': actual_status,
                                            'updatedAt': date_time.strftime('%c')})
                self.save_json()

            else:
                print(f"{actual_status} is not a valid status\n"
                      f"try with 'in-progress' or 'done'")

        else:
            print(f"There is no task with id {task_id}")

    def save_json(self):
        """

        :return:
        """
        tasks_json = json.dumps(self.tasks)
        with open(TASKS_PATH, 'w') as f:
            f.write(tasks_json)

        return self.tasks

    def list_all_tasks(self):
        """

        :return:
        """
        for task, value in self.tasks.items():
            print(f"{task} - {value['Description']} / {value['Status']}")

        return self.tasks

    def list_done_tasks(self):
        """

        :return:
        """
        for task, value in self.tasks.items():
            if value['Status'] == 'Done':
                print(f"{task} - {value['Description']} / {value['Status']}")
        return self.tasks

    def list_not_done_tasks(self):
        """"""
        for task, value in self.tasks.items():
            if value['Status'] == 'Todo':
                print(f"{task} - {value['Description']} / {value['Status']}")
        return self.tasks

tmanager = TaskManager()
