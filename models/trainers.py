from db.connect import get_db_connection

class Trainer:
    all = {}

    def __init__(self, id, name, phone_number) :
        self.id = id
        self.name = name
        self.phone_number = phone_number
        Trainer.all[self.id] = self

    def __repr__(self) :
        return f"<Trainer {self.id}:{self.name}>"
    
    def save(self):
       conn = get_db_connection()
       cursor = conn.cursor()
       sql = '''
              INSERT INTO trainers (name,phone_number)
              VALUES (? ,?)
              '''         
       cursor.execute(sql,(self.name, self.phone_number, ))
       self.id = cursor.lastrowid
       conn.commit()
       conn.close()
    
    @classmethod
    def add(cls, name, phone_number):
        trainer = cls(None, name, phone_number )
        trainer.save()
        return trainer
    
    def delete(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = '''
            DELETE FROM trainers
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
            UPDATE trainers
            SET name = ?, phone_number = ?
            WHERE id = ?
        """
        cursor.execute(sql, (self.name, self.phone_number,  self.id))
        conn.commit()
        conn.close()

    @classmethod
    def single_trainer(cls, row):

        id = row[0]
        name = row[1]
        phone_number = row[2]

        trainer = cls.all.get(id)
        if trainer:
            trainer.name = name
            trainer.phone_number = phone_number
        else:
            trainer = cls(id, name, phone_number)

        return trainer
    
    @classmethod
    def search_by_name(cls, name):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql ='''
            SELECT * 
            FROM trainers 
            WHERE name = ?
        '''

        row = cursor.execute(sql, (name,)).fetchone()
        return cls.single_trainer(row) if row else None

    @classmethod
    def search_by_id(cls, id):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql ='''
            SELECT * 
            FROM trainers
            WHERE id is ?
        '''

        row = cursor.execute(sql, (id,)).fetchone()
        return cls.single_trainer(row) if row else None
    
    @classmethod
    def search_workout_by_trainer(cls, id):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = '''
            SELECT * FROM workouts
            WHERE trainer_id = ?
        '''
        cursor.execute(sql, (id,))
        rows = cursor.fetchall()
        conn.close()
        return rows
    