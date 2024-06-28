from models.base import Base
from models.neuroatipico import Neuroatipico
from models.terapeuta import Terapeuta
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship

class Avaliacao(Base):
    __tablename__ = 'atendimento'

    id_atendimento = Column(Integer,primary_key=True)
    cpf_neuroatípica = Column(Integer(11))
    cpf_terapeuta = Column(Integer(11))
    historico = Column(String(120))
    data_atendimento = Column(DateTime())