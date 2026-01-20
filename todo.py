tasks = []

def add_task(task):
    tasks.append(task)
    return task

def list_tasks():
    return tasks

def remove_task(task_num):
    # task_num is 1-based (like your console app)
    if 0 < task_num <= len(tasks):
        return tasks.pop(task_num - 1)
    else:
        return None
