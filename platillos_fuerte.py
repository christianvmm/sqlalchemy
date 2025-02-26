from session import session
from models import PlatillosFuerte
import uuid

def print_platofuerte(platofuerte):
    print(platofuerte.id_platofuerte, platofuerte.nombre, platofuerte.descripcion)

def get_platillos_fuertes():
    platillos = session.query(PlatillosFuerte).all()
    return platillos

def get_platofuerte_by_id(id):
    platofuerte = session.get(PlatillosFuerte, id)
    return platofuerte

def insert_platofuerte():
    platofuerte = PlatillosFuerte(
        id_platofuerte=str(uuid.uuid4()),
        nombre="Filete Mignon",
        descripcion="Filete de res envuelto en tocino con salsa de champiñones"
    )
    session.add(platofuerte)
    session.commit()
    print("Platillo fuerte creado")
    return platofuerte

def delete_platofuerte(id):
    platofuerte = get_platofuerte_by_id(id)
    if platofuerte:
        session.delete(platofuerte)
        session.commit()
        print("Platillo fuerte eliminado")

def update_platofuerte(id):
    platofuerte = get_platofuerte_by_id(id)
    if platofuerte:
        platofuerte.descripcion = "Filete de res envuelto en tocino con reducción de vino tinto y champiñones"
        session.commit()
        print("Platillo fuerte actualizado")