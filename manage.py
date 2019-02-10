import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask_script import Manager, Server
from application import create_app
from flask_migrate import MigrateCommand
from flask import render_template

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server(
    use_debugger=True,
    use_reloader=True,
    host='127.0.0.1',
    port=5000
)
                    )


if __name__ == '__main__':
    manager.run()


def get_current_app():
    return app
