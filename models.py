# coding: utf-8
from sqlalchemy import CHAR, CheckConstraint, Column, Date, Enum, Float, ForeignKey, Integer, String, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Cliente(Base):
    __tablename__ = 'clientes'
    __table_args__ = (
        CheckConstraint("telefono ~ '^[0-9]+$'::text"),
    )

    id_cliente = Column(UUID, primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellidos = Column(String(50), nullable=False)
    telefono = Column(CHAR(12), nullable=False)
    email = Column(String(30), nullable=False, unique=True)
    direccion = Column(String(80), nullable=False)


class DiasFeriado(Base):
    __tablename__ = 'dias_feriados'

    id_feriado = Column(UUID, primary_key=True)
    fecha = Column(Date, nullable=False, unique=True)
    nombre = Column(String(50), nullable=False)


class Empleado(Base):
    __tablename__ = 'empleados'
    __table_args__ = (
        CheckConstraint("telefono ~ '^[0-9]+$'::text"),
    )

    id_empleado = Column(UUID, primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellidos = Column(String(50), nullable=False)
    telefono = Column(CHAR(12), nullable=False)


class Hotel(Base):
    __tablename__ = 'hotel'
    __table_args__ = (
        CheckConstraint('(estrellas >= 1) AND (estrellas <= 5)'),
    )

    id_hotel = Column(UUID, primary_key=True)
    nombre = Column(String(50), nullable=False)
    direccion = Column(String(100), nullable=False)
    estrellas = Column(Integer)


class PlatillosEntrada(Base):
    __tablename__ = 'platillos_entrada'

    id_entrada = Column(UUID, primary_key=True)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(255), nullable=False)


class PlatillosFuerte(Base):
    __tablename__ = 'platillos_fuertes'

    id_platofuerte = Column(UUID, primary_key=True)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(255), nullable=False)


class Postre(Base):
    __tablename__ = 'postres'

    id_postre = Column(UUID, primary_key=True)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(255), nullable=False)


class Salon(Base):
    __tablename__ = 'salon'
    __table_args__ = (
        CheckConstraint('capacidad > 0'),
        CheckConstraint('precio > (0)::double precision')
    )

    id_salon = Column(UUID, primary_key=True)
    nombre = Column(String(50), nullable=False)
    capacidad = Column(Integer, nullable=False)
    precio = Column(Float, nullable=False)


class Servicio(Base):
    __tablename__ = 'servicios'
    __table_args__ = (
        CheckConstraint('precio_fijo > (0)::double precision'),
    )

    id_servicio = Column(UUID, primary_key=True)
    tipo = Column(String(50), nullable=False)
    precio_fijo = Column(Float, nullable=False)


class Temporada(Base):
    __tablename__ = 'temporadas'
    __table_args__ = (
        CheckConstraint('incremento_precio >= (0)::double precision'),
    )

    id_temporada = Column(UUID, primary_key=True)
    nombre = Column(String(50), nullable=False)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)
    incremento_precio = Column(Float)


class TipoEvento(Base):
    __tablename__ = 'tipo_eventos'

    id_tipo = Column(UUID, primary_key=True)
    nombre = Column(String(50), nullable=False)


class Evento(Base):
    __tablename__ = 'eventos'

    id_evento = Column(UUID, primary_key=True)
    id_tipo = Column(ForeignKey('tipo_eventos.id_tipo'), nullable=False)
    id_entrada = Column(ForeignKey('platillos_entrada.id_entrada'), nullable=False)
    id_platofuerte = Column(ForeignKey('platillos_fuertes.id_platofuerte'), nullable=False)
    id_postre = Column(ForeignKey('postres.id_postre'), nullable=False)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(255), nullable=False)
    fecha_solicitud = Column(Date, nullable=False, server_default=text("CURRENT_DATE"))
    status = Column(Enum('activo', 'modificado', 'cancelado', name='estado_evento'), nullable=False, server_default=text("'activo'::estado_evento"))
    empleados_requeridos = Column(Integer, nullable=False, server_default=text("0"))

    platillos_entrada = relationship('PlatillosEntrada')
    platillos_fuerte = relationship('PlatillosFuerte')
    postre = relationship('Postre')
    tipo_evento = relationship('TipoEvento')


class DetallesEvento(Base):
    __tablename__ = 'detalles_evento'
    __table_args__ = (
        CheckConstraint('cantidad > 0'),
    )

    id_detalle = Column(UUID, primary_key=True)
    id_evento = Column(ForeignKey('eventos.id_evento'), nullable=False)
    id_servicio = Column(ForeignKey('servicios.id_servicio'), nullable=False)
    cantidad = Column(Integer, nullable=False)

    evento = relationship('Evento')
    servicio = relationship('Servicio')


class EmpleadoEvento(Base):
    __tablename__ = 'empleado_evento'

    id_empleado = Column(ForeignKey('empleados.id_empleado'), primary_key=True, nullable=False)
    id_evento = Column(ForeignKey('eventos.id_evento'), primary_key=True, nullable=False)
    rol_empleado = Column(Enum('mesero', 'chef', 'bartender', 'host', 'lavaplatos', name='roles_empleados'), nullable=False)
    horario_ingreso = Column(String(15), nullable=False)
    horario_salida = Column(String(15), nullable=False)

    empleado = relationship('Empleado')
    evento = relationship('Evento')


class ModificacionesEvento(Base):
    __tablename__ = 'modificaciones_eventos'

    id_modificacion = Column(UUID, primary_key=True)
    id_evento = Column(ForeignKey('eventos.id_evento'), nullable=False)
    fecha_modificacion = Column(Date, nullable=False, server_default=text("CURRENT_DATE"))
    nombre_anterior = Column(String(50))
    nombre_nuevo = Column(String(50))
    descripcion_anterior = Column(String(255))
    descripcion_nueva = Column(String(255))

    evento = relationship('Evento')


class Reservacione(Base):
    __tablename__ = 'reservaciones'
    __table_args__ = (
        CheckConstraint('fecha_evento > fecha_reservacion'),
    )

    id_reservacion = Column(UUID, primary_key=True)
    id_cliente = Column(ForeignKey('clientes.id_cliente'), nullable=False)
    id_evento = Column(ForeignKey('eventos.id_evento'), nullable=False)
    id_salon = Column(ForeignKey('salon.id_salon'), nullable=False)
    fecha_reservacion = Column(Date, nullable=False, server_default=text("CURRENT_DATE"))
    fecha_evento = Column(Date, nullable=False)
    fecha_cancelacion = Column(Date)
    status = Column(Enum('pendiente', 'confirmada', 'cancelada', name='estado_reservacion'), nullable=False, server_default=text("'pendiente'::estado_reservacion"))

    cliente = relationship('Cliente')
    evento = relationship('Evento')
    salon = relationship('Salon')


class FacturacionReservacion(Base):
    __tablename__ = 'facturacion_reservacion'
    __table_args__ = (
        CheckConstraint('costo_total >= (0)::double precision'),
        CheckConstraint('descuento >= (0)::double precision'),
        CheckConstraint('penalizacion >= (0)::double precision')
    )

    id_facturacion = Column(UUID, primary_key=True)
    id_reservacion = Column(ForeignKey('reservaciones.id_reservacion'), nullable=False)
    costo_total = Column(Float)
    descuento = Column(Float, server_default=text("0"))
    penalizacion = Column(Float, server_default=text("0"))
    fecha_pago = Column(Date)
    divisa = Column(Enum('MXN', 'USD', 'EUR', 'CAD', 'ARG', 'FR', name='divisas'), nullable=False)

    reservacione = relationship('Reservacione')


class DetallesFacturacion(Base):
    __tablename__ = 'detalles_facturacion'
    __table_args__ = (
        CheckConstraint('costo >= (0)::double precision'),
    )

    id_facturacion = Column(ForeignKey('facturacion_reservacion.id_facturacion'), primary_key=True, nullable=False)
    id_servicio = Column(ForeignKey('servicios.id_servicio'), primary_key=True, nullable=False)
    costo = Column(Float, nullable=False)

    facturacion_reservacion = relationship('FacturacionReservacion')
    servicio = relationship('Servicio')
