class TaskData:

    def __init__(self, user_id, task_completed):
        self.__user_id = user_id
        self.__task_completed = task_completed

    def to_json(self):
        return {'userId': self.__user_id, 'task_completed': self.__task_completed}

