import sqlite3
import datetime

def connect_db():
  return sqlite3.connect("tipsy.db")

def new_user(db, email, password, name):
  c = db.cursor()
  query = """INSERT INTO users VALUES (NULL, ?, ?, ?)"""
  result = c.execute(query, (email, password, name))
  db.commit()
  return result.lastrowid

def authenticate(db, email, password):
  c = db.cursor()
  query = """SELECT * FROM users WHERE email=? AND password=?"""
  c.execute(query, (email,password))
  result = c.fetchone()
  if result:
   fields = ["id", "email", "password", "username"]
   return dict(zip(fields, result))

  return None

def new_task(db,title,user_id):
  user_id = str(user_id)
  timestamp = datetime.datetime.today()
  c = db.cursor()
  query = """INSERT INTO tasks VALUES (NULL,?, ?, NULL, ?)"""
  result = c.execute(query, (title,timestamp,user_id))
  db.commit()
  return result.lastrowid
 
def get_user(db, user_id):
  c = db.cursor()
  user_id = str(user_id)
  query = """SELECT * FROM users WHERE id=?"""
  c.execute(query,(user_id))
  result = c.fetchone()
  
  if result:
    keys = ["id", "email", "password", "name"]
    return dict(zip(keys,result))
  return None

def complete_task(db,task_id):
  c = db.cursor()
  timestamp = datetime.datetime.today()
  query = """UPDATE tasks SET completed_by=? WHERE id=?"""
  result = c.execute(query,(timestamp,task_id, ))
  db.commit()
  return 

def get_task(db, task_id):
  c = db.cursor()
  task_id = str(task_id)
  query = """SELECT * FROM tasks WHERE id=?"""
  c.execute(query, (task_id))
  row = c.fetchone()
  if row:
    fields = ["id", "title", "created_at", "completed_by","user_id"]
    return dict(zip(fields, row))
  return None

def get_tasks(db,user_id):
  c = db.cursor()
  if user_id:
    user_id = str(user_id)
    query = """SELECT * FROM tasks WHERE user_id=?"""
    c.execute(query, (user_id))
  else:
    query = """SELECT * FROM tasks"""
    c.execute(query)

  rows = c.fetchall()
  if rows:
    fields = ['id', 'title', 'created_at', 'completed_by', 'user_id']
    tasks = []
    for row in rows:
      task = dict(zip(fields,row))
      tasks.append(task)
    return tasks
  return None 



  
   

  
