from flask import Flask

app = Flask(__name__)

books = ["Pan Tadeusz", "Krzyżacy"]


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/books/")
def books_list():
    books_list = [f"<li><a href='/books/{i}'>{book}</li>" for i, book in enumerate(books, start=1)]

    response = f"""
    <ul>
    {' '.join(books_list)}
    </ul>
    """

    return response
