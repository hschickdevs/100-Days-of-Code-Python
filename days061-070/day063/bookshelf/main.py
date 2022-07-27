from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from werkzeug.datastructures import MultiDict

from backend.forms import AddBookForm, EditBookForm
from backend.database import LibraryDatabase

app = Flask(__name__)
app.secret_key = 'super_secret_key'
Bootstrap(app)
database = LibraryDatabase()


@app.route('/')
def home():
    all_books = database.load_books()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddBookForm()
    if form.validate_on_submit():
        database.add_book(id=int(database.load_books()[-1]['id']) + 1, title=form.name.data, author=form.author.data, 
                          rating=form.rating.data, icon_url=form.icon.data)
        return render_template("index.html", books=database.load_books())
    
    return render_template('add.html', form=form)

@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    book = database.load_books(id=book_id)[0]
    
    # Pass default values to the form for existing book data
    form = EditBookForm(data=MultiDict(book))
    
    if form.validate_on_submit():
        database.update_book(book_id, form.title.data, form.author.data, form.rating.data, form.icon.data)
        return render_template("index.html", books=database.load_books())
    
    return render_template('edit.html', form=form, book=book)

@app.route("/delete/<int:book_id>", methods=["GET", "POST"])
def delete(book_id):
    database.remove_book(id=book_id)
    
    return render_template('index.html', books=database.load_books())


if __name__ == "__main__":
    app.run(debug=True)

