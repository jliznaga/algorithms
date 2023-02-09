from flask import Flask
from flask_socketio import SocketIO, emit, send


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
# app.debug = True
# app.host = 'localhost'


socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('connect')
def connect():	
	print('Connected')
	emit('my response', {'data': 'Connected'})


@socketio.on('message')
def handle_message(msg):
    print('received message: ' + msg)
    send(msg, broadcast=True)    

if __name__ == '__main__':
	socketio.run(app)
	# app.run()
