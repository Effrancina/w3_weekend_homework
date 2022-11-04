from flask import render_template, request, redirect
from app import app
from models.library_books import books_list, add_new_book
# remember to add other functions here
from models.book import Book

@app.route('/books')
def index():
    return render_template('index.html', title='Home', books=books_list)

@app.route('/books', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    newbook = Book(title=title, author=author, genre=genre)
    add_new_book(newbook)
    return redirect('/books')

# add functions!