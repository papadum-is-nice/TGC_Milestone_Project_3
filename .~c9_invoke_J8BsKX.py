import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo, DESCENDING
from bson.objectid import ObjectId
import re

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'goodreads'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@cluster0-y00j5.mongodb.net/goodreads?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html', title="Home")
    
    
@app.route('/get_books')
def get_books():
    books=mongo.db.books.find()
    return render_template('books_collection.html', title="Books Collection", books=books)
    
@app.route('/add_book')
def add_book():
    return render_template('add_book.html', title="Add book")

@app.route('/insert_book', methods=['POST'])
def insert_book():
    book = mongo.db.books
    new_book = {
        'Brand': request.form.get('Brand'),
        'Flavour':request.form.get('Flavour'),
        'Style': request.form.get('Style'),
        'Country':request.form.get('Country'),
        'Stars':int(request.form.get('Stars')),
        'Ratings':request.form.get('Ratings')
    }
    ramens.insert_one(new_ramen)
    return redirect(url_for('get_ramen'))    
    
@app.route('/edit_book/<book_id>', methods=['GET'])
def edit_book(book_id):
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template('edit_book.html', title="Edit book", book=book)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
