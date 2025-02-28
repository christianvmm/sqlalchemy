from session import session
from sqlalchemy import select
from eventos import get_eventos
from models import ModificacionesEvento

def obtener_historial_modificaciones(id_evento: str):
    query = (
        select(
            ModificacionesEvento.fecha_modificacion,
            ModificacionesEvento.nombre_anterior,
            ModificacionesEvento.nombre_nuevo,
            ModificacionesEvento.descripcion_anterior,
            ModificacionesEvento.descripcion_nueva
        )
        .where(ModificacionesEvento.id_evento == id_evento)
        .order_by(ModificacionesEvento.fecha_modificacion.desc())
    )

    resultado = session.execute(query).fetchall()
    return resultado

# Uso de la función (ejemplo)
eventos = get_eventos()
historial = obtener_historial_modificaciones(eventos[0].id_evento)

print(f"\nHistorial de modificaciones para el evento con ID: {eventos[0].id_evento}\n")
print("=" * 80)

for registro in historial:
    fecha, nombre_anterior, nombre_nuevo, descripcion_anterior, descripcion_nueva = registro
    print(f"📅 Fecha de modificación: {fecha}")
    print(f"🔹 Nombre anterior: {nombre_anterior}")
    print(f"🔹 Nombre nuevo: {nombre_nuevo}")
    print(f"📝 Descripción anterior: {descripcion_anterior}")
    print(f"📝 Descripción nueva: {descripcion_nueva}")
    print("-" * 80)
