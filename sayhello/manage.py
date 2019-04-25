from flask_script import Manager
from sayhello import app,db
from flask_migrate import Migrate,MigrateCommand
from sayhello.models import Comment


manager = Manager(app)
migrate = Migrate(app,db)



manager.add_command("db",MigrateCommand)

if __name__ == "__main__":
    manager.run()
