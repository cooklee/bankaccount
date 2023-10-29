from flask import Flask, request

from polaczenie import connect
from zapytania import add_person, get_all_persons

app = Flask(__name__)
MENU = """
<ul>
<li><a href='/dodaj'>Dodaj</a></li>
<li><a href='/wyswietl'>wyświetl</a></li>
</ul>
"""

@app.route('/')
def hello_world():  # put application's code here
    return f'{MENU} Hello World!'

@app.route('/dodaj', methods=['GET', 'POST'])
def dodaj_osobe():
    if request.method == 'GET':
        form = """
        <FORM method='post'>
        <input type='text' name='first_name'>
        <input type='text' name='last_name'>
        <input type='text' name='b_year'>
        <input type='submit' name='b_year'>
        </FORM>
        """
        return f"{MENU} {form}"
    imie = request.form.get('first_name')
    nazwisko = request.form.get('last_name')
    b_year = request.form.get('b_year')
    connection = connect()
    cursor = connection.cursor()
    add_person(imie, nazwisko, b_year, cursor)

    return f'udało sie dodać osbe'

@app.route('/wyswietl')
def show_person():
    connection = connect()
    cursor = connection.cursor()
    persons = get_all_persons(cursor)
    cursor.close()
    connection.close()
    lst = "<ul>"
    for osoba in persons:
        lst += f"<li>{osoba}</li>"
    lst += '</ul>'
    return f'{MENU} {lst}'




if __name__ == '__main__':
    app.run()
