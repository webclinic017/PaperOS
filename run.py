import os
from app import create_app, db
from app.models import Role, User
from flask_migrate import Migrate


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Role=Role, User=User)


if __name__ == '__main__':
    app.run()
    app.debug(True)