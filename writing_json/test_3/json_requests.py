import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

todos_by_user = {}

for todo in todos:
    if todo["completed"]:
        try:
            todos_by_user[todo["userId"]] += 1

        except KeyError:
            todos_by_user[todo["userId"]] = 1

print([todos_by_user])
top_users = sorted(todos_by_user.items(), key=lambda x:x[1], reverse=True)
print(top_users)

max_complete = top_users[0][1]
print(max_complete)

users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

print(users)

max_users = " and ".join(users)
print(f"user(s) {max_users} completed {max_complete} TODOs")

def keep(todo):
    is_complete = todo["completed"]
    has_max_count = str(todo["userId"]) in users
    return is_complete and has_max_count

with open("filtered_data_file.json","w") as data_file:
    filetered_todos = list(filter(keep, todos))
    json.dump(filetered_todos, data_file, indent=2)
