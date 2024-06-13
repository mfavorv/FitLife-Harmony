from db.connect import get_db_connection

class Workout:
    all = {}

    def __init__(self,id, name ,scheduled_time ,trainer_id):
        self.id = id
        self.name = name
        self.scheduled_time = scheduled_time
        self.trainer_id = trainer_id
        Workout.all[self.id] = self
    
    def __repr__(self) :
        return (
            f"<Workout {self.id}:{self.name}> " 
        )

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = '''
              INSERT INTO workouts (name, scheduled_time ,trainer_id)
              VALUES (? ,?, ? )
              '''         
        cursor.execute(sql,(self.name,  self.scheduled_time, self.trainer_id,))
        self.id = cursor.lastrowid
        conn.commit()
        conn.close()

    @classmethod
    def add(cls, name ,scheduled_time ,trainer_id):
       workout = cls(None, name ,scheduled_time ,trainer_id )
       workout.save()
       return workout

    def delete(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = '''
            DELETE FROM workouts 
            WHERE id = ?
       '''
        cursor.execute(sql,(self.id, ))
        del type(self).all[self.id]
        self.id = None

        conn.commit()
        conn.close()

    def update(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """
            UPDATE workouts
            SET name = ?, scheduled_time = ?, trainer_id = ?
            WHERE id = ?
        """
        cursor.execute(sql, (self.name, self.scheduled_time, self.trainer_id, self.id)) 
        conn.commit()

    @classmethod
    def single_workout(cls, row):

        id = row[0]
        name = row[1]
        scheduled_time = row[2]
        trainer_id = row[3]

        workout = cls.all.get(id)
        if workout:
            workout.name = name
            workout.scheduled_time = scheduled_time
            workout.trainer_id = trainer_id
        else:
            workout = cls(id, name, scheduled_time, trainer_id)

        return workout
    
    @classmethod
    def search_by_id(cls, id):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql ='''
            SELECT * 
            FROM workouts 
            WHERE id = ?
        '''

        row = cursor.execute(sql, (id,)).fetchone()
        return cls.single_workout(row) if row else None

    @classmethod
    def search_by_time(cls, time):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql ='''
            SELECT * 
            FROM workouts 
            WHERE strftime('%H:%M', scheduled_time) =  ?
        '''

        rows = cursor.execute(sql, (time,)).fetchall()
        return [cls.single_workout(row) for row in rows ]

    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = '''
            SELECT *
            FROM workouts
        '''
        rows = cursor.execute(sql).fetchall()
        return [cls.single_workout(row) for row in rows]