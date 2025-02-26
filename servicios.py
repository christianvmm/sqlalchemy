from session import session
from models import Servicio
import uuid

def print_servicio(servicio):
    print(servicio.id_servicio, servicio.tipo, servicio.precio_fijo)

def get_servicios():
    servicios = session.query(Servicio).all()
    return servicios

def get_servicio_by_id(id):
    servicio = session.get(Servicio, id)
    return servicio

def insert_servicio():
    servicio = Servicio(
        id_servicio=str(uuid.uuid4()),
        tipo="Spa",
        precio_fijo=50.0
    )
    session.add(servicio)
    session.commit()
    print("Servicio creado")

def delete_servicio(id):
    servicio = get_servicio_by_id(id)
    if servicio:
        session.delete(servicio)
        session.commit()
        print("Servicio eliminado")

def update_servicio(id):
    servicio = get_servicio_by_id(id)
    if servicio:
        servicio.precio_fijo = 60.0
        session.commit()
        print("Servicio actualizado")

# ===============
# Create
# ===============
# insert_servicio()

# ===============
# List
# ===============
# servicios = get_servicios()
# for servicio in servicios:
#     print_servicio(servicio)

# ===============
# Get
# ===============
# servicios = get_servicios()
# servicio = get_servicio_by_id(servicios[0].id_servicio)
# print_servicio(servicio)

# ===============
# Update
# ===============
# servicios = get_servicios()
# update_servicio(servicios[0].id_servicio)

# ===============
# Delete
# ===============
# servicios = get_servicios()
# delete_servicio(servicios[0].id_servicio)
