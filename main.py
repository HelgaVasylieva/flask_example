from flask import Flask, request
from utils import get_requirements, get_generate_users, get_space, get_mean, get_password

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


@app.route('/password/')
def password():
    length = request.args.get('length') or '10'

    if length.isdigit():
        length = int(length)
        max_length = 200

        if length > max_length:
            return f'Max length should be less that {max_length}.'
    else:
        return f'Invalid parameter length {length}. Integer is expected.'

    result = get_password(length)
    return result


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
    