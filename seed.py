import model

db = model.connect_db()
user_id = model.new_user(db, "chriszf@gmail.com", "securepassword", "Christian")
task = model.new_task(db, "complete this now!", 2)

user_id1 = model.new_user(db, "mdeegill@gmail.com", "secure-ishpassword", "Dee")
task1 = model.new_task(db, "new task", 3)
user_id2 = model.new_user(db, "binky@gmail.com", "anotherpassword", "Binky")
task2 = model.new_task(db, "anothertask", 2)

task3 = model.new_task(db, "task again", 4)
