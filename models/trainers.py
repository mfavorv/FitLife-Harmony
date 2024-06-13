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