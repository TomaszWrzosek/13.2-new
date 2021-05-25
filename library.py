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

@app.route('/')
def index():
    return render_template('firstpage.html')

@app.route('/library', methods=['GET', 'POST'])
def library():
    error = None
    if request.method == 'POST':
        Author = request.form['Author'].strip()
        Title = request.form['Title'].strip()
        if len(Title) > 0:
            Status = '0'
            db = get_db("library.sqlite")
            db.execute('INSERT INTO library VALUES (?, ?, ?, ?);',
                       [None, Author, Title, Status])

            db.execute('INSERT INTO author VALUES (?, ?, ?);',
                       [None, Title, Status])
            db.commit()
            return redirect(url_for('library'))

    cursor = get_db("library.sqlite").execute('SELECT * from library ORDER BY status desc;')
    library = cursor.fetchall()
    return render_template('library_list.html', library=library, error=error)

@app.route('/status', methods=['POST'])
def status():
    library_id = request.form['id']
    db = get_db("library.sqlite")
    db.execute('UPDATE library SET status=1 WHERE id=?', [library_id])
    db.commit()
    return redirect(url_for('library'))

@app.route('/delete', methods=['POST'])
def delete():
    library_id = request.form['id']
    db = get_db('library.sqlite')
    db.execute('DELETE FROM library WHERE id=?', [library_id])
    db.commit()
    return redirect(url_for('library'))

if __name__ == '__main__':
    app.run(debug=True)