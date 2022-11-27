from flask import Flask, render_template

app = Flask(__name__)

books = ["Pan Tadeusz", "Krzyżacy"]


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
    books_list = [f"<li><a href='/books/{i}'>{book}</li>" for i, book in enumerate(books, start=1)]

    response = f"""
    <ul>
    {' '.join(books_list)}
    </ul>
    """

    return response
