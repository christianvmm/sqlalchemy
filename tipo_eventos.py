from session import session
from models import TipoEvento
import uuid

def print_tipo_evento(tipo_evento):
    print(tipo_evento.id_tipo, tipo_evento.nombre)

def get_tipos_evento():
    tipos_evento = session.query(TipoEvento).all()
    return tipos_evento

def get_tipo_evento_by_id(id):
    tipo_evento = session.get(TipoEvento, id)
    return tipo_evento

def insert_tipo_evento():
    tipo_evento = TipoEvento(
        id_tipo=str(uuid.uuid4()),
        nombre="Conferencia"
    )
    session.add(tipo_evento)
    session.commit()
    print("Tipo de evento creado")
    return tipo_evento

def delete_tipo_evento(id):
    tipo_evento = get_tipo_evento_by_id(id)
    if tipo_evento:
        session.delete(tipo_evento)
        session.commit()
        print("Tipo de evento eliminado")

def update_tipo_evento(id, nuevo_nombre):
    tipo_evento = get_tipo_evento_by_id(id)
    if tipo_evento:
        tipo_evento.nombre = nuevo_nombre
        session.commit()
        print("Tipo de evento actualizado")
