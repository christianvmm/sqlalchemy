from session import session
from models import Evento
from tipo_eventos import insert_tipo_evento
from platillos_entrada import insert_entrada
from platillos_fuerte import insert_platofuerte
from postres import insert_postre
from datetime import date
import uuid

# Listar los eventos programados en una fecha determinada: 
# Se requiere una consulta que retorne todos los eventos que 
# están programados para una fecha específica, 
# incluyendo detalles como el tipo de evento, la ubicación y el cliente asociado.

def create_fake_event():
	tipo_evento = insert_tipo_evento()
	platillo_entrada = insert_entrada()
	platillo_fuerte = insert_platofuerte()
	postre = insert_postre()

	evento = Evento(
		id_evento=str(uuid.uuid4()),
		id_tipo=tipo_evento.id_tipo,
		id_entrada=platillo_entrada.id_entrada,
		id_platofuerte=platillo_fuerte.id_platofuerte,
		id_postre=postre.id_postre,

		nombre='Cena de Gala',
		descripcion='Una cena elegante para todos los empleados.',
		fecha_solicitud=date.today(),
		status='activo',  
		empleados_requeridos=10
	)

	# record "new" has no field "fecha_evento"
	# CONTEXT:  SQL expression "NEW.fecha_solicitud > NEW.fecha_evento"
	# PL/pgSQL function validar_fecha_evento() line 3 at IF
	session.add(evento)
	session.commit()
	print("Evento creado")


# create_fake_event()


def listar_eventos_por_fecha(session, fecha: date):
	return session.query(Evento).all()

eventos = listar_eventos_por_fecha(session, date.today())
for evento in eventos:
    print(evento.nombre, evento.descripcion)
