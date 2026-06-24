from database import db
from barbearia_batata.models.barbearia_clientes import Clientes

def listar_clientes():
    clientes = Clientes.query.all()
    
    return [cliente.to_dict() for cliente in clientes]

def listar_clientes_id(id):
    cliente = db.session.get(Clientes, id)
    if not cliente:
        return None
    
    return cliente.to_dict()

def incluir_cliente(dados):
   novo_cliente = Clientes(
      nome = dados.get("nome"),
      horario = dados.get("horario"),
      data = dados.get("data")
   )
   
   db.session.add(novo_cliente)
   db.session.commit()
   
   return novo_cliente.to_dict()

def atualizar_cliente(dados, id):
    cliente = db.session.get(Clientes, id)
    if not cliente:
        return None
    
    Clientes.nome = dados.get("nome")
    Clientes.horario = dados.get("horario")
    Clientes.data = dados.get("data")

    db.session.commit()

    return cliente.to_dict()

def deletar_cliente(id):
    cliente = db.session.get(Clientes, id)
    if not cliente:
        return None
    
    db.session.delete(cliente)
    db.session.commit()

    return {"sucesso": "cliente removido com exito."}