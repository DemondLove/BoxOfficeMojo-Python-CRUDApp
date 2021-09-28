import os
from bom import create_app, db
from bom.models import Title
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.shell_context_processor
def makeShellContext():
    return dict(db=db, Title=Title)