from flask import render_template, request, redirect, url_for
from web_dev import app, db
from web_dev import models

@app.route('/')
def index():
    books = models.Book.query.all()
    return render_template('index.html', books=books)

@app.route('/add_book', methods=['POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        new_book = models.Book(title=title, author=author)

        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/edit_book/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    book = models.Book.query.get(book_id)
    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']

        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_book.html', book=book)

@app.route('/delete_book/<int:book_id>')
def delete_book(book_id):
    book = models.Book.query.get(book_id)

    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('index'))