from models.base import Base
from models.pessoa import Pessoa
from sqlalchemy.ext.declarative import AbstractConcreteBase
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship


class Neuroatipico(Pessoa,Base):
    __tablename__ = 'pessoa_neuroatipica'
    
    sensibilidade = Column(String(120))
    restricao_alimentar = Column(String(120))
    nivel_suporte = Column(Integer)
    cpf_tutor = Column(Integer)
    cpf_neuroatípico = Column(Integer, unique=True)