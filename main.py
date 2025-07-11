class TaskManager:
    """
    Model a task manager app
    """
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        """
        Adds a task to the tasks dictionary
        :param task: Task to be added
        :return: self.tasks
        """
        task_id = str(len(self.tasks) + 1)
        self.tasks[task_id] = {'Description': task, 'Status': 'To-do',
                               'createdAt': '', 'updatedAt': '',}

        return self.tasks

    def update_task(self, task_id, updated_task):
        """

        :param task_id:
        :return:
        """
        if task_id in self.tasks:
            self.tasks[task_id].update({'Description': updated_task,
                                        'updatedAt': ''})
            return self.tasks[task_id]
        else:
            print("Task ID does not exist")
            return None

tman = TaskManager()
tman.add_task('Cocinar')
print(tman.tasks)

tman.update_task('1', 'Lavar')
print(tman.tasks)

