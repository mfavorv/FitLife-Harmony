from .connect import get_db_connection

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            trainer_id INTEGER,
            workout_id INTEGER,
            FOREIGN KEY (trainer_id) REFERENCES trainers (id),
            FOREIGN KEY (workout_id) REFERENCES workouts (id)
              )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS trainers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone_number TEXT
              )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            scheduled_time TEXT,
            trainer_id INTEGER,
            FOREIGN KEY (trainer_id) REFERENCES trainers (id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS equipment (
            name TEXT NOT NULL,
            user_id INTEGER,
            condition TEXT NOT NULL,
            price INTEGER,
            quantity INTEGER,
            PRIMARY KEY (name, user_id),
            FOREIGN KEY (user_id) REFERENCES members (id)
        )
    ''')


    conn.commit()
    conn.close()