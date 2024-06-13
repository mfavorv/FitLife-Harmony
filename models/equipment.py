from db.connect import get_db_connection

class Equipment:
    all = {}

    def __init__(self,name ,user_id ,condition ,price ,quantity ):
        self.name = name
        self.user_id = user_id
        self.condition = condition
        self.price = price
        self.quantity = quantity
        Equipment.all[self.name] = self
    
    def __repr__(self) :
        return (
            f"<Equipment {self.name}:{self.quantity}> " 
        )

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = '''
              INSERT INTO equipment (name, user_id, condition, price, quantity)
              VALUES (?, ?, ?, ?, ?)
              '''
        cursor.execute(sql, (self.name, self.user_id, self.condition, self.price, self.quantity))
        self.id = cursor.lastrowid
        conn.commit()
        conn.close()

    @classmethod
    def add(cls, name, user_id, condition, price, quantity):
        equipment = cls(name,user_id, condition, price, quantity )
        equipment.save()
        return equipment

    def delete(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = '''
            DELETE FROM equipment 
            WHERE name = ?
       '''
        cursor.execute(sql,(self.name, ))
        del type(self).all[self.name]
        self.name = None

        conn.commit()
        conn.close()

    def update(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """
            UPDATE equipment
            SET name = ?, user_id = ?, condition = ?, price = ?, quantity = ?
            WHERE name = ?
        """
        cursor.execute(sql, (self.name, self.user_id, self.condition, self.price, self.quantity, self.name))
        conn.commit()
        conn.close()
