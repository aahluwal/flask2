CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  email VARCHAR(64),
  password VARCHAR(64),
  name VARCHAR(64)
  );

CREATE TABLE tasks (
  id INTEGER PRIMARY KEY,
  title VARCHAR(64),
  created_at DATETIME,
  completed_by DATETIME,
  user_id INTEGER
  );
