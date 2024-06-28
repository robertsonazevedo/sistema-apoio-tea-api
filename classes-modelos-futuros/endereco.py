from models.base import Base
from models.pessoa import Pessoa
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship

class Endereco(Base):
    __tablename__ = 'endereco'

    logradouro = Column(String(120))
    numero = Column(Integer)
    complemento = Column(String(120))
    bairro = Column(String(120))
    cidade = Column(String(120))
    estado = Column(String(120))
    pais = Column(String(120))
    cep = Column(Integer)
    data_cadastro = Column(DateTime())
    cpf_pessoa = Column(Integer)
