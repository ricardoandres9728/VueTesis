from application import create_app
from flask import session
from datetime import timedelta


app = create_app()


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)