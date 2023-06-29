from flask import Flask, jsonify, request

app = Flask(__name__)


books_db = [
    {
       'name': 'Let Us C'
               , 'price': 430
    },

    {
        'name': 'Secret'
        , 'price': 300
    },
    {
        'name': 'The Power of the Sub-Conscious Mind'
        , 'price': 500
    }
]

# retrieve all books
@app.route('/books')
def get_all_books():
    return jsonify({'books': books_db})


# retrieve one book
@app.route('/book/<string:name>')
def get_book(name):
    for book in books_db:
        if book['name'] == name:
            return jsonify(book)

    return jsonify({'message': 'Book not found'})


# Create a book
@app.route('/book', methods=['POST'])
def create_book():
    body_data = request.get_json()
    books_db.append(body_data)

    return jsonify({"message": "Book has been created"})


app.run(port=5000)