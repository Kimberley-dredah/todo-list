from flask import Flask, request
import todo  # this imports your functions from todo.py

app = Flask(__name__)

@app.route("/add", methods=["POST"])
def add():
    name = request.form.get("task")
    if not name:
        return "Missing 'task' field", 400
    todo.add_task(name)
    return f"Added: {name}"

@app.route("/list", methods=["GET"])
def list_all():
    tasks = todo.list_tasks()
    return "<br>".join([f"{i}. {t}" for i, t in enumerate(tasks, start=1)])

@app.route("/remove", methods=["POST"])
def remove():
    raw = request.form.get("task_num")
    try:
        task_num = int(raw)
    except (TypeError, ValueError):
        return "Provide a valid 'task_num' number", 400

    removed = todo.remove_task(task_num)
    if removed is None:
        return "Invalid task number.", 400
    return f"Removed: {removed}"

if __name__ == "__main__":
    app.run(debug=True)
