from session import session
from models import Hotel
import uuid

def print_hotel(hotel):
    print(hotel.id_hotel, hotel.nombre, hotel.direccion, hotel.estrellas)

def get_hoteles():
    hoteles = session.query(Hotel).all()
    return hoteles

def get_hotel_by_id(id):
    hotel = session.get(Hotel, id)
    return hotel

def insert_hotel():
    hotel = Hotel(
        id_hotel=str(uuid.uuid4()),
        nombre="Hotel Paradise",
        direccion="Av. Principal #123",
        estrellas=5
    )
    session.add(hotel)
    session.commit()
    print("Hotel creado")

def delete_hotel(id):
    hotel = get_hotel_by_id(id)
    if hotel:
        session.delete(hotel)
        session.commit()
        print("Hotel eliminado")

def update_hotel(id):
    hotel = get_hotel_by_id(id)
    if hotel:
        hotel.estrellas = 4
        session.commit()
        print("Hotel actualizado")

# ===============
# Create
# ===============
# insert_hotel()

# ===============
# List
# ===============
# hoteles = get_hoteles()
# for hotel in hoteles:
#     print_hotel(hotel)

# ===============
# Get
# ===============
# hoteles = get_hoteles()
# hotel = get_hotel_by_id(hoteles[0].id_hotel)
# print_hotel(hotel)

# ===============
# Update
# ===============
# hoteles = get_hoteles()
# update_hotel(hoteles[0].id_hotel)

# ===============
# Delete
# ===============
# hoteles = get_hoteles()
# delete_hotel(hoteles[0].id_hotel)
