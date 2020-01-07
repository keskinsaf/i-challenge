from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/<username>', methods=['GET'])
def identicon_generator(username):
    print(username)
    size = request.args.get('size', default=300, type=int)
    row = request.args.get('row', default=5, type=int)
    print("username: {}\t\t size: {}\t\t row: {}".format(username, size, row))
    meta = {"username": username, "size": size, "row": row}
    return meta


if __name__ == '__main__':
    app.run()
