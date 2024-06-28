from models.base import Base
from models.pessoa import Pessoa
from sqlalchemy.ext.declarative import AbstractConcreteBase
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship

class Terapeuta(Base):
    __tablename__ = 'pessoa_terapeuta'

    supervisao = Column(String(120))
    especialidade = Column(String(120))
    registro_conselho = Column(Integer, unique=True)
    formacao = Column(String(120))
    cpf_terapeuta = Column(Integer, unique=True)