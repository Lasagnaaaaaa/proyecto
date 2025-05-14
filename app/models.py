from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize SQLAlchemy
db = SQLAlchemy()

# Role model
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

# User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    role = db.relationship('Role', backref='users')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_admin(self):
        return self.role and self.role.name == 'Admin'

    def is_editor(self):
        return self.role and self.role.name == 'Editor'

    def is_author(self):
        return self.role and self.role.name == 'Autor'

# Article model
class Articulo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    contenido = db.Column(db.Text, nullable=False)
    categoria = db.Column(db.String(50), nullable=False, default='General')  # Default category
    fecha_publicacion = db.Column(db.Date, default=db.func.current_timestamp())  # Default to current timestamp
    estado = db.Column(db.Enum('Borrador', 'Publicado'), default='Borrador')

    autor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    autor = db.relationship('User', backref='articulos')

    # Optional: media (for images or files related to the article)
    imagen = db.Column(db.String(256))  # Can store a file path or URL for images
