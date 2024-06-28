from models.base import Base
from sqlalchemy.ext.declarative import AbstractConcreteBase
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship

class Pessoa(Base):
    __tablename__ = 'pessoa'

    cpf = Column(Integer,primary_key=True)
    nome = Column(String(120))
    data_nascimento = Column(DateTime())
    sexo = Column(String(1))
    telefone = Column(Integer, unique=True)
    email = Column(String(120), unique=True)
    data_cadastro = Column(DateTime())
