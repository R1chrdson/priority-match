from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

@app.cli.command('create-db')
def create_db():
    with app.app_context():
        db.create_all()
