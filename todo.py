from flask import Flask, render_template, redirect, url_for,request
import os
import sqlite3

app = Flask(__name__)

def get_db(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

@app.route('/zadania', methods=['GET', 'POST'])
def zadania():
    error = None
    if request.method == 'POST':
        tytuł = request.form['tytuł'].strip()
        opis = request.form['opis'].strip()
        if len(tytuł) > 0:
            status = '0'
            db = get_db("zadania.sqlite")
            db.execute('INSERT INTO zadania VALUES (?, ?, ?, ?);',
                       [None, tytuł, opis, status])
            db.commit()
            return redirect(url_for('zadania'))

    cursor = get_db("zadania.sqlite").execute('SELECT * from zadania ORDER BY status desc;')
    zadania = cursor.fetchall()
    return render_template('zadania_lista.html', zadania=zadania, error=error)

@app.route('/zrobione', methods=['POST'])
def zrobione():
    zadanie_id = request.form['id']
    db = get_db("zadania.sqlite")
    db.execute('UPDATE zadania SET status=1 WHERE id=?', [zadanie_id])
    db.commit()
    return redirect(url_for('zadania'))

if __name__ == '__main__':
    app.run(debug=True)