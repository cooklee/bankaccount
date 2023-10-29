



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
