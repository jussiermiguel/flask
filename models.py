from flask_sqlalchemy import SQLAlchemy
from app import app

# Configurando o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/bdteste'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Chave primária
    username = db.Column(db.String(80), unique=True, nullable=False)  # Campo obrigatório e único
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
