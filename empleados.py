from session import session
from models import Empleado
import uuid

def print_empleado(empleado):
    print(empleado.id_empleado, empleado.nombre, empleado.apellidos, empleado.telefono)

def get_empleados():
    empleados = session.query(Empleado).all()
    return empleados

def get_empleado_by_id(id):
    empleado = session.get(Empleado, id)
    return empleado

def insert_empleado():
    empleado = Empleado(
        id_empleado=str(uuid.uuid4()),
        nombre="Juan",
        apellidos="Pérez",
        telefono="523312223221"
    )
    session.add(empleado)
    session.commit()
    print("Empleado creado")

def delete_empleado(id):
    empleado = get_empleado_by_id(id)
    if empleado:
        session.delete(empleado)
        session.commit()
        print("Empleado eliminado")

def update_empleado(id):
    empleado = get_empleado_by_id(id)
    if empleado:
        empleado.telefono = "528899112233"
        session.commit()
        print("Empleado actualizado")

# ===============
# Create
# ===============
# insert_empleado()

# ===============
# List
# ===============
# empleados = get_empleados()
# for empleado in empleados:
#     print_empleado(empleado)

# ===============
# Get
# ===============
# empleados = get_empleados()
# empleado = get_empleado_by_id(empleados[0].id_empleado)
# print_empleado(empleado)

# ===============
# Update
# ===============
# empleados = get_empleados()
# update_empleado(empleados[0].id_empleado)

# ===============
# Delete
# ===============
# empleados = get_empleados()
# delete_empleado(empleados[0].id_empleado)
