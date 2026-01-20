import requests

# Add a task
resp = requests.post("http://127.0.0.1:5000/add", data={"task": "Learn Flask"})
print(resp.text)

# List tasks
resp = requests.get("http://127.0.0.1:5000/list")
print(resp.text)
