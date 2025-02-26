from  session import session
from models import Cliente
import uuid


def print_client(client):
	print(client.id_cliente, client.nombre, client.apellidos, client.telefono, client.email, client.direccion)

def get_clients():
	clients = session.query(Cliente).all()
	return clients

def get_client_by_id(id):
	client = session.get(Cliente, id)
	return client

def insert_client():
	client = Cliente(
		id_cliente=str(uuid.uuid4()),
		nombre="Daniel",
		apellidos="Martinez",
		telefono="523312223221",
		email="daniel@gmail.com",
		direccion="Av. Mexico #33"
	)

	session.add(client)
	session.commit()
	print("Client created")


def delete_client(id):
	client = get_client_by_id(id)

	if(client):
		session.delete(client)
		session.commit()
		print("Client deleted")

def update_client(id):
	client = get_client_by_id(id)

	if(client):
		client.email = "updated@email.com"
		session.commit()
		print("Client updated")


#	===============
#	Create
#	===============

# insert_client()



#	===============
#	List
#	===============

# clients = get_clients()
# for client in clients:
# 	print_client(client)


#	===============
#	Get
#	===============

# clients = get_clients()
# client = get_client_by_id(clients[0].id_cliente)
# print_client(client)



#	===============
#	Update
#	===============

# clients = get_clients()
# update_client(clients[0].id_cliente)



#	===============
#	Delete
#	===============
# clients = get_clients()
# delete_client(clients[0].id_cliente)



