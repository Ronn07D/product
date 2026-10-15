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

def insert_product():
    with app.app_context():
        p1 = Product(name="Laptop",price=4500.50,stock=10)
        p2 = Product(name="celular",price=3500.50,stock=5)
        p3 = Product(name="pantalla",price=2500.50,stock=3)

        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)

        db.session.commit()
        print("Producto insertado")

def query_products():
    with app.app_context():
        print("listsa de productos")
        productos = Product.query.all()
        for p in productos:
            print(p)

        print("\nobtencion de un solo producto")
        producto = Product.query.filter_by(id=2).first()

        if producto:
            print(producto)

if __name__ == "__main__":
    #init_db()
    #insert_product()
    query_products()
    #update_product()
    #delete_product()