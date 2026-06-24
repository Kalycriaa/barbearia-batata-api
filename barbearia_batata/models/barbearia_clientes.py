from database import db

class Clientes(db.Model):
    __tablename__ = "clientes"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String(50), nullable = False)
    horario = db.Column(db.String(5), nullable = False)
    data = db.Column(db.String(10), nullable = False)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "horario": self.horario,
            "data": self.data
        }