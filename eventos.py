from session import session
from models import Evento
import uuid

def print_evento(evento):
    print(evento.id_evento, evento.nombre, evento.descripcion, evento.fecha, evento.id_organizador)

def get_eventos():
    eventos = session.query(Evento).all()
    return eventos

def get_evento_by_id(id):
    evento = session.get(Evento, id)
    return evento

def insert_evento():
    evento = Evento(
        id_evento=str(uuid.uuid4()),
        nombre="Conferencia Tech 2025",
        descripcion="Evento sobre las últimas tendencias en tecnología.",
        fecha="2025-06-15",
        id_organizador="123e4567-e89b-12d3-a456-426614174000"  # Reemplazar con un ID válido
    )
    session.add(evento)
    session.commit()
    print("Evento creado")

def delete_evento(id):
    evento = get_evento_by_id(id)
    if evento:
        session.delete(evento)
        session.commit()
        print("Evento eliminado")

def update_evento(id):
    evento = get_evento_by_id(id)
    if evento:
        evento.descripcion = "Evento actualizado con nuevos ponentes."
        session.commit()
        print("Evento actualizado")

# ===============
# Create
# ===============
# insert_evento()

# ===============
# List
# ===============
# eventos = get_eventos()
# for evento in eventos:
#     print_evento(evento)

# ===============
# Get
# ===============
# eventos = get_eventos()
# evento = get_evento_by_id(eventos[0].id_evento)
# print_evento(evento)

# ===============
# Update
# ===============
# eventos = get_eventos()
# update_evento(eventos[0].id_evento)

# ===============
# Delete
# ===============
# eventos = get_eventos()
# delete_evento(eventos[0].id_evento)
