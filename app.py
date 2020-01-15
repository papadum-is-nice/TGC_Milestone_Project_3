import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo, DESCENDING
from bson.objectid import ObjectId
import re

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'goodreads'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html', title="Home")
 
@app.route('/search_books/', methods=["GET", "POST"])
def search_books():
    post_request = request.args['query']
    return render_template("search_books.html",
                            title="Search Results",
                            query=post_request,
                            search_books=mongo.db.books.find({"$or":[{"title" : {"$regex": post_request, "$options": "i"}}, {"authors" : {"$regex": post_request, "$options": "i"}}]}).limit(12),
                            search_books_count=mongo.db.books.find({"title" : {"$regex": post_request, "$options": "i"}}).count())
    
@app.route('/get_books')
def get_books():
    books=mongo.db.books.find().sort([("_id", DESCENDING)]).limit(12)
    return render_template('books_collection.html', title="Books Collection", books=books)
    
@app.route('/add_book')
def add_book():
    return render_template('add_book.html', title="Add book")

@app.route('/insert_book', methods=['POST'])
def insert_book():
    book = mongo.db.books
    new_book = {
        'title': request.form.get('title'),
        'authors':request.form.get('authors'),
        'language_code':request.form.get('language_code'),
        'num_pages':int(request.form.get('num_pages')),
        'rating':int(request.form.get('rating')),
        'isbn13':int(request.form.get('isbn13'))
    }
    book.insert_one(new_book)
    return redirect(url_for('index'))    
    
@app.route('/edit_book/<book_id>', methods=['GET'])
def edit_book(book_id):
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template('edit_book.html', title="Edit book", book=book)

@app.route('/update_book/<book_id>', methods=["POST"])
def update_book(book_id):
    book = mongo.db.books.find_one({"_id:": ObjectId(book_id)})
    book.update( {'_id': ObjectId(book_id)},
    {
        'title': request.form.get('title'),
        'authors':request.form.get('authors'),
        'language_code':request.form.get('language_code'),
        'num_pages':int(request.form.get('num_pages')),
        'rating':int(request.form.get('rating')),
        'isbn13':int(request.form.get('isbn13'))
    })
    return redirect(url_for('get_books'))
    
@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    mongo.db.books.remove({'_id': ObjectId(book_id)})
    return redirect(url_for('get_books'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
