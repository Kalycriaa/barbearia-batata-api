from flask import Flask
from database import db
from barbearia_batata.routes.route_clientes import barbearia_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///barberia.db'
db.init_app(app)

app.register_blueprint(barbearia_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug = True)
