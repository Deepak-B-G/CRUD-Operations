from flask import Flask,jsonify,request

app = Flask(__name__)

books = [
    {"id":1, "Title":"book1", "Author": "Author1"},
    {"id":2, "Title":"book2", "Author": "Author2"},
    {"id":3, "Title":"book3", "Author": "Author3"}
]

# GET all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# GET individual book
@app.route('/books/<int:book_id>',methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return book
    return{'error':'Book not found'}

# CREATE a book
@app.route('/books', methods=['POST'])
def create_book():
    new_book = {'id':len(books)+1, 'Title':request.json['Title'], 'Author':request.json['Author']}
    books.append(new_book)
    return new_book
            
#UPDATE a book
@app.route('/books/<int:book_id>', methods=["PUT"])
def update_book(book_id):
    for book in books:
        if book['id'] == book_id:
            book['Title'] = request.json['Title']
            book['Author'] = request.json['Author']
            return book
    return {'Error':'Book not found'}

# DELETE a book
@app.route('/books/<int:book_id>', methods=["DELETE"])
def delete_book(book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {"data": "Book Deleted Successfully"}
    return{'error':'Book not found'}


if __name__ == '__main__':
    app.run(debug=True)