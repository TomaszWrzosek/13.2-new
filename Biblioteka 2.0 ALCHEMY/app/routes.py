from flask import Flask, render_template, redirect, url_for,request
import os, db
import sqlite3

app = Flask(__name__)

@app.route("/library2", methods=["GET","POST"])
def add_book():
    author = request.form["title"]
    title = request.form["title"]

    book = Book(author=author, title=title)
    db.session.add(book)
    db.session.commit()

@app.route("/delete2", methods=["GET","POST"])
def delete_book():
    book = Book.query.get(book_id)
    db.session.delete(video)
    db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)