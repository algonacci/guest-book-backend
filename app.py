from flask import Flask, jsonify, request
from flask_cors import cross_origin
import time

app = Flask(__name__)

# in-memory database to store guest book entries
guest_book_entries = [
    {"name": "John Doe", "message": "Hello, world!", "timestamp": time.time()},
    {"name": "Jane Doe", "message": "Nice to meet you!", "timestamp": time.time()},
    {"name": "Bob Smith", "message": "Greetings from Bob!", "timestamp": time.time()}
]


@app.route("/")
def root():
    return jsonify({
        "status_code": 200,
        "message": "Success Fetching the API!"
    }), 200


@app.route("/guest-book")
@cross_origin()
def guest_book():
    # sort the guest book entries by timestamp in descending order
    sorted_entries = sorted(
        guest_book_entries, key=lambda entry: entry["timestamp"], reverse=True)
    return jsonify(sorted_entries)


@app.route("/add-message", methods=["POST"])
@cross_origin()
def add_message():
    # get the data from the request
    data = request.get_json()
    name = data["name"]
    message = data["message"]
    timestamp = time.time()

    # add the new guest book entry to the in-memory database
    guest_book_entries.append({
        "name": name,
        "message": message,
        "timestamp": timestamp
    })

    # return the updated list of guest book entries
    return jsonify(guest_book_entries), 200


if __name__ == "__main__":
    app.run()
