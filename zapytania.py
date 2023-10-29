class Person:

    def __init__(self, id=None, first_name='', last_name='', b_year=0):
        self._id = id
        self.first_name = first_name
        self.last_name = last_name
        self.b_year = b_year

    @classmethod
    def get_persons(cls):
        query = """
                SELECT * FROM person;
            """
        cursor.execute(query)
        persons_tuples = cursor.fetchall()
        persons = []
        for p in persons_tuples:
            new_person = Person(p[0], p[1], p[2], p[3])
            persons.append(new_person)
        return persons

    def save(self):
        if self._id is None:
            query = f"""
            INSERT INTO person (first_name, last_name,b_year) VALUES
            ('{self.first_name}', '{self.last_name}', {self.b_year})
            returning id; 
            """
            cursor.execute(query)
            id = cursor.fetchone()
            self._id = id
        else:
            query = f"""
            UPDATE person SET
            first_name = '{self.first_name}',
            last_name = '{self.last_name}',
            b_year = {self.b_year}
            WHERE id = {self._id}
            """
            cursor.execute(query)


def get_all_persons(cursor):
    query = """
        SELECT * FROM person;
    """
    cursor.execute(query)
    return cursor.fetchall()


def add_person(first_name, last_name, b_year, cursor):
    query = f"""
        INSERT INTO person (first_name,last_name, b_year) VALUES ('{first_name}', '{last_name}', {b_year}) 
        RETURNING id;
    """
    cursor.execute(query)
    return cursor.fetchone()


def delete_person(id, cursor):
    query = f"""
    DELETE FROM person where id={id}
    """
    cursor.execute(query)


def update_person(id, first_name, last_name, b_year, cursor):
    query = f"""
    UPDATE person SET
    first_name = '{first_name}',
    last_name = '{last_name}',
    b_year = {b_year}
    WHERE id={id}
    """
    cursor.execute(query)
if __name__ == '__main__':
    from polaczenie import connect
    c = connect()
    cursor = c.cursor()


    # p = Person(first_name='Kuba', last_name='rozpruwacz', b_year=666)
    # p.save()

    osoby = Person.get_persons()
    for o in osoby:
        print(o._id, o.first_name, o.last_name, o.b_year)

    k = osoby[-1]
    k.b_year = 1666
    k.save()
    osoby = Person.get_persons()
    for o in osoby:
        print(o._id, o.first_name, o.last_name, o.b_year)

