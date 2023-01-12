from flask import Flask, request
from utils import get_requirements, get_generate_users, get_space, get_mean

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/requirements/')
def requirements():
    result = get_requirements()
    return result


@app.route('/generate-users/')
def generate_users():
    length = request.args.get('length') or '100'

    if length.isdigit():
        length = int(length)

    else:
        return f'Invalid parameter length {length}. Integer is expected.'

    result = get_generate_users(length)
    return str(result)


@app.route('/space/')
def space():
    result = get_space()
    return str(result)


@app.route('/mean/')
def mean():
    result = get_mean()
    return str(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    