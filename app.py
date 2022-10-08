from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__, static_folder='./build', static_url_path='/')
cors = CORS(app)


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.get('/api/users')
def return_all_users():
    return users


@app.get('/api/users/<user>')
def return_user(user):
    return f'User {user}'


@app.post('/api/users')
def add_user():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return f"Add user {json['user']}"
    else:
        return 'Content-Type not supported.'


@app.get('/api/channels')
def return_all_channels():
    return channels


@app.get('/api/messages')
def return_all_messages():
    return messages


@app.post('/api/messages')
def add_message():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return f"Add message {json['message']}"
    else:
        return 'Content-Type not supported.'


# BEGIN DUMMY DATA
users = ['eric', 'other_guy', 'Jimmy J']
messages = [
  {
    'id': 1,
    'user': 'eric',
    'text': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Saepe cupiditate cum aut distinctio, rem voluptatibus beatae, unde odit ad suscipit magni dignissimos veniam ea dolorum.'
  },
  {
    'id': 2,
    'user': 'other_guy',
    'text': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Saepe cupiditate cum aut distinctio, rem voluptatibus beatae, unde odit ad suscipit magni dignissimos veniam ea dolorum.'
  },
  {
    'id': 3,
    'user': 'eric',
    'text': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Saepe cupiditate cum aut distinctio, rem voluptatibus beatae, unde odit ad suscipit magni dignissimos veniam ea dolorum.'
  },
  {
    'id': 4,
    'user': 'other_guy',
    'text': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Saepe cupiditate cum aut distinctio, rem voluptatibus beatae, unde odit ad suscipit magni dignissimos veniam ea dolorum.'
  },
  {
    'id': 5,
    'user': 'eric',
    'text': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Saepe cupiditate cum aut distinctio, rem voluptatibus beatae, unde odit ad suscipit magni dignissimos veniam ea dolorum.'
  },
  {
    'id': 6,
    'user': 'other_guy',
    'text': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Saepe cupiditate cum aut distinctio, rem voluptatibus beatae, unde odit ad suscipit magni dignissimos veniam ea dolorum.'
  }
]
channels = ['General', 'Random', 'Off-topic']
# END DUMMY DATA


if __name__ == '__main__':
    app.run(debug=True)
