from flask import Flask, request, abort, send_file
from io import BytesIO
from util import create_hex_hash, generate_image_from_hash

app = Flask(__name__)

MAX_SIZE = 500
ALLOWED_ROWS = {3: True, 5: True, 7: True}


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/<username>', methods=['GET'])
def identicon_generator(username: str):
    if not username.endswith(".png"):
        abort(400, "A png image should be requested. Read docs.")
    size = abs(request.args.get('size', default=300, type=int))
    row = abs(request.args.get('row', default=5, type=int))

    if row in ALLOWED_ROWS:
        print("Row: {} is allowed.".format(row))
    else:
        print("Row: {} is not allowed. Will be set to 5.".format(row))
        row = 5

    if size <= MAX_SIZE:
        print("Size: {} is allowed.".format(size))
    else:
        print("Size: {} is not allowed. Will be set to {}.".format(size, MAX_SIZE))
        size = MAX_SIZE

    row = row if row in ALLOWED_ROWS else 5

    print("username: {}\t\t size: {}\t\t row: {}".format(username, size, row))
    hex_hash = create_hex_hash(username)
    identicon = generate_image_from_hash(hex_hash, size, row)
    # identicon.save("images/l_" + username, "png") # saving locally

    bin_img = BytesIO()
    identicon.save(bin_img, 'png')
    bin_img.seek(0)
    return send_file(bin_img, mimetype='image/png')


@app.errorhandler(400)
def handle_bad_request(e: Exception):
    msg = str(e)
    return msg, 400


if __name__ == '__main__':
    app.run()
