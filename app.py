from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///almacen.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self.stock})"


def init_db():
    with app.app_context():
        db.create_all()
        print("Tablas creadas exitosamente")


if __name__ == "__main__":
    init_db()
    #insert_product()
    #query_products()
    #update_product()
    #delete_product()