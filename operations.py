from session import session
from models import Evento, EmpleadoEvento, Empleado
from tipo_eventos import insert_tipo_evento
from platillos_entrada import insert_entrada
from platillos_fuerte import insert_platofuerte
from postres import insert_postre
from datetime import date
import uuid

from sqlalchemy.orm import aliased
from sqlalchemy import and_, not_, exists

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
     

#Encontrar empleados disponibles para un rol específico en un rango de fechas: Esta consulta debe identificar a los empleados que no tienen asignaciones en conflicto 
#y que pueden desempeñar un rol determinado (por ejemplo, mesero o coordinador) durante un período de tiempo específico.

def empleados_disponibles(rol, fecha_inicio, fecha_fin):
    EmpleadoAlias = aliased(Empleado)
    EmpleadoEventoAlias = aliased(EmpleadoEvento)
    EventoAlias = aliased(Evento)
    
    subquery = (
        session.query(EmpleadoEventoAlias.id_empleado)
        .join(EventoAlias, EmpleadoEventoAlias.id_evento == EventoAlias.id_evento)
        .filter(
            and_(
                EmpleadoEventoAlias.rol_empleado == rol,
                EventoAlias.fecha_solicitud.between(fecha_inicio, fecha_fin)
            )
        )
        .subquery()
    )
    
    empleados_disponibles = (
        session.query(EmpleadoAlias)
        .filter(
            and_(
                EmpleadoAlias.id_empleado.notin_(subquery),
                EmpleadoEventoAlias.rol_empleado == rol
            )
        )
    ).all()
    
    return empleados_disponibles


# create_fake_event()
empleados = empleados_disponibles('mesero', '2025-03-01', '2025-03-10')

# Mostrar resultados en la consola
for empleado in empleados:
    print(f"ID: {empleado.id_empleado}, Nombre: {empleado.nombre} {empleado.apellidos}, Teléfono: {empleado.telefono}")






# Insertar empleados de ejemplo y empleados_eventos



def empleados_disponibles(rol, fecha_inicio, fecha_fin):
    EmpleadoAlias = aliased(Empleado)
    EmpleadoEventoAlias = aliased(EmpleadoEvento)
    EventoAlias = aliased(Evento)
    
    subquery = (
        session.query(EmpleadoEventoAlias.id_empleado)
        .join(EventoAlias, EmpleadoEventoAlias.id_evento == EventoAlias.id_evento)
        .filter(
            and_(
                EmpleadoEventoAlias.rol_empleado == rol,
                EventoAlias.fecha_solicitud.between(fecha_inicio, fecha_fin)
            )
        )
        .subquery()
    )
    
    empleados_disponibles = (
        session.query(EmpleadoAlias)
        .filter(
            and_(
                EmpleadoAlias.id_empleado.notin_(subquery),
                EmpleadoEventoAlias.rol_empleado == rol
            )
        )
    ).all()
    
    return empleados_disponibles

def agregar_empleados_ejemplo():
    empleados = [
        Empleado(id_empleado=str(uuid.uuid4()), nombre="Juan", apellidos="Pérez", telefono="1234567890"),
        Empleado(id_empleado=str(uuid.uuid4()), nombre="María", apellidos="Gómez", telefono="0987654321"),
        Empleado(id_empleado=str(uuid.uuid4()), nombre="Carlos", apellidos="Rodríguez", telefono="1122334455"),
    ]
    session.add_all(empleados)
    session.commit()
    print("Empleados de ejemplo añadidos.")

def agregar_evento_empleado_ejemplo(session, id_empleado, id_evento, rol, horario_ingreso, horario_salida):
    empleado_evento = EmpleadoEvento(
        id_empleado=id_empleado,
        id_evento=id_evento,
        rol_empleado=rol,
        horario_ingreso=horario_ingreso,
        horario_salida=horario_salida
    )
    session.add(empleado_evento)
    session.commit()
    print("Evento de empleado añadido.")




agregar_empleados_ejemplo()  
agregar_evento_empleado_ejemplo(id_empleado, id_evento, rol, horario_ingreso, horario_salida)


# def listar_eventos_por_fecha(session, fecha: date):
# 	return session.query(Evento).all()

# eventos = listar_eventos_por_fecha(session, date.today())
# print(len(eventos))
# for evento in eventos:
#     print(evento.nombre, evento.descripcion)
