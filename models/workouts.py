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