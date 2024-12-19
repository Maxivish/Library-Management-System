# app.py
from flask import Flask, request, jsonify
from models import Book, Member
from config import Config
from functools import wraps

app = Flask(__name__)
app.config.from_object(Config)

# Token-based authentication
def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing'}), 403
        if token != 'your_secret_token':  # Replace with actual token logic
            return jsonify({'message': 'Token is invalid'}), 403
        return f(*args, **kwargs)
    return decorated_function

# Default route (index)
@app.route('/')
def index():
    return jsonify({
        'message': 'Welcome to the Library Management System API!',
        'available_routes': [
            '/books - GET all books',
            '/books/<book_id> - GET a specific book by ID',
            '/books - POST a new book',
            '/books/<book_id> - PUT to update a book',
            '/books/<book_id> - DELETE to remove a book',
            '/members - GET all members',
            '/members - POST a new member'
        ]
    })

# Route to get all books (with pagination)
@app.route('/books', methods=['GET'])
def get_books():
    page = request.args.get('page', 1, type=int)
    limit = Config.PAGINATION_LIMIT
    offset = (page - 1) * limit
    books = Book.get_all(limit, offset)
    return jsonify(books)

# Route to get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.get_by_id(book_id)
    if book:
        return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404

# Route to create a new book (requires token)
@app.route('/books', methods=['POST'])
@token_required
def create_book():
    data = request.get_json()
    if not data.get('title') or not data.get('author'):
        return jsonify({'message': 'Title and author are required'}), 400
    Book.create(data['title'], data['author'], data['year'])
    return jsonify({'message': 'Book created successfully'}), 201

# Route to update a book by ID (requires token)
@app.route('/books/<int:book_id>', methods=['PUT'])
@token_required
def update_book(book_id):
    data = request.get_json()
    if not data.get('title') or not data.get('author'):
        return jsonify({'message': 'Title and author are required'}), 400
    Book.update(book_id, data['title'], data['author'], data['year'])
    return jsonify({'message': 'Book updated successfully'})

# Route to delete a book by ID (requires token)
@app.route('/books/<int:book_id>', methods=['DELETE'])
@token_required
def delete_book(book_id):
    Book.delete(book_id)
    return jsonify({'message': 'Book deleted successfully'})

# Route to search for books by title or author
@app.route('/books/search', methods=['GET'])
def search_books():
    query = request.args.get('query', '', type=str)
    page = request.args.get('page', 1, type=int)
    limit = Config.PAGINATION_LIMIT
    offset = (page - 1) * limit
    books = Book.search_by_title_or_author(query, limit, offset)
    return jsonify(books)

# Route to get all members (with pagination)
@app.route('/members', methods=['GET'])
def get_members():
    page = request.args.get('page', 1, type=int)
    limit = Config.PAGINATION_LIMIT
    offset = (page - 1) * limit
    members = Member.get_all(limit, offset)
    return jsonify(members)

# Route to create a new member (requires token)
@app.route('/members', methods=['POST'])
@token_required
def create_member():
    data = request.get_json()
    if not data.get('name') or not data.get('email'):
        return jsonify({'message': 'Name and email are required'}), 400
    Member.create(data['name'], data['email'])
    return jsonify({'message': 'Member created successfully'}), 201

if __name__ == '__main__':
    from database import init_db
    init_db()
    app.run(debug=True)
