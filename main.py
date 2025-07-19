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
        if not self.tasks:
            task_id = 1
        else:
            task_id = int(max(self.tasks)) + 1

        date_time = datetime.datetime.now()
        task = task.capitalize()

        self.tasks[str(task_id)] = {'Description': task, 'Status': 'todo',
                               'createdAt': date_time.strftime('%c'),
                               'updatedAt': None,}

        return task, task_id

    def update_task(self, task_id, new_task):
        """

        :param task_id:
        :param new_task:
        :return:
        """
        if task_id in self.tasks:
            old_task = self.tasks[task_id]['Description']
            date_time = datetime.datetime.now()
            new_task = new_task.capitalize()

            self.tasks[task_id].update({'Description': new_task,
                                        'updatedAt': date_time.strftime('%c')})
            return old_task, new_task

        else:
            return False, False

    def delete_task(self, task_id):
        """

        :param task_id:
        :return:
        """
        if task_id in self.tasks:
            deleted_task = self.tasks.pop(task_id)
            return deleted_task

        else:
            return None

    def mark_status(self, task_id, new_status):
        """

        :param task_id:
        :param new_status:
        :return:
        """
        if task_id in self.tasks:
            old_status = self.tasks[task_id]['Status']

            if new_status != old_status:
                date_time = datetime.datetime.now()

                self.tasks[task_id].update({
                    'Status': new_status, 'updatedAt': date_time.strftime('%c')
                })
                return old_status, new_status, self.tasks[task_id]['Description']

            return None, None, None

        else:
            return False, False, False

    def list(self, status=None):
        """

        :return:
        """
        if status is None:
            for task, value in self.tasks.items():
                print(f" [ID: {task}] '{value['Description']}' -"
                      f" (Status: {value['Status'].capitalize()})")
        else:
            for task, value in self.tasks.items():
                if value['Status'] == status:
                    print(f" [ID: {task}] '{value['Description']}' -"
                          f" (Status: {value['Status'].capitalize()})")

        return self.tasks

    def save_json(self):
        """

        :return:
        """
        with open(TASKS_PATH, 'w') as f:
            f.write(json.dumps(self.tasks))
        return self.tasks

def main():
    """

    :return:
    """
    task_manager = TaskManager()

    parser = argparse.ArgumentParser(description='Task Manager CLI')
    subparser = parser.add_subparsers(dest='command', required=True)

    # Add command
    add_parser = subparser.add_parser('add')
    add_parser.add_argument('description', help='Task description')

    # Update command
    update_parser = subparser.add_parser('update')
    update_parser.add_argument('task_id', type=int, help='Task ID to update')
    update_parser.add_argument('update', help='New task')

    # Delete command
    delete_parser = subparser.add_parser('delete')
    delete_parser.add_argument('task_id', type=int,
                               help='Task ID to be deleted')

    # Mark status command
    mark_parser = subparser.add_parser('mark')
    mark_parser.add_argument('task_id', type=int,
                             help='Task ID to change status')
    mark_parser.add_argument('status',
                             choices=['todo', 'in-progress', 'done'],
                             help='New Status')

    # List command
    list_parser = subparser.add_parser('list')
    list_parser.add_argument('status', nargs='?',
                             choices=['todo', 'in-progress', 'done'],
                             help='Filter by status')

    # Quit command
    quit_parser = subparser.add_parser('q')

    # Save command
    save_parser = subparser.add_parser('s')

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

            args = parser.parse_args(parts)

            if args.command == 'add':
                task, task_id = task_manager.add_task(args.description)
                print(f"'{task}' added successfully (ID: {task_id})")

            elif args.command == 'update':
                old_task, new_task = task_manager.update_task(
                    str(args.task_id), args.update
                )
                if old_task:
                    print(f"'{old_task}' changed successfully to '{new_task}'")
                else:
                    print("Task ID does not exist")

            elif args.command == 'delete':
                deleted_task = task_manager.delete_task(str(args.task_id))
                if deleted_task:
                    print(f"'{deleted_task['Description']}'"
                          f" deleted successfully")
                else:
                    print("Task ID does not exist")

            elif args.command == 'mark':
                old_status, new_status, task = task_manager.mark_status(
                    str(args.task_id), args.status
                )
                if old_status:
                    print(
                        f"'{task}' status changed from "
                        f"'{old_status.capitalize()}' to '{new_status.capitalize()}'"
                    )
                elif old_status is None:
                    print(f"The task already has that status")
                else:
                    print("Task ID does not exist")

            elif args.command == 'list':
                task_manager.list(args.status)

            elif args.command == 'q':
                print("Saving...")
                task_manager.save_json()
                break

            elif args.command == 's':
                task_manager.save_json()
                print("Saved successfully")

        except KeyboardInterrupt:
            print("Saving...")
            task_manager.save_json()
            break

        except SystemExit:
            continue

if __name__ == '__main__':
    main()