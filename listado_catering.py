from session import session
from models import Evento, DetallesEvento, Servicio, Reservacione
from tipo_eventos import insert_tipo_evento
from platillos_entrada import insert_entrada
from platillos_fuerte import insert_platofuerte
from postres import insert_postre
from datetime import date
import uuid

def insert_catering_service():
    """Inserta el servicio de catering si no existe y lo devuelve."""
    catering = session.query(Servicio).filter_by(tipo="Catering").first()
    if not catering:
        catering = Servicio(id_servicio=str(uuid.uuid4()), tipo="Catering", precio_fijo=5000.00)
        session.add(catering)
        session.commit()
    return catering

def create_fake_event_with_catering():
    """Crea un evento con servicio de catering."""
    tipo_evento = insert_tipo_evento()
    platillo_entrada = insert_entrada()
    platillo_fuerte = insert_platofuerte()
    postre = insert_postre()
    servicio_catering = insert_catering_service()

    evento = Evento(
        id_evento=str(uuid.uuid4()),
        id_tipo=tipo_evento.id_tipo,
        id_entrada=platillo_entrada.id_entrada,
        id_platofuerte=platillo_fuerte.id_platofuerte,
        id_postre=postre.id_postre,
        nombre="Boda Elegante",
        descripcion="Una boda con servicio de catering premium.",
        fecha_solicitud=date.today(),
        status="activo",
        empleados_requeridos=15
    )

    session.add(evento)
    session.commit()

    # Relacionar el evento con el servicio de catering
    detalle_evento = DetallesEvento(
        id_detalle=str(uuid.uuid4()),
        id_evento=evento.id_evento,
        id_servicio=servicio_catering.id_servicio,
        cantidad=1
    )

    session.add(detalle_evento)
    session.commit()
    print("Evento con servicio de catering creado.")

def get_events_with_catering_by_month(year, month):
    """Consulta eventos con catering en un mes específico."""
    eventos_con_catering = (
        session.query(Evento.nombre, Evento.descripcion, Reservacione.fecha_evento, DetallesEvento.cantidad)
        .join(DetallesEvento, DetallesEvento.id_evento == Evento.id_evento)
        .join(Servicio, Servicio.id_servicio == DetallesEvento.id_servicio)
        .join(Reservacione, Reservacione.id_evento == Evento.id_evento)
        .filter(Servicio.tipo == "Catering")
        .filter(Reservacione.fecha_evento.between(f"{year}-{month}-01", f"{year}-{month}-31"))
        .all()
    )

    for evento in eventos_con_catering:
        print(f"Evento: {evento.nombre}, Descripción: {evento.descripcion}, Fecha: {evento.fecha_evento}, Cantidad de servicios: {evento.cantidad}")

# Crear un evento de prueba con catering
# create_fake_event_with_catering()

from datetime import date

def listar_eventos_con_catering_por_mes(session, year, month):
    """Lista los eventos con servicio de catering en un mes específico y los muestra en la consola."""
    fecha_inicio = date(year, month, 1)
    
    # Para calcular el último día del mes correctamente:
    if month == 12:
        fecha_fin = date(year + 1, 1, 1)  # Primer día del siguiente año
    else:
        fecha_fin = date(year, month + 1, 1)  # Primer día del siguiente mes

    eventos = (
        session.query(Evento)
        .join(DetallesEvento, DetallesEvento.id_evento == Evento.id_evento)
        .join(Servicio, Servicio.id_servicio == DetallesEvento.id_servicio)
        .join(Reservacione, Reservacione.id_evento == Evento.id_evento)
        .filter(Servicio.tipo == "Catering")
        .filter(Reservacione.fecha_evento >= fecha_inicio, Reservacione.fecha_evento < fecha_fin)
        .all()
    )

    print(f"Eventos con catering en {year}-{month}: {len(eventos)}")
    for evento in eventos:
        print(f"{evento.nombre} - {evento.descripcion}")

# Llamada a la función para listar eventos con catering en febrero 2025
listar_eventos_con_catering_por_mes(session, 2025, 2)


