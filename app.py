from flask import Flask, request, abort

from util import create_hex_hash

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/<username>', methods=['GET'])
def identicon_generator(username: str):
    if not username.endswith(".png"):
        abort(400, "A png image should be requested. Read docs.")
    size = request.args.get('size', default=300, type=int)
    row = request.args.get('row', default=5, type=int)
    print("username: {}\t\t size: {}\t\t row: {}".format(username, size, row))
    # meta = {"username": username, "size": size, "row": row}
    return create_hex_hash(username)


@app.errorhandler(400)
def handle_bad_request(e: Exception):
    msg = str(e)
    return msg, 400


if __name__ == '__main__':
    app.run()
