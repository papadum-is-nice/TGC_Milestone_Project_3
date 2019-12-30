import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'goodreads'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@cluster0-y00j5.mongodb.net/goodreads?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_books')
def get_books():
    return render_template("books.html", books=mongo.db.books.find())
    
# @app.route('/')
# @app.route('/add_book')
# def add_book():
#     return render_template('edit_books.html', categories=mongo.db.books.find())

# @app.route('/')
# @app.route('/insert_book', methods=['POST'])
# def insert_task():
#     tasks = mongo.db.books
#     tasks.insert_one(request.form.to_dict())
#     return redirect(url_for('get_books'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
