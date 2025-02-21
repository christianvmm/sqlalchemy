# coding: utf-8
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Index, Integer, Numeric, String, Table, Text, text
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class PrismaMigration(Base):
    __tablename__ = '_prisma_migrations'

    id = Column(String(36), primary_key=True)
    checksum = Column(String(64), nullable=False)
    finished_at = Column(DateTime(True))
    migration_name = Column(String(255), nullable=False)
    logs = Column(Text)
    rolled_back_at = Column(DateTime(True))
    started_at = Column(DateTime(True), nullable=False, server_default=text("now()"))
    applied_steps_count = Column(Integer, nullable=False, server_default=text("0"))


class SaveMediaIgSearch(Base):
    __tablename__ = 'save_media_ig_searches'

    id = Column(Integer, primary_key=True, server_default=text("nextval('save_media_ig_searches_id_seq'::regclass)"))
    type = Column(Text, nullable=False)
    term = Column(Text, nullable=False)
    succeeded = Column(Boolean, nullable=False, server_default=text("true"))
    created_at = Column(TIMESTAMP(precision=3), nullable=False, server_default=text("CURRENT_TIMESTAMP"))


class SaveMediaIgToken(Base):
    __tablename__ = 'save_media_ig_tokens'

    id = Column(Integer, primary_key=True, server_default=text("nextval('save_media_ig_tokens_id_seq'::regclass)"))
    email = Column(Text)
    mid = Column(Text, nullable=False)
    datr = Column(Text, nullable=False)
    ig_did = Column(Text, nullable=False)
    csrftoken = Column(Text, nullable=False)
    ds_user_id = Column(Text, nullable=False)
    sessionid = Column(Text, nullable=False)
    wd = Column(Text, nullable=False)
    rur = Column(Text, nullable=False)
    succeeded = Column(Boolean, nullable=False, server_default=text("true"))
    created_at = Column(TIMESTAMP(precision=3), nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP(precision=3), nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    shbid = Column(Text)
    shbts = Column(Text)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, server_default=text("nextval('users_id_seq'::regclass)"))
    first_name = Column(Text)
    last_name = Column(Text)
    email = Column(Text, nullable=False, unique=True)
    email_verified = Column(TIMESTAMP(precision=3))
    password = Column(Text, nullable=False)
    image = Column(Text)


t_verification_tokens = Table(
    'verification_tokens', metadata,
    Column('identifier', Text, nullable=False),
    Column('token', Text, nullable=False, unique=True),
    Column('expires', TIMESTAMP(precision=3), nullable=False),
    Index('verification_tokens_identifier_token_key', 'identifier', 'token', unique=True)
)


class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, server_default=text("nextval('accounts_id_seq'::regclass)"))
    user_id = Column(ForeignKey('users.id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
    name = Column(Text, nullable=False)
    balance = Column(Numeric(12, 2), nullable=False, server_default=text("0.00"))
    color = Column(Text, nullable=False, server_default=text("'#4579f0'::text"))
    created_at = Column(TIMESTAMP(precision=3), nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP(precision=3), nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    active = Column(Boolean, nullable=False, server_default=text("true"))

    user = relationship('User')


class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True, server_default=text("nextval('notes_id_seq'::regclass)"))
    user_id = Column(ForeignKey('users.id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP(precision=3), nullable=False, server_default=text("CURRENT_TIMESTAMP"))

    user = relationship('User')


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, server_default=text("nextval('transactions_id_seq'::regclass)"))
    user_id = Column(ForeignKey('users.id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
    destiny_id = Column(ForeignKey('accounts.id', ondelete='SET NULL', onupdate='CASCADE'))
    amount = Column(Numeric(10, 2), nullable=False)
    description = Column(Text)
    category_id = Column(Integer)
    type = Column(Text, nullable=False, server_default=text("'INC'::text"))
    date = Column(TIMESTAMP(precision=3), nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    created_at = Column(TIMESTAMP(precision=3), nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP(precision=3), nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    account_id = Column(ForeignKey('accounts.id', ondelete='SET NULL', onupdate='CASCADE'))
    currency = Column(Text, nullable=False, server_default=text("'MXN'::text"))

    account = relationship('Account', primaryjoin='Transaction.account_id == Account.id')
    destiny = relationship('Account', primaryjoin='Transaction.destiny_id == Account.id')
    user = relationship('User')
