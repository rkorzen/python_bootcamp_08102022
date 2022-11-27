from flask import Flask, render_template, abort
from dataclasses import dataclass

app = Flask(__name__)


@dataclass
class Book:
    title: str
    author: str
    desc: str


b1 = Book("Krzyżacy", "Henryk Sienkiewcz", "Zmagania ze złym komturem")
b2 = Book("Pan Tadeusz", "Adam Mickiewicz", "Epopeja narodowa")

books = [b1, b2]


@app.route("/")
def hello_world():
    return render_template(
        "main.html",
        x=2,
        y=2,
        lista=["a", "b", "c"],
        dane={"x": "wartośc x", "y": 10}
    )


@app.route("/books/")
def books_list():
    return render_template("books.html", books=books)


@app.route("/books/<int:book_id>")
def book_details(book_id):
    try:
        book = books[book_id - 1]
    except IndexError:
        abort(404)

    return render_template(
        "book_details.html",
        book=book
    )
