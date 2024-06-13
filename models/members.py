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

    def delete(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = '''
            DELETE FROM members
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
            UPDATE members
            SET   name = ?  , email =? , trainer_id = ? , workout_id = ?
            WHERE id = ?
        """
        cursor.execute(sql, (self.name, self.email, self.trainer_id, self.workout_id,self.id))
        conn.commit()


    @classmethod
    def single_member(cls, row):
        """Return a Member object having the attribute values from the table row."""
        
        # Ensure the input row has the correct length
        if len(row) != 5:
            raise ValueError("Row must have exactly 5 elements: id, name, email, trainer_id, workout_id")

        member_id = row[0]
        name = row[1]
        email = row[2]
        trainer_id = row[3]
        workout_id = row[4]

        member = cls.all.get(member_id)
        if member:
            member.name = name
            member.email = email
            member.trainer_id = trainer_id
            member.workout_id = workout_id
        else:
            member = cls(member_id, name, email, trainer_id, workout_id)

        return member

    @classmethod
    def search_by_name(cls, name):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql ='''
            SELECT * 
            FROM members 
            WHERE name = ?
        '''

        row = cursor.execute(sql, (name,)).fetchone()
        return cls.single_member(row) if row else None

    @classmethod
    def search_by_id(cls, id):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql ='''
            SELECT * 
            FROM members 
            WHERE id = ?
        '''

        row = cursor.execute(sql, (id,)).fetchone()
        return cls.single_member(row) if row else None
    
    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = '''
            SELECT *
            FROM members
        '''
        rows = cursor.execute(sql).fetchall()
        return [cls.single_member(row) for row in rows]