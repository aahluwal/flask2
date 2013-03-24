
from flask import Flask, render_template, request, redirect 
import model

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html", user_name="chriszf")

@app.route("/tasks")
def list_tasks():
  db = model.connect_db()
  tasks_from_db = model.get_tasks(db, None)
  user_id_list = []
  for dictionary in tasks_from_db:
    user_id_list.append(dictionary["user_id"])
  for user_id in user_id_list:
    users_from_db = model.get_user(db, user_id)
  return render_template("list_tasks.html", tasks=tasks_from_db,users=users_from_db)

@app.route("/new_task")
def new_tasks():
  return render_template("new_task.html")

@app.route("/save_task", methods=["POST"])
def save_task():
  task_title = request.form['task_title']
  db = model.connect_db()
  task_id = model.new_task(db, task_title, 1)
  return redirect("/tasks")

@app.route("/complete_task", methods=["POST"])
def complete_task():
  task_id = request.form['task_id']
  db = model.connect_db()
  model.complete_task(db, task_id)
  return redirect("/tasks") 

if __name__ == "__main__":
  app.run(debug=True)
