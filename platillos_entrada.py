from session import session
from models import PlatillosEntrada
import uuid

def print_entrada(entrada):
	print(entrada.id_entrada, entrada.nombre, entrada.descripcion)

def get_entradas():
	entradas = session.query(PlatillosEntrada).all()
	return entradas

def get_entrada_by_id(id):
	entrada = session.get(PlatillosEntrada, id)
	return entrada

def insert_entrada():
	entrada = PlatillosEntrada(
		id_entrada=str(uuid.uuid4()),
		nombre="Bruschetta",
		descripcion="Pan crujiente con tomate, albahaca y aceite de oliva"
	)
	
	session.add(entrada)
	session.commit()
	print("Platillo de entrada creado")
	return entrada

def delete_entrada(id):
	entrada = get_entrada_by_id(id)
	
	if entrada:
		session.delete(entrada)
		session.commit()
		print("Platillo de entrada eliminado")

def update_entrada(id):
	entrada = get_entrada_by_id(id)
	if entrada:
		entrada.descripcion = "Pan crujiente con tomate cherry, albahaca fresca y aceite de oliva extra virgen"
		session.commit()
		print("Platillo de entrada actualizado")
