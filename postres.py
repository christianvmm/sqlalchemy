from session import session
from models import Postre
import uuid

def print_postre(postre):
	print(postre.id_postre, postre.nombre, postre.descripcion)

def get_postres():
	postres = session.query(Postre).all()
	return postres

def get_postre_by_id(id):
	postre = session.get(Postre, id)
	return postre

def insert_postre():
	postre = Postre(
		id_postre=str(uuid.uuid4()),
		nombre="Tiramisú",
		descripcion="Postre italiano con capas de bizcocho de café y crema de mascarpone"
	)
    
	session.add(postre)
	session.commit()
	print("Postre creado")
	return postre

def delete_postre(id):
	postre = get_postre_by_id(id)
	if postre:
		session.delete(postre)
		session.commit()
		print("Postre eliminado")

def update_postre(id):
	postre = get_postre_by_id(id)
	if postre:
		postre.descripcion = "Postre italiano con bizcocho de café, crema de mascarpone y cacao en polvo"
		session.commit()
		print("Postre actualizado")
		