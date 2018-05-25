from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)


@app.route('/', methods=['GET', 'POST'])
def sessions():
    return render_template('session.html')


def messageRecived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('message')
def handle_message(message, methods=['GET', 'POST']):
    print('received message: ' + message)
    send(message, broadcast=True)


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('recived my event: ' + str(json))
    socketio.emit('my response', json, callback=messageRecived)


if __name__ == '__main__':
    socketio.run(app, debug=True)
