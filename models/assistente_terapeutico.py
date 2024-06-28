from sqlalchemy import Column, String, Integer
from  models import Base

class AssistenteTerapeutico(Base):
    __tablename__ = 'assistente_terapeutico'

    id = Column("pk_assistente_terapeutico", Integer,primary_key=True)
    nome = Column(String(120))
    telefone = Column(String(120))
    cidade = Column(String(120))
    estado = Column(String(120))



    def __init__(self,nome,cidade,estado,telefone):
        self.nome = nome
        self.telefone = telefone
        self.cidade = cidade
        self.estado = estado

    def __str__(self):
        return f'{self.nome} | {self.telefone}'