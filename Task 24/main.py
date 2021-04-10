import json
from TaskData import TaskData


def deserialize(source):
    with open(source, "r") as read_file:
        return json.load(read_file)


def serialize(file_name, data):
    with open(file_name, "w") as write_file:
        json.dump(data, write_file)


data = deserialize("in.json")
todo = {}
for object in data:
    if object["completed"]:
        try:
            todo[object["userId"]] += 1
        except KeyError:
            todo[object["userId"]] = 1

result_task_data = []
keys = todo.keys()

for key in keys:
    result_task_data.append(TaskData(key, todo[key]).to_json())

serialize("out.json", result_task_data)


