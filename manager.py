import os

from flask_script import Server, Manager
from flask_migrate import Migrate, MigrateCommand


from app import app

app.config.from_object(os.environ['APP_SETTINGS'])


manager = Manager(app)

manager.add_command("runserver", Server(host='0.0.0.0', port='5000'))

if __name__ == '__main__':
	manager.run()