from db.connect import get_db_connection

class Member:
    all = {}

    def __init__(self, id, name, email, trainer_id, workout_id):
        self.id = id
        self.name = name
        self.email = email
        self.trainer_id = trainer_id
        self.workout_id = workout_id
        Member.all[self.id] = self

    def __repr__(self):
        return f"<Member {self.id}:{self.name}>"

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = '''
            INSERT INTO members (name, email, trainer_id, workout_id)
            VALUES (?, ?, ?, ?)
        '''
        cursor.execute(sql, (self.name, self.email, self.trainer_id, self.workout_id))
        self.id = cursor.lastrowid
        conn.commit()
        conn.close()

    @classmethod
    def add(cls, name, email, trainer_id, workout_id):
        member = cls(None, name, email, trainer_id, workout_id)
        member.save()
        return member