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

        self.tasks[task_id] = {'Description': task, 'Status': 'todo',
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
        """

        :param task_id:
        :return:
        """
        task_id = str(task_id)

        if task_id in self.tasks:
            del self.tasks[task_id]
            return self.tasks
        else:
            print("Task ID does not exist")
            return None

    def change_task_status(self, task_id, status):
        """

        :param task_id:
        :param status:
        :return:
        """
        status = status.strip().lower()
        task_id = str(task_id)

        if task_id in self.tasks:

            if status == 'in-progress' or 'done' or 'todo':
                date_time = datetime.datetime.now()
                self.tasks[task_id].update({'Status': status,
                                            'updatedAt': date_time.strftime('%c')})
                self.save_json()

            else:
                print(f"{status} is not a valid status\n"
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

    def list(self, status=None):
        """

        :return:
        """
        if status is None:
            for task, value in self.tasks.items():
                print(f"{task} - {value['Description']} / {value['Status']}")
            return self.tasks

        elif status == 'done':
            for task, value in self.tasks.items():
                if value['Status'] == 'Done':
                    print(f"{task} - {value['Description']} / {value['Status']}")
            return self.tasks

        elif status == 'todo':
            for task, value in self.tasks.items():
                if value['Status'] == 'Todo':
                    print(f"{task} - {value['Description']} / {value['Status']}")
            return self.tasks

        elif status == 'in-progress':
            for task, value in self.tasks.items():
                if value['Status'] == 'In-Progress':
                    print(f"{task} - {value['Description']} / {value['Status']}")
            return self.tasks

        return self.tasks

def main():
    """

    :return:
    """
    task_manager = TaskManager()

    parser = argparse.ArgumentParser(description='Task Manager CLI')
    subparser = parser.add_subparsers(dest='command', required=True)

    #Add command
    add_parser = subparser.add_parser('add')
    add_parser.add_argument('description', help='Task description')

    #Update command
    update_parser = subparser.add_parser('update')
    update_parser.add_argument('task_id', help='Task ID to update')
    update_parser.add_argument('update', help='Task updated')

    #Delete command
    delete_parser = subparser.add_parser('delete')
    delete_parser.add_argument('task_id', help='Task ID to be deleted')

    #Change status command
    change_status_parser = subparser.add_parser('change')
    change_status_parser.add_argument('task_id', help='Task ID to change status')
    change_status_parser.add_argument('status',
                                      choices=['todo', 'in-progress', 'done'],
                                      help='New Status')

    #List command
    list_parser = subparser.add_parser('list')
    list_parser.add_argument('status', nargs='?',
                             choices=['todo', 'in-progress', 'done'],
                             help='Filter by status')

    ###
    args = parser.parse_args()

    if args.command == 'add':
        task_manager.add_task(args.description)
    elif args.command == 'update':
        task_manager.update_task(args.task_id, args.update)
    elif args.command == 'delete':
        task_manager.delete_task(args.task_id)
    elif args.command == 'change':
        task_manager.change_task_status(args.task_id, args.status)
    elif args.command == 'list':
        task_manager.list(args.status)

main()