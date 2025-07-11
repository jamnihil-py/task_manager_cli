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
        task_id = len(self.tasks) + 1
        self.tasks[task_id] = {'Description': task, 'Status': 'To-do',
                               'createdAt': '', 'updatedAt': '',}

        return self.tasks