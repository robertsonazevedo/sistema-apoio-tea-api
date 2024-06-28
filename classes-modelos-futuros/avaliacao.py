from models.base import Base
from models.neuroatipico import Neuroatipico
from models.terapeuta import Terapeuta
from datetime import datetime
from sqlalchemy import Columm, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship

class Avaliacao(Base):
    __tablename__ = 'avaliacao'

    id_avaliacao = Columm(Integer,primary_key=True)
    cpf_neuroatípica = Columm(Integer(11))
    cpf_terapeuta = Columm(Integer(11))
    nota_terapeuta = Columm(String(120))
    data_avaliacao = Columm(DateTime())
