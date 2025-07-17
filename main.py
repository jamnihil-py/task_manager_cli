import datetime
import argparse
import json
import shlex
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
            with open(TASKS_PATH, 'r') as f:
                self.tasks = json.load(f)

        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = {}
            with open(TASKS_PATH, 'w') as f:
                f.write(json.dumps(self.tasks))

    def add_task(self, task):
        """
        Adds a task to the tasks dictionary
        :param task: Task to be added
        :return: self.tasks
        """
        task_id = len(self.tasks) + 1
        while str(task_id) in self.tasks:
            task_id += 1

        date_time = datetime.datetime.now()

        self.tasks[str(task_id)] = {'Description': task, 'Status': 'todo',
                               'createdAt': date_time.strftime('%c'),
                               'updatedAt': None,}
        self.save_json()
        print(f"{task} successfully added")
        return self.tasks

    def update_task(self, task_id, new_task):
        """

        :param task_id:
        :param new_task:
        :return:
        """
        task_id = str(task_id)

        if task_id in self.tasks:
            old_task = self.tasks[task_id]['Description']
            date_time = datetime.datetime.now()

            self.tasks[task_id].update({'Description': new_task,
                                        'updatedAt': date_time.strftime('%c')})
            self.save_json()

            if self.tasks[task_id]['Description'] == new_task:
                print(f"'{old_task}' changed successfully to '{new_task}'")

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
            deleted_task = self.tasks.pop(task_id)
            print(f"'{deleted_task['Description']}' deleted successfully")
            self.save_json()
            return self.tasks

        else:
            print("Task ID does not exist")
            return None

    def mark_status(self, task_id, new_status):
        """

        :param task_id:
        :param new_status:
        :return:
        """
        task_id = str(task_id)

        if task_id in self.tasks:
            old_status = self.tasks[task_id]['Status']

            if new_status != old_status:
                date_time = datetime.datetime.now()

                self.tasks[task_id].update({
                    'Status': new_status, 'updatedAt': date_time.strftime('%c')
                })
                print(
                    f"'{self.tasks[task_id]['Description']}' status changed from "
                    f"'{old_status}' to '{new_status}'"
                )
                self.save_json()

            else:
                print("The task already has that status")

        else:
            print(f"There is no task with id {task_id}")

    def save_json(self):
        """

        :return:
        """
        with open(TASKS_PATH, 'w') as f:
            f.write(json.dumps(self.tasks))
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
                if value['Status'] == 'done':
                    print(f"{task} - {value['Description']} / {value['Status']}")
            return self.tasks

        elif status == 'todo':
            for task, value in self.tasks.items():
                if value['Status'] == 'todo':
                    print(f"{task} - {value['Description']} / {value['Status']}")
            return self.tasks

        elif status == 'in-progress':
            for task, value in self.tasks.items():
                if value['Status'] == 'in-progress':
                    print(f"{task} - {value['Description']} / {value['Status']}")
            return self.tasks

        return self.tasks

def main():
    """

    :return:
    """
    task_manager = TaskManager()

    while True:
        try:
            user_input = input("> ").strip()
            if not user_input:
                continue

            try:
                parts = shlex.split(user_input)
            except ValueError:
                print("Please, enter a valid input")
                continue

            parser = argparse.ArgumentParser(description='Task Manager CLI')
            subparser = parser.add_subparsers(dest='command', required=True)

            #Add command
            add_parser = subparser.add_parser('add')
            add_parser.add_argument('description', help='Task description')

            #Update command
            update_parser = subparser.add_parser('update')
            update_parser.add_argument('task_id', type=int, help='Task ID to update')
            update_parser.add_argument('update', help='New task')

            #Delete command
            delete_parser = subparser.add_parser('delete')
            delete_parser.add_argument('task_id', type=int, help='Task ID to be deleted')

            #Mark status command
            mark_parser = subparser.add_parser('mark')
            mark_parser.add_argument('task_id', type=int, help='Task ID to change status')
            mark_parser.add_argument('status',
                                              choices=['todo', 'in-progress', 'done'],
                                              help='New Status')

            #List command
            list_parser = subparser.add_parser('list')
            list_parser.add_argument('status', nargs='?',
                                     choices=['todo', 'in-progress', 'done'],
                                     help='Filter by status')

            ###
            args = parser.parse_args(parts)

            if args.command == 'add':
                task_manager.add_task(args.description)
            elif args.command == 'update':
                task_manager.update_task(str(args.task_id), args.update)
            elif args.command == 'delete':
                task_manager.delete_task(str(args.task_id))
            elif args.command == 'mark':
                task_manager.mark_status(str(args.task_id), args.status)
            elif args.command == 'list':
                task_manager.list(args.status)

        except KeyboardInterrupt:
            print("Exit")
            break

        except SystemExit:
            continue

if __name__ == '__main__':
    main()